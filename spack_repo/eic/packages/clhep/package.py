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

    test_requires_compiler = True

    def test_three_vector(self):
        """compile and run a program that uses CLHEP::Hep3Vector"""
        cxx = Executable(self.spec["cxx"].package.cxx)
        src = join_path(self.test_suite.current_test_data_dir, "test_clhep.cpp")
        libs = find_libraries("libCLHEP", root=self.prefix, shared=True, recursive=True)
        cxx(
            "-std=c++17",
            src,
            "-o",
            "test_clhep",
            f"-I{self.prefix.include}",
            *libs.ld_flags.split(),
            *[f"-Wl,-rpath,{d}" for d in libs.directories],
        )
        out = Executable("./test_clhep")(output=str)
        assert "magnitude: 13" in out, out
