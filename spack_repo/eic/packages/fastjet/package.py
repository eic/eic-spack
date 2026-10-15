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
# FastJet uses Autotools; the build places shared libraries under
# ``src/.libs/`` in the source tree.  The default HwcapsAutotoolsMixin
# recursive copy collects them all.

from spack_repo.builtin.packages.fastjet.package import Fastjet as _BuiltinFastjet
from spack_repo.eic.build_systems.hwcaps import HwcapsAutotoolsMixin, add_hwcaps_variant

from spack.package import *


class Fastjet(_BuiltinFastjet, HwcapsAutotoolsMixin):
    __doc__ = _BuiltinFastjet.__doc__

    add_hwcaps_variant()
