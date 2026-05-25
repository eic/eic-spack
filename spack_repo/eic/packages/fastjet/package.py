# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Overlay of the builtin fastjet package that adds an ``hwcaps`` multi-valued
# variant.  When set, additional optimised shared-library builds are placed in
# ``lib/glibc-hwcaps/<level>/`` inside the install prefix.  Any binary whose
# RPATH already points at the prefix ``lib/`` directory gets automatic
# runtime CPU dispatch through the glibc dynamic-linker hwcaps mechanism —
# no changes to the consumer binary are needed.
#
# FastJet supports both CMake and Autotools build systems (the EIC stack uses
# CMake via build_system=cmake).  The cmake build scatters shared libraries
# across several subdirectories of the build tree (src/, plugins/SISCone/…),
# so we use a recursive search when collecting the rebuilt objects.  The
# Autotools build places libraries in the source tree's ``src/.libs/`` —
# handled by the AutotoolsBuilder overlay below.

import os

from spack_repo.builtin.build_systems import autotools as _autotools
from spack_repo.builtin.packages.fastjet.package import (
    AutotoolsBuilder as _BuiltinAutotoolsBuilder,
    CMakeBuilder as _BuiltinCMakeBuilder,
    Fastjet as _BuiltinFastjet,
)
from spack_repo.eic.packages.hwcaps_support.package import (
    add_hwcaps_variant,
    copy_so_files,
    copy_so_files_recursive,
    hwcaps_march,
    install_hwcaps_variants,
)

from spack.package import *


class Fastjet(_BuiltinFastjet):
    __doc__ = _BuiltinFastjet.__doc__

    add_hwcaps_variant()


class CMakeBuilder(_BuiltinCMakeBuilder):
    """CMakeBuilder for fastjet with optional glibc hwcaps multi-build."""

    @run_after("install")
    def _install_hwcaps_variants(self):
        install_hwcaps_variants(self, self.build_for_hwcaps)

    def build_for_hwcaps(self, target_name: str, march_flag: str, hwcaps_dir: str) -> None:
        """Re-build FastJet shared libraries with the hwcaps march flag.

        FastJet's cmake build places shared libraries in multiple subdirectories
        of the build tree (e.g. ``src/``, ``plugins/SISCone/…``), so we use a
        recursive search to collect all rebuilt ``lib*.so*`` files.
        """
        with working_dir(self.build_directory):
            cmake(
                f"-DCMAKE_CXX_FLAGS_RELEASE:STRING=-O3 -DNDEBUG {march_flag}",
                f"-DCMAKE_C_FLAGS_RELEASE:STRING=-O3 -DNDEBUG {march_flag}",
                ".",
            )
            make("-B")

        copy_so_files_recursive(self.build_directory, hwcaps_dir)


class AutotoolsBuilder(_BuiltinAutotoolsBuilder):
    """AutotoolsBuilder for fastjet with optional glibc hwcaps multi-build."""

    @run_after("install")
    def _install_hwcaps_variants(self):
        install_hwcaps_variants(self, self.build_for_hwcaps)

    def build_for_hwcaps(self, target_name: str, march_flag: str, hwcaps_dir: str) -> None:
        """Re-build FastJet shared libraries (Autotools build) with hwcaps march flag."""
        with working_dir(self.build_directory):
            make("-B", f"CXXFLAGS=-O3 {march_flag}", f"CFLAGS=-O3 {march_flag}")

        src_libs = join_path(self.build_directory, "src", ".libs")
        if not os.path.isdir(src_libs):
            src_libs = join_path(self.build_directory, ".libs")
        copy_so_files(src_libs, hwcaps_dir)
