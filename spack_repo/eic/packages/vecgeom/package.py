# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Overlay of the builtin vecgeom package that adds an ``hwcaps`` multi-valued
# variant.  When set, additional optimised shared-library builds are placed in
# ``lib/glibc-hwcaps/<level>/`` inside the install prefix.  Any binary whose
# RPATH already points at the prefix ``lib/`` directory gets automatic
# runtime CPU dispatch through the glibc dynamic-linker hwcaps mechanism —
# no changes to the consumer binary are needed.
#
# VecGeom uses CMake and its performance depends critically on the
# ``VECGEOM_VECTOR`` backend selection, which controls explicit SIMD
# intrinsics.  For an x86_64_v3 hwcaps build we set VECGEOM_VECTOR=avx2 in
# addition to passing ``-march=x86-64-v3``.  The correct VECGEOM_VECTOR value
# for each hwcaps target is derived by inspecting the archspec feature set of
# the target.

from spack_repo.builtin.build_systems import cmake as _cmake
from spack_repo.builtin.packages.vecgeom.package import Vecgeom as _BuiltinVecgeom
from spack_repo.eic.packages.hwcaps_support.package import (
    add_hwcaps_variant,
    copy_so_files_recursive,
    install_hwcaps_variants,
)

import spack.vendor.archspec.cpu as _cpu

from spack.package import *

#: Ordered list of SIMD instruction sets that VecGeom knows about (lowest first).
_VECGEOM_ARCH = "sse2 sse3 ssse3 sse4.1 sse4.2 avx avx2".split()


def _vecgeom_vector_for_target(target_name: str) -> str:
    """Return the best VECGEOM_VECTOR value for *target_name*.

    Mirrors the logic in the builtin VecGeom cmake_args(): iterates the
    supported SIMD levels in descending order and returns the first one that
    the archspec target supports.  Falls back to ``empty`` if none match.
    """
    try:
        target = _cpu.TARGETS[target_name]
    except KeyError:
        return "empty"
    for feature in reversed(_VECGEOM_ARCH):
        if feature.replace(".", "_") in target:
            return feature
    return "empty"


class Vecgeom(_BuiltinVecgeom):
    __doc__ = _BuiltinVecgeom.__doc__

    add_hwcaps_variant()


class CMakeBuilder(_cmake.CMakeBuilder):
    """CMakeBuilder for vecgeom with optional glibc hwcaps multi-build."""

    @run_after("install")
    def _install_hwcaps_variants(self):
        install_hwcaps_variants(self, self.build_for_hwcaps)

    def build_for_hwcaps(self, target_name: str, march_flag: str, hwcaps_dir: str) -> None:
        """Re-build VecGeom shared libraries with the hwcaps march flag.

        VecGeom's performance also depends on the VECGEOM_VECTOR backend, so
        we update that cache entry along with the C/C++ Release flags.
        Shared libraries are scattered under the cmake build tree (not in a
        top-level ``lib/`` subdir), so we use a recursive search.
        """
        vecgeom_vector = _vecgeom_vector_for_target(target_name)
        with working_dir(self.build_directory):
            cmake(
                f"-DCMAKE_CXX_FLAGS_RELEASE:STRING=-O3 -DNDEBUG {march_flag}",
                f"-DCMAKE_C_FLAGS_RELEASE:STRING=-O3 -DNDEBUG {march_flag}",
                f"-DVECGEOM_VECTOR:STRING={vecgeom_vector}",
                ".",
            )
            make("-B")

        copy_so_files_recursive(self.build_directory, hwcaps_dir)
