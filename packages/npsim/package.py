# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Npsim(CMakePackage):
    """DD4hep-based simulation plugins, front-end, and related utilities."""

    homepage = "https://github.com/eic/npsim"
    url = "https://github.com/eic/npsim/archive/refs/tags/v1.0.0.zip"
    git = "https://github.com/eic/npsim.git"
    list_url = "https://github.com/eic/npsim/tags"

    maintainers = ["wdconinc"]

    version("main", branch="main")
    version("1.4.3", sha256="4d636863d02d70897ddf036b4003e47f7e0c85125268f92f880c98e25bd38ce4")
    version("1.4.2", sha256="7cd83a6cceea42c9a74cbb10fbd069b658c1bb263fce507d42e62570f5c040cf")
    version("1.4.1", sha256="74d1c2c8fb8e8a05d9daaf228214f2054e3147f30ec13581e99f7549df8d4be3") 
    version("1.4.0", sha256="77c40277c3439b191e5f7508263b4b0a73c05bda00c8c1408065a2e4479de688")
    version(
        "1.3.0",
        sha256="6870ca80c6255d1a35b0d05c70e86c7f252e8401dfb53759cbec8a93c5d74794",
    )
    version(
        "1.2.0",
        sha256="2a7e039dfcf8ed4c8a22fc9cb00bf73859537b3ee83a5bb128cc1ef451763865",
    )
    version(
        "1.1.1",
        sha256="d1a34efd22832f0da863e5712d342153ca63520acccf9516b47ff3cb2ed4e935",
    )
    version(
        "1.1.0",
        sha256="0ca9a88560eae22ecce3ffee4cdb38ee21bea8fa7330fded8f896b93679bf5a3",
    )
    version(
        "1.0.0",
        sha256="eccfb93ad47a3788c0d03a522c640e4510b3a3cba2771e92b136a246b7211f50",
    )

    variant("http", default=False, description="Build web display services")
    variant("geocad", default=False, description="Build the geocad interface")

    depends_on("cxx", type="build")

    depends_on("fmt +shared")
    depends_on("root")
    depends_on("py-pyyaml", type="build")
    depends_on("py-jinja2", type="build")
    depends_on("spdlog")
    depends_on("root +http", when="+http")
    depends_on("dd4hep +ddg4")
    depends_on("dd4hep@1.18:")
    depends_on("opencascade", when="+geocad")
    depends_on("py-six")

    def cmake_args(self):
        args = [self.define_from_variant("USE_GEOCAD", "geocad")]
        args.append("-DCMAKE_CXX_STANDARD=17")
        return args
