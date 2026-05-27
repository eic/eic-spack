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
# Both the CMake and Makefile build systems are supported: the appropriate mixin
# is activated via the inner builder classes below.

from spack_repo.builtin.packages.lz4.package import CMakeBuilder as _BuiltinCMakeBuilder
from spack_repo.builtin.packages.lz4.package import Lz4 as _BuiltinLz4
from spack_repo.builtin.packages.lz4.package import MakefileBuilder as _BuiltinMakefileBuilder
from spack_repo.eic.build_systems.hwcaps import (
    HwcapsCMakeMixin,
    HwcapsMakefileMixin,
    add_hwcaps_variant,
)

from spack.package import *


class Lz4(_BuiltinLz4):
    __doc__ = _BuiltinLz4.__doc__

    #: Extra args for ``make -B`` during hwcaps rebuilds (Makefile build only);
    #: targets only the ``lib/`` subdirectory to skip tools and test binaries.
    hwcaps_make_args = ["-C", "lib"]
    #: Subdirectory where rebuilt ``*.so*`` files land (Makefile build only).
    hwcaps_lib_subdir = "lib"

    add_hwcaps_variant(conflicts="libs=static")


class CMakeBuilder(HwcapsCMakeMixin, _BuiltinCMakeBuilder):
    """CMake builder for lz4 with optional glibc hwcaps multi-build.

    Inherits ``root_cmakelists_dir = build/cmake/`` from the builtin so that
    cmake finds ``CMakeLists.txt`` in the right subdirectory, and adds hwcaps
    rebuild support via :class:`~spack_repo.eic.build_systems.hwcaps.HwcapsCMakeMixin`.
    """


class MakefileBuilder(HwcapsMakefileMixin, _BuiltinMakefileBuilder):
    """Makefile builder for lz4 with optional glibc hwcaps multi-build.

    Inherits the standard in-source Makefile build from the builtin and adds
    hwcaps rebuild support via
    :class:`~spack_repo.eic.build_systems.hwcaps.HwcapsMakefileMixin`.
    """
