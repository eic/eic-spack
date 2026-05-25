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
# across several subdirectories of the build tree (src/, plugins/SISCone/…);
# the default HwcapsCMakeMixin uses a recursive copy to collect them all.
# The Autotools build places libraries in the source tree's ``src/.libs/`` —
# handled by the default HwcapsAutotoolsMixin recursive copy.

from spack_repo.builtin.build_systems import autotools as _autotools
from spack_repo.builtin.build_systems import cmake as _cmake
from spack_repo.builtin.packages.fastjet.package import Fastjet as _BuiltinFastjet
from spack_repo.eic.build_systems.hwcaps import (
    HwcapsAutotoolsMixin,
    HwcapsCMakeMixin,
    add_hwcaps_variant,
)

# The eic fork of spack-packages adds explicit CMakeBuilder and AutotoolsBuilder
# to the builtin fastjet package; the upstream spack-packages does not.  Fall
# back to the base build-system builders when the imports are unavailable so
# that this overlay works with both.
try:
    from spack_repo.builtin.packages.fastjet.package import CMakeBuilder as _BuiltinCMakeBuilder
except ImportError:
    _BuiltinCMakeBuilder = _cmake.CMakeBuilder

try:
    from spack_repo.builtin.packages.fastjet.package import (
        AutotoolsBuilder as _BuiltinAutotoolsBuilder,
    )
except ImportError:
    _BuiltinAutotoolsBuilder = _autotools.AutotoolsBuilder

from spack.package import *


class Fastjet(_BuiltinFastjet):
    __doc__ = _BuiltinFastjet.__doc__

    add_hwcaps_variant()


class CMakeBuilder(HwcapsCMakeMixin, _BuiltinCMakeBuilder):
    """CMakeBuilder for fastjet with optional glibc hwcaps multi-build."""


class AutotoolsBuilder(HwcapsAutotoolsMixin, _BuiltinAutotoolsBuilder):
    """AutotoolsBuilder for fastjet with optional glibc hwcaps multi-build."""
