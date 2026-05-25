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
# the target.  The package class defines ``hwcaps_cmake_extra_args()`` to
# return the ``-DVECGEOM_VECTOR=...`` argument; the ``HwcapsCMakeMixin`` injects
# the ``-march=`` flag via SPACK_CXXFLAGS/SPACK_CFLAGS and calls cmake only for
# the VECGEOM_VECTOR update.

from spack_repo.builtin.packages.vecgeom.package import Vecgeom as _BuiltinVecgeom
from spack_repo.eic.build_systems.hwcaps import HwcapsCMakeMixin, add_hwcaps_variant

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


class Vecgeom(HwcapsCMakeMixin, _BuiltinVecgeom):
    __doc__ = _BuiltinVecgeom.__doc__

    add_hwcaps_variant()

    def hwcaps_cmake_extra_args(self, target_name: str) -> list:
        """Return cmake args for a VecGeom hwcaps rebuild at *target_name*.

        Updates only ``VECGEOM_VECTOR``; the ``-march=`` flag is handled by the
        ``HwcapsCMakeMixin`` via ``SPACK_CXXFLAGS``/``SPACK_CFLAGS`` injection.
        """
        return [f"-DVECGEOM_VECTOR:STRING={_vecgeom_vector_for_target(target_name)}"]
