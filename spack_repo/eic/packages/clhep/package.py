# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Overlay of the builtin clhep package that adds an ``hwcaps`` multi-valued
# variant.  When set, additional optimised shared-library builds are placed in
# ``lib/glibc-hwcaps/<level>/`` inside the install prefix.  Any binary whose
# RPATH already points at the prefix ``lib/`` directory gets automatic
# runtime CPU dispatch through the glibc dynamic-linker hwcaps mechanism —
# no changes to the consumer binary are needed.
#
# CLHEP uses CMake and places all compiled shared libraries directly in
# ``lib/`` within the cmake build directory.  We re-run cmake with the hwcaps
# march flag appended to ``CMAKE_CXX_FLAGS_RELEASE`` and ``CMAKE_C_FLAGS_RELEASE``
# (the flags used in a Release build), then force a full rebuild with ``make -B``
# and copy the resulting shared libraries.

from spack_repo.builtin.build_systems import cmake as _cmake
from spack_repo.builtin.packages.clhep.package import Clhep as _BuiltinClhep
from spack_repo.eic.packages.hwcaps_support.package import (
    add_hwcaps_variant,
    copy_so_files,
    hwcaps_march,
    install_hwcaps_variants,
)

from spack.package import *


class Clhep(_BuiltinClhep):
    __doc__ = _BuiltinClhep.__doc__

    add_hwcaps_variant()


class CMakeBuilder(_cmake.CMakeBuilder):
    """CMakeBuilder for clhep with optional glibc hwcaps multi-build."""

    @run_after("install")
    def _install_hwcaps_variants(self):
        install_hwcaps_variants(self, self.build_for_hwcaps)

    def build_for_hwcaps(self, target_name: str, march_flag: str, hwcaps_dir: str) -> None:
        """Re-build CLHEP shared libraries with the hwcaps march flag.

        Re-runs cmake in the existing build directory with the hwcaps march
        flag appended to the Release-mode C/C++ flags.  This regenerates all
        compiler rule makefiles (``CMakeFiles/*/flags.make``) so that the
        subsequent forced rebuild uses the new flags.  Shared libraries land
        in ``lib/`` within the cmake build directory.
        """
        with working_dir(self.build_directory):
            cmake(
                f"-DCMAKE_CXX_FLAGS_RELEASE:STRING=-O3 -DNDEBUG {march_flag}",
                f"-DCMAKE_C_FLAGS_RELEASE:STRING=-O3 -DNDEBUG {march_flag}",
                ".",
            )
            make("-B")

        copy_so_files(join_path(self.build_directory, "lib"), hwcaps_dir)
