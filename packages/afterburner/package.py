# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Afterburner(CMakePackage):
    """An EIC Monte Carlo Afterburner for beam effects."""

    homepage = "https://github.com/eic/afterburner"
    url = "https://github.com/eic/afterburner/archive/refs/tags/v0.1.2.tar.gz"
    list_url = "https://github.com/eic/afterburner/tags"
    git = "https://github.com/eic/afterburner"

    maintainers = ["wdconinc", "DraTeots"]

    tags = ["eic"]

    version("main", branch="main")
    version(
        "0.1.2",
        sha256="4de4d8ce9f76830a1e1a2b4b680a78baa5ed2f28f1aaac4c0e861c48bbff259e",
    )
    version(
        "0.1.1",
        sha256="a29f576e11debeaa2e1a1da87eb51bd58281f7fd547906159e41aefc4635f265",
    )
    version(
        "0.1.0",
        sha256="2a4c083323ba43944ac1b5cae66f5b45205042cff0adb80506feb2b95a075179",
    )
    version(
        "0.0.2",
        sha256="7e4f8e601bdca3691725b3cc22e72409eb85e8a48852bdeed944590864339cb5",
    )
    version(
        "0.0.1",
        sha256="53ac535cc1bfed3dd9d482d942622a472617d4d53771d5cbc9da4feac071b770",
    )

    variant("root", default=False, description="Support reading ROOT files")
    variant("zlib", default=True, description="Support reading compressed files")

    depends_on("cxx", type="build")

    depends_on("gsl")
    depends_on("hepmc3")
    depends_on("clhep")
    depends_on("yaml-cpp")
    depends_on("root", when="+root")
    depends_on("zlib", when="+zlib")

    root_cmakelists_dir = "cpp"

    def patch(self):
        filter_file(
            r"add_subdirectory\(test\)", "#add_subdirectory(test)", "cpp/CMakeLists.txt"
        )
        filter_file(r"enable_testing\(\)", "#enable_testing()", "cpp/CMakeLists.txt")

    def cmake_args(self):
        if "+root" in self.spec:
            cxxstd = self.spec["root"].variants["cxxstd"].value
        else:
            cxxstd = "11"
        args = [self.define("CMAKE_CXX_STANDARD", cxxstd)]
        return args
