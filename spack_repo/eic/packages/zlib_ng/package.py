# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Overlay of the builtin zlib-ng package that adds an ``hwcaps`` multi-valued
# variant.  When set, additional optimised shared-library builds are placed in
# ``lib/glibc-hwcaps/<level>/`` inside the install prefix.  Any binary whose
# RPATH already points at the prefix ``lib/`` directory gets automatic
# runtime CPU dispatch through the glibc dynamic-linker hwcaps mechanism —
# no changes to the consumer binary are needed.

import re as _re

from spack_repo.builtin.packages.zlib_ng.package import (
    AutotoolsBuilder as _BuiltinAutotoolsBuilder,
    ZlibNg as _BuiltinZlibNg,
)
from spack_repo.eic.packages.hwcaps_support.package import (
    copy_so_files,
    hwcaps_march,
    install_hwcaps_variants,
    valid_hwcaps_values,
)

from spack.package import *


class ZlibNg(_BuiltinZlibNg):
    __doc__ = _BuiltinZlibNg.__doc__

    variant(
        "hwcaps",
        values=("none",) + valid_hwcaps_values(),
        default="none",
        multi=True,
        description=(
            "Build additional optimised shared libraries for the listed glibc hwcaps "
            "levels and install them to lib/glibc-hwcaps/<level>/.  Each level must be "
            "strictly greater than the spec's baseline target in archspec ordering.  "
            "Requires +shared."
        ),
    )

    for _v in valid_hwcaps_values():
        conflicts("~shared", when=f"hwcaps={_v}", msg="hwcaps requires a shared library build")


class AutotoolsBuilder(_BuiltinAutotoolsBuilder):
    """AutotoolsBuilder for zlib-ng with optional glibc hwcaps multi-build."""

    @run_after("install")
    def _install_hwcaps_variants(self):
        install_hwcaps_variants(self, self.build_for_hwcaps)

    def build_for_hwcaps(self, target_name: str, flags: str, hwcaps_dir: str) -> None:
        """Re-build zlib-ng shared libraries with hwcaps optimisation flags.

        Patches the build-system's ``CFLAGS`` in the Makefile to prepend the
        hwcaps march flag (preserving all original compiler defines, include
        paths, and feature flags), runs ``make -B`` to force a full rebuild,
        copies the resulting ``*.so*`` files to *hwcaps_dir*, then restores the
        Makefile to its original state.
        """
        build_dir = self.build_directory
        makefile_path = join_path(build_dir, "Makefile")

        with open(makefile_path) as fh:
            original_content = fh.read()

        pattern = _re.compile(r"^(CFLAGS=)(.*)$", _re.MULTILINE)
        if not pattern.search(original_content):
            raise InstallError("hwcaps: could not locate CFLAGS line in Makefile")
        patched_content = pattern.sub(rf"\g<1>{flags} \g<2>", original_content, count=1)

        try:
            with open(makefile_path, "w") as fh:
                fh.write(patched_content)
            with working_dir(build_dir):
                make("-B")
        finally:
            with open(makefile_path, "w") as fh:
                fh.write(original_content)

        copy_so_files(build_dir, hwcaps_dir)

