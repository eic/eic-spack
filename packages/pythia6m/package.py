# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pythia6m(CMakePackage):
    """Pythia6 modified to better describe lepton-nucleon scattering
    at intermediate energies."""

    homepage = "https://gitlab.com/eic/mceg/pythia6m"
    url = "https://gitlab.com/eic/mceg/pythia6m/-/archive/master/pythia6m-master.tar.gz"
    list_url = "https://gitlab.com/eic/mceg/pythia6m/-/tags"
    git = "https://gitlab.com/eic/mceg/pythia6m.git"

    tags = ["eic"]

    version("master", branch="master", submodules=True)

    depends_on("fortran", type="build")
    depends_on("cmake@2.8:", type="build")
    depends_on("root")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value
        )
        return args
