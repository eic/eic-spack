# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Simsipm(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    url = "https://github.com/EdoPro98/SimSiPM/archive/refs/tags/v2.0.2.tar.gz"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("2.0.2", sha256="ba60ed88b54b1b29d089f583dbce93b3272b0b13d47772941339f1503ee3fa48")

    variant("python", default=True, description="Compile python bindings for SiPM simulation library")

    depends_on("cmake@3.9:", type="build")

    depends_on("py-pybind11")

    depends_on("py-pytest", type="test")
    depends_on("googletest", type="test")

    def cmake_args(self):
        args = [
            self.define_from_variant("SIPM_BUILD_PYTHON", "python"),
            self.define("SIPM_ENABLE_TEST", self.run_tests),
        ]
        return args
