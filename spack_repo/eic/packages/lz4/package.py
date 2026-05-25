# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Overlay of the builtin lz4 package that adds an ``hwcaps`` multi-valued
# variant.  When set, additional optimised shared-library builds are placed in
# ``lib/glibc-hwcaps/<level>/`` inside the install prefix.  Any binary whose
# RPATH already points at the prefix ``lib/`` directory gets automatic
# runtime CPU dispatch through the glibc dynamic-linker hwcaps mechanism —
# no changes to the consumer binary are needed.
#
# lz4 is an ideal showcase for the hwcaps approach: unlike zlib-ng (which
# performs its own runtime SIMD dispatch), lz4 relies on the compiler's
# auto-vectoriser.  Compiling with ``-march=x86-64-v3`` therefore enables
# AVX2 auto-vectorised code paths in the hot compression/decompression loops,
# producing a measurably different (and faster) binary than the baseline.
# The package-level attributes ``hwcaps_make_args`` and ``hwcaps_lib_subdir``
# configure the ``HwcapsMakefileMixin`` to target only the ``lib/`` subdirectory.

from spack_repo.builtin.packages.lz4.package import Lz4 as _BuiltinLz4
from spack_repo.eic.build_systems.hwcaps import HwcapsMakefileMixin, add_hwcaps_variant

from spack.package import *


class Lz4(HwcapsMakefileMixin, _BuiltinLz4):
    __doc__ = _BuiltinLz4.__doc__

    #: Extra args for ``make -B`` during hwcaps rebuilds; targets only the lib
    #: subdirectory so we don't rebuild the tools and test binaries.
    hwcaps_make_args = ["-C", "lib"]
    #: Subdirectory of the build tree where rebuilt ``*.so*`` files land.
    hwcaps_lib_subdir = "lib"

    add_hwcaps_variant(conflicts="libs=static")
