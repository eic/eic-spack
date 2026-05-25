# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Overlay of the builtin zlib-ng package that adds an ``hwcaps`` multi-valued
# variant.  When set, additional optimised shared-library builds are placed in
# ``lib/glibc-hwcaps/<level>/`` inside the install prefix.  Any binary whose
# RPATH already points at the prefix ``lib/`` directory gets automatic
# runtime CPU dispatch through the glibc dynamic-linker hwcaps mechanism —
# no changes to the consumer binary are needed.

import glob as _glob
import os

from spack_repo.builtin.packages.zlib_ng.package import (
    AutotoolsBuilder as _BuiltinAutotoolsBuilder,
    ZlibNg as _BuiltinZlibNg,
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


def _hwcaps_flags(target_name):
    subdir = _GLIBC_HWCAPS_SUBDIRS.get(target_name)
    return f"-march={subdir}" if subdir else ""


class ZlibNg(_BuiltinZlibNg):
    __doc__ = _BuiltinZlibNg.__doc__

    variant(
        "hwcaps",
        values=("none",) + _valid_hwcaps_values(),
        default="none",
        multi=True,
        description=(
            "Build additional optimised shared libraries for the listed glibc hwcaps "
            "levels and install them to lib/glibc-hwcaps/<level>/.  Each level must be "
            "strictly greater than the spec's baseline target in archspec ordering.  "
            "Requires +shared."
        ),
    )

    conflicts("~shared", when="hwcaps=x86_64_v2", msg="hwcaps requires a shared library build")
    conflicts("~shared", when="hwcaps=x86_64_v3", msg="hwcaps requires a shared library build")
    conflicts("~shared", when="hwcaps=x86_64_v4", msg="hwcaps requires a shared library build")


class AutotoolsBuilder(_BuiltinAutotoolsBuilder):
    """AutotoolsBuilder for zlib-ng with optional glibc hwcaps multi-build."""

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

            flags = _hwcaps_flags(target_name)
            hwcaps_dir = join_path(self.spec.prefix, "lib", "glibc-hwcaps", subdir)
            mkdirp(hwcaps_dir)
            self.build_for_hwcaps(target_name, flags, hwcaps_dir)

    def build_for_hwcaps(self, target_name: str, flags: str, hwcaps_dir: str) -> None:
        """Re-build zlib-ng shared libraries with hwcaps optimisation flags.

        Patches the build-system's ``CFLAGS`` in the Makefile to prepend the
        hwcaps march flag (preserving all original compiler defines, include
        paths, and feature flags), runs ``make -B`` to force a full rebuild,
        copies the resulting ``*.so*`` files to *hwcaps_dir*, then restores the
        Makefile to its original state.
        """
        import re as _re

        build_dir = self.build_directory
        makefile_path = join_path(build_dir, "Makefile")

        with open(makefile_path) as fh:
            original_content = fh.read()

        # Prepend the hwcaps -march flag to CFLAGS, keeping all existing flags.
        pattern = _re.compile(r"^(CFLAGS=)(.*)$", _re.MULTILINE)
        if not pattern.search(original_content):
            raise InstallError("hwcaps: could not locate CFLAGS line in Makefile")
        patched_content = pattern.sub(rf"\g<1>{flags} \g<2>", original_content, count=1)

        try:
            with open(makefile_path, "w") as fh:
                fh.write(patched_content)
            with working_dir(build_dir):
                make("-B")
        finally:
            with open(makefile_path, "w") as fh:
                fh.write(original_content)

        # Copy shared-library files (actual ELFs and SONAME/ldconfig symlinks).
        for src in sorted(_glob.glob(join_path(build_dir, "*.so*"))):
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
