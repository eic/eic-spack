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
