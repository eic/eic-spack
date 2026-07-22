# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Timeframebuilder(CMakePackage):
    """A Timeframe Builder to combine signal and background events."""

    homepage = "https://github.com/eic/TimeframeBuilder"
    url = "https://github.com/eic/TimeframeBuilder/archive/refs/tags/v0.9.1.tar.gz"
    list_url = "https://github.com/eic/TimeframeBuilder/tags"
    git = "https://github.com/eic/TimeframeBuilder.git"

    maintainers("simonge")

    tags = ["eic"]

    version("main", branch="main")
    version("0.9.1", sha256="dc6d35d898456307686aaf29ac62976e5dfd04a4ba38429a0d6461d4703ed39e")
    version("0.9.0", sha256="9726690f74b32af37e598fbc23701f2bc14c30f4b877544ffc4c08648588ca52")
            

    depends_on("cxx", type="build")

    depends_on("hepmc3 +rootio")
    depends_on("edm4hep")
    depends_on("podio")
    depends_on("root")
    depends_on("yaml-cpp")

    def cmake_args(self):
        args = [
            self.define("TIMEFRAME_BUILDER_VERSION_FULL", self.version),
            self.define("CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value),
        ]
        return args
