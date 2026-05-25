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

import os

from spack_repo.builtin.packages.lz4.package import Lz4 as _BuiltinLz4
from spack_repo.builtin.packages.lz4.package import MakefileBuilder as _BuiltinMakefileBuilder
from spack_repo.eic.build_systems.hwcaps import (
    HwcapsMixin,
    add_hwcaps_variant,
    copy_so_files,
    valid_hwcaps_values,
)

from spack.package import *


class Lz4(_BuiltinLz4):
    __doc__ = _BuiltinLz4.__doc__

    add_hwcaps_variant(
        "Build additional optimised shared libraries for the listed glibc hwcaps "
        "levels and install them to lib/glibc-hwcaps/<level>/.  Each level must be "
        "strictly greater than the spec's baseline target in archspec ordering.  "
        "Requires libs=shared."
    )

    for _v in valid_hwcaps_values():
        conflicts(
            "libs=static",
            when=f"hwcaps={_v}",
            msg="hwcaps requires a shared library build (libs=shared)",
        )


class MakefileBuilder(HwcapsMixin, _BuiltinMakefileBuilder):
    """MakefileBuilder for lz4 with optional glibc hwcaps multi-build."""

    def build_for_hwcaps(self, target_name: str, march_flag: str, hwcaps_dir: str) -> None:
        """Re-build lz4 shared library with the hwcaps march flag and copy to hwcaps_dir.

        lz4's lib/Makefile uses ``CFLAGS = $(DEBUGFLAGS) $(USERCFLAGS)`` where
        ``USERCFLAGS`` expands from the ``CFLAGS`` environment variable.  We
        temporarily override ``CFLAGS`` in the environment so that the
        compiler wrapper's ``SPACK_TARGET_ARGS`` (which prepends the baseline
        -march) is overridden by our hwcaps march flag (which appears later on
        the command line — GCC applies the last -march flag).
        """
        pic = self.pkg.compiler.cc_pic_flag
        # Add -O3 because lz4's Makefile prepends -O3 to USERCFLAGS anyway.
        new_cflags = f"{pic} -O3 {march_flag}"

        old_cflags = os.environ.get("CFLAGS")
        os.environ["CFLAGS"] = new_cflags
        try:
            with working_dir(self.build_directory):
                make("-B", "-C", "lib")
        finally:
            if old_cflags is not None:
                os.environ["CFLAGS"] = old_cflags
            else:
                os.environ.pop("CFLAGS", None)

        copy_so_files(join_path(self.build_directory, "lib"), hwcaps_dir)
