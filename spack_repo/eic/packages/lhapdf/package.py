# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Overlay of the builtin lhapdf package that adds an ``hwcaps`` multi-valued
# variant.  When set, additional optimised shared-library builds are placed in
# ``lib/glibc-hwcaps/<level>/`` inside the install prefix.  Any binary whose
# RPATH already points at the prefix ``lib/`` directory gets automatic
# runtime CPU dispatch through the glibc dynamic-linker hwcaps mechanism —
# no changes to the consumer binary are needed.
#
# LHAPDF uses a GNU Autotools / libtool build.  The shared library is built
# in a ``src/.libs/`` subdirectory within the source tree (in-source build).
# The default HwcapsAutotoolsMixin behaviour (CXXFLAGS/CFLAGS override on the
# make command line + ``make -B`` + recursive copy) is sufficient; the
# recursive copy finds the rebuilt libraries in ``src/.libs/`` automatically.

from spack_repo.builtin.build_systems import autotools as _autotools
from spack_repo.builtin.packages.lhapdf.package import Lhapdf as _BuiltinLhapdf
from spack_repo.eic.build_systems.hwcaps import HwcapsAutotoolsMixin, add_hwcaps_variant

from spack.package import *


class Lhapdf(_BuiltinLhapdf):
    __doc__ = _BuiltinLhapdf.__doc__

    add_hwcaps_variant()


class AutotoolsBuilder(HwcapsAutotoolsMixin, _autotools.AutotoolsBuilder):
    """AutotoolsBuilder for lhapdf with optional glibc hwcaps multi-build."""
