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

    test_requires_compiler = True

    def test_cluster(self):
        """compile and run a program that clusters three particles with anti-kt"""
        fastjet_config = which("fastjet-config", path=self.prefix.bin, required=True)
        flags = fastjet_config("--cxxflags", "--libs", output=str).split()
        cxx = Executable(self.spec["cxx"].package.cxx)
        src = join_path(self.test_suite.current_test_data_dir, "test_fastjet.cpp")
        cxx("-std=c++17", src, "-o", "test_fastjet", *flags, f"-Wl,-rpath,{self.prefix.lib}")
        out = Executable("./test_fastjet")(output=str)
        assert "jets: 2" in out, out
        assert "jet 0: pt 103" in out and "jet 1: pt 99" in out, out
