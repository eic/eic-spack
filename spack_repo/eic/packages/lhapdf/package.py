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
# We force a rebuild by overriding ``CXXFLAGS`` on the ``make`` command line;
# GNU make's command-line variable override is propagated to the compiler
# invocations that libtool wraps.

import os

from spack_repo.builtin.build_systems import autotools as _autotools
from spack_repo.builtin.packages.lhapdf.package import Lhapdf as _BuiltinLhapdf
from spack_repo.eic.packages.hwcaps_support.package import (
    add_hwcaps_variant,
    copy_so_files,
    hwcaps_march,
    install_hwcaps_variants,
)

from spack.package import *


class Lhapdf(_BuiltinLhapdf):
    __doc__ = _BuiltinLhapdf.__doc__

    add_hwcaps_variant()


class AutotoolsBuilder(_autotools.AutotoolsBuilder):
    """AutotoolsBuilder for lhapdf with optional glibc hwcaps multi-build."""

    @run_after("install")
    def _install_hwcaps_variants(self):
        install_hwcaps_variants(self, self.build_for_hwcaps)

    def build_for_hwcaps(self, target_name: str, march_flag: str, hwcaps_dir: str) -> None:
        """Re-build the LHAPDF shared library with the hwcaps march flag.

        LHAPDF uses libtool, so the compiled shared library ends up in
        ``src/.libs/`` within the (in-source) build tree.  We override
        ``CXXFLAGS`` on the ``make`` command line so that GNU make propagates
        it to every libtool compilation rule, then copy the rebuilt library.
        """
        # Pass flags via make command-line override (highest-priority for GNU make)
        with working_dir(self.build_directory):
            make("-B", f"CXXFLAGS=-O3 {march_flag}", f"CFLAGS=-O3 {march_flag}")

        # libtool places the actual .so in src/.libs/; fall back to top-level
        # .libs/ if the src/ subdir layout is not present.
        src_libs = join_path(self.build_directory, "src", ".libs")
        if not os.path.isdir(src_libs):
            src_libs = join_path(self.build_directory, ".libs")
        copy_so_files(src_libs, hwcaps_dir)
