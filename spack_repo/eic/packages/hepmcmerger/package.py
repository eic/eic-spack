# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

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
    version("2.2.0", sha256="ae513c0653afed35c1ec1cb4e209b0dd990b7c658732829168404475bac41c8c")
    version("2.1.0", sha256="fbff886e503fd7ccd1258857b69c9bcc4a8ee55dd3d9c345b53416d9a9708c6e")
    version("2.0.0", sha256="901dd224aa68c308fc34fc3b859ef9e04cacfd915e5c11cf3a98ad1ec372b5ce")
    version("1.1.1", sha256="c55f2016901feb081c87ad275b99a4e9da0ce476a23c0c1fa15a347ca1018f97")
    version("1.1.0", sha256="69385f36f1d4d9b9c725afc5b40dbf0ba4253e3fccde76f989d84afee72d36b6")
    version("1.0.5", sha256="3660c602212368f04e98a36ced68e4ea3dcc8a23a0cb5047ef27afe07c16bf32")
    version("1.0.4", sha256="0f5e1d6b2d76af764f5cc528ccfad1269047f6e361b6bc0a1b80941388f71437")
    version("1.0.3", sha256="9f245dc46e159f9424383a4337ebbc685973e83240fe178c776e6cca5e9674f0")
    version("1.0.2", sha256="e8bb639545e472f46b7de8f0c6e03c9ee61086c92b8ffcba661f0fe3b1064ad6")
    version("1.0.1", sha256="419732c2d46afbad89e32362d339a643dc1e6e5ff9724c3027a45aef1b8fbf95")
    version("1.0.0", sha256="5f36b0b65f1062aab79dc6653b6f6fecb9682022f1a471efa62b5614c9731618")

    depends_on("c", type="build", when="@:2.0.0")
    depends_on("cxx", type="build")

    depends_on("hepmc3")
    depends_on("root")

    def cmake_args(self):
        args = [
            self.define("CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value),
        ]
        return args
