# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""Shared infrastructure for glibc hwcaps multi-arch shared library builds.

This module is **not a real installable package**.  It is a helper module
imported by overlay packages that want to add the ``hwcaps`` multi-valued
variant.  Typical usage::

    from spack_repo.eic.packages.hwcaps_support.package import (
        GLIBC_HWCAPS_SUBDIRS,
        valid_hwcaps_values,
        hwcaps_march,
        copy_so_files,
        install_hwcaps_variants,
    )

    class MyPackage(_BuiltinPackage):
        variant(
            "hwcaps",
            values=("none",) + valid_hwcaps_values(),
            default="none",
            multi=True,
            description="...",
        )
        for _v in valid_hwcaps_values():
            conflicts("<shared-off-flag>", when=f"hwcaps={_v}",
                      msg="hwcaps requires a shared library build")

    class MyBuilder(_BuiltinBuilder):
        @run_after("install")
        def _install_hwcaps_variants(self):
            install_hwcaps_variants(self, self.build_for_hwcaps)

        def build_for_hwcaps(
            self, target_name: str, march_flag: str, hwcaps_dir: str
        ) -> None:
            # package-specific rebuild logic; copy results with copy_so_files()
            ...

Background
----------
glibc's dynamic linker transparently prefers libraries in
``<prefix>/lib/glibc-hwcaps/<level>/`` over those in ``<prefix>/lib/`` when
running on a CPU that satisfies *level*.  Installing a baseline-optimised
library in ``lib/`` and a higher-level rebuild in
``lib/glibc-hwcaps/x86-64-v3/`` therefore gives zero-overhead CPU dispatch
with no changes to consumer binaries.

The glibc hwcaps subdirectory names (``x86-64-v2``, ``x86-64-v3``, …) are
defined by glibc itself and happen to coincide with the GCC ``-march=`` flag
names for the generic x86-64 baseline levels.  This module derives the
mapping automatically from the vendored archspec CPU database: for each
generic target whose modern-GCC ``-march`` name matches the pattern
``^x86-64-v[2-9]$``, the target name and march name are recorded.  New
x86_64_v* levels added to archspec are therefore picked up without any code
change here.
"""

import glob as _glob
import os
import re as _re

import spack.vendor.archspec.cpu as _cpu
from spack.error import InstallError
from spack.package import *

# ---------------------------------------------------------------------------
# Mapping: archspec target name → glibc hwcaps subdirectory name
# ---------------------------------------------------------------------------

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


#: Mapping from archspec target name to the glibc hwcaps subdirectory name.
#: Derived at import time from the vendored archspec CPU database.
GLIBC_HWCAPS_SUBDIRS = _build_hwcaps_subdirs()


def valid_hwcaps_values():
    """Return a sorted tuple of valid archspec target names for the hwcaps variant."""
    return tuple(sorted(GLIBC_HWCAPS_SUBDIRS.keys()))


def hwcaps_march(target_name):
    """Return the ``-march=<subdir>`` flag for *target_name*, or an empty string."""
    subdir = GLIBC_HWCAPS_SUBDIRS.get(target_name)
    return f"-march={subdir}" if subdir else ""


def copy_so_files(src_dir, hwcaps_dir):
    """Copy ``*.so*`` files (ELFs and SONAME/ldconfig symlinks) into *hwcaps_dir*.

    Symlinks are re-created as symlinks; regular files are copied with spack's
    ``install()`` (which preserves permissions).  Existing destinations are
    silently replaced.
    """
    for src in sorted(_glob.glob(join_path(src_dir, "*.so*"))):
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


def install_hwcaps_variants(builder, build_fn):
    """Iterate over the ``hwcaps`` variant values and call *build_fn* for each.

    Parameters
    ----------
    builder:
        The spack Builder instance (provides ``spec``, ``spec.prefix``, etc.).
    build_fn:
        Callable ``(target_name: str, march_flag: str, hwcaps_dir: str) -> None``
        that performs the package-specific rebuild.  It is responsible for
        placing the rebuilt shared libraries in *hwcaps_dir* (typically by
        calling :func:`copy_so_files`).
    """
    if "hwcaps" not in builder.spec.variants:
        return
    hwcaps_targets = builder.spec.variants["hwcaps"].value
    if not hwcaps_targets or set(hwcaps_targets) == {"none"}:
        return

    baseline_str = str(builder.spec.architecture.target)
    try:
        t_baseline = _cpu.TARGETS[baseline_str]
    except KeyError:
        raise InstallError(f"hwcaps: unrecognised baseline target {baseline_str!r}")

    for target_name in hwcaps_targets:
        if target_name == "none":
            continue

        subdir = GLIBC_HWCAPS_SUBDIRS.get(target_name)
        if not subdir:
            raise InstallError(
                f"hwcaps: {target_name!r} has no known glibc hwcaps subdirectory; "
                f"valid values: {valid_hwcaps_values()!r}"
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

        march_flag = hwcaps_march(target_name)
        hwcaps_dir = join_path(builder.spec.prefix, "lib", "glibc-hwcaps", subdir)
        mkdirp(hwcaps_dir)
        build_fn(target_name, march_flag, hwcaps_dir)


# ---------------------------------------------------------------------------
# Stub Package class — required so spack can load this file as a package
# module.  This package is never intended to be installed.
# ---------------------------------------------------------------------------

class HwcapsSupport(Package):
    """Internal helper module — provides shared hwcaps build infrastructure.

    This is not a real installable package.  See the module docstring for
    usage instructions.
    """

    homepage = "https://github.com/eic/eic-spack"
    phases: list = []
