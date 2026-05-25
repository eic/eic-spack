# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Overlay of the builtin lz4 package that adds an ``hwcaps`` multi-valued
# variant.  When set, additional optimised shared-library builds are placed in
# ``lib/glibc-hwcaps/<level>/`` inside the install prefix.  Any binary whose
# RPATH already points at the prefix ``lib/`` directory gets automatic
# runtime CPU dispatch through the glibc dynamic-linker hwcaps mechanism —
# no changes to the consumer binary are needed.
#
# lz4 is an ideal showcase for the hwcaps approach: unlike zlib-ng (which
# performs its own runtime SIMD dispatch), lz4 relies on the compiler's
# auto-vectoriser.  Compiling with ``-march=x86-64-v3`` therefore enables
# AVX2 auto-vectorised code paths in the hot compression/decompression loops,
# producing a measurably different (and faster) binary than the baseline.

import glob as _glob
import os

from spack_repo.builtin.packages.lz4.package import (
    MakefileBuilder as _BuiltinMakefileBuilder,
    Lz4 as _BuiltinLz4,
)

from spack.package import *

# ---------------------------------------------------------------------------
# Mapping: archspec target name → glibc hwcaps subdirectory name
#
# Derived at import time from the vendored archspec database rather than
# hardcoded.  For each generic target whose modern-GCC ``-march`` flag name
# matches the glibc hwcaps naming convention (``x86-64-v[2-9]``, defined by
# glibc itself), we record the mapping.  This means new x86_64_v* levels
# added to archspec are picked up automatically.
# ---------------------------------------------------------------------------
import re as _re
import spack.vendor.archspec.cpu as _cpu

_GLIBC_HWCAPS_PATTERN = _re.compile(r"^x86-64-v[2-9]$")


def _build_hwcaps_subdirs():
    result = {}
    for _name, _target in sorted(_cpu.TARGETS.items()):
        if _target.vendor != "generic":
            continue
        _gcc_entries = _target.compilers.get("gcc", [])
        if not _gcc_entries:
            continue
        # First entry has the most-recent (highest minimum) compiler version,
        # i.e. the canonical modern -march name for this target.
        _march_name = _gcc_entries[0].get("name", _name)
        if _GLIBC_HWCAPS_PATTERN.match(_march_name):
            result[_name] = _march_name
    return result


_GLIBC_HWCAPS_SUBDIRS = _build_hwcaps_subdirs()


def _valid_hwcaps_values():
    return tuple(sorted(_GLIBC_HWCAPS_SUBDIRS.keys()))


def _hwcaps_march(target_name):
    subdir = _GLIBC_HWCAPS_SUBDIRS.get(target_name)
    return f"-march={subdir}" if subdir else ""


class Lz4(_BuiltinLz4):
    __doc__ = _BuiltinLz4.__doc__

    variant(
        "hwcaps",
        values=("none",) + _valid_hwcaps_values(),
        default="none",
        multi=True,
        description=(
            "Build additional optimised shared libraries for the listed glibc hwcaps "
            "levels and install them to lib/glibc-hwcaps/<level>/.  Each level must be "
            "strictly greater than the spec's baseline target in archspec ordering.  "
            "Requires libs=shared."
        ),
    )

    conflicts(
        "libs=static",
        when="hwcaps=x86_64_v2",
        msg="hwcaps requires a shared library build (libs=shared)",
    )
    conflicts(
        "libs=static",
        when="hwcaps=x86_64_v3",
        msg="hwcaps requires a shared library build (libs=shared)",
    )
    conflicts(
        "libs=static",
        when="hwcaps=x86_64_v4",
        msg="hwcaps requires a shared library build (libs=shared)",
    )


class MakefileBuilder(_BuiltinMakefileBuilder):
    """MakefileBuilder for lz4 with optional glibc hwcaps multi-build."""

    @run_after("install")
    def install_hwcaps_variants(self):
        """Re-build shared libraries for each requested hwcaps level and install them."""
        if "hwcaps" not in self.spec.variants:
            return
        hwcaps_targets = self.spec.variants["hwcaps"].value
        if not hwcaps_targets or set(hwcaps_targets) == {"none"}:
            return

        baseline_str = str(self.spec.architecture.target)
        try:
            t_baseline = _cpu.TARGETS[baseline_str]
        except KeyError:
            raise InstallError(f"hwcaps: unrecognised baseline target {baseline_str!r}")

        for target_name in hwcaps_targets:
            if target_name == "none":
                continue

            subdir = _GLIBC_HWCAPS_SUBDIRS.get(target_name)
            if not subdir:
                raise InstallError(
                    f"hwcaps: {target_name!r} has no known glibc hwcaps subdirectory; "
                    f"valid values: {_valid_hwcaps_values()!r}"
                )

            try:
                t_hwcaps = _cpu.TARGETS[target_name]
            except KeyError:
                raise InstallError(f"hwcaps: unrecognised archspec target {target_name!r}")

            if not (t_hwcaps > t_baseline):
                raise InstallError(
                    f"hwcaps target {target_name!r} is not strictly greater than "
                    f"baseline target {baseline_str!r} in archspec ordering"
                )

            march_flag = _hwcaps_march(target_name)
            hwcaps_dir = join_path(self.spec.prefix, "lib", "glibc-hwcaps", subdir)
            mkdirp(hwcaps_dir)
            self.build_for_hwcaps(target_name, march_flag, hwcaps_dir)

    def build_for_hwcaps(self, target_name: str, march_flag: str, hwcaps_dir: str) -> None:
        """Re-build lz4 shared library with the hwcaps march flag and copy to hwcaps_dir.

        lz4's lib/Makefile uses ``CFLAGS = $(DEBUGFLAGS) $(USERCFLAGS)`` where
        ``USERCFLAGS`` expands from the ``CFLAGS`` environment variable.  We
        temporarily override ``CFLAGS`` in the environment so that the
        compiler wrapper's ``SPACK_TARGET_ARGS`` (which prepends the baseline
        -march) is overridden by our hwcaps march flag (which appears later on
        the command line — GCC applies the last -march flag).
        """
        pic = self.pkg.compiler.cc_pic_flag
        # Add -O3 because lz4's Makefile prepends -O3 to USERCFLAGS anyway.
        new_cflags = f"{pic} -O3 {march_flag}"

        old_cflags = os.environ.get("CFLAGS")
        os.environ["CFLAGS"] = new_cflags
        try:
            with working_dir(self.build_directory):
                make("-B", "-C", "lib")
        finally:
            if old_cflags is not None:
                os.environ["CFLAGS"] = old_cflags
            else:
                os.environ.pop("CFLAGS", None)

        # Copy shared-library files (actual ELFs and SONAME/ldconfig symlinks).
        src_lib = join_path(self.build_directory, "lib")
        for src in sorted(_glob.glob(join_path(src_lib, "*.so*"))):
            dst = join_path(hwcaps_dir, os.path.basename(src))
            if os.path.islink(src):
                link_target = os.readlink(src)
                if os.path.lexists(dst):
                    os.unlink(dst)
                os.symlink(link_target, dst)
            else:
                if os.path.lexists(dst):
                    os.unlink(dst)
                install(src, dst)
