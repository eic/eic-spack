# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Hepmcmerger(CMakePackage):
    """An EIC HepMC merger to combine signal and background events."""

    homepage = "https://github.com/eic/HEPMC_Merger"
    url = "https://github.com/eic/HEPMC_Merger/archive/refs/tags/v1.0.4.tar.gz"
    list_url = "https://github.com/eic/HEPMC_Merger/tags"
    git = "https://github.com/eic/HEPMC_Merger.git"

    maintainers("kkauder")

    tags = ["eic"]

    version("main", branch="main")
    version("1.0.4", sha256="0f5e1d6b2d76af764f5cc528ccfad1269047f6e361b6bc0a1b80941388f71437")
    version("1.0.3", sha256="9f245dc46e159f9424383a4337ebbc685973e83240fe178c776e6cca5e9674f0")
    version("1.0.2", sha256="e8bb639545e472f46b7de8f0c6e03c9ee61086c92b8ffcba661f0fe3b1064ad6")
    version("1.0.1", sha256="419732c2d46afbad89e32362d339a643dc1e6e5ff9724c3027a45aef1b8fbf95")
    version("1.0.0", sha256="5f36b0b65f1062aab79dc6653b6f6fecb9682022f1a471efa62b5614c9731618")

    depends_on("hepmc3")
    depends_on("root")

    def cmake_args(self):
        args = [
            self.define("CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value),
        ]
        return args
