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
# ``lib/`` within the cmake build directory.  The default HwcapsCMakeMixin
# behaviour (inject march flag via SPACK_CXXFLAGS/SPACK_CFLAGS + ``make -B``
# + recursive copy) is sufficient — no cmake re-configure is needed for a
# pure ``-march=`` change.

from spack_repo.builtin.packages.clhep.package import Clhep as _BuiltinClhep
from spack_repo.eic.build_systems.hwcaps import HwcapsCMakeMixin, add_hwcaps_variant

from spack.package import *


class Clhep(_BuiltinClhep, HwcapsCMakeMixin):
    __doc__ = _BuiltinClhep.__doc__

    add_hwcaps_variant()
