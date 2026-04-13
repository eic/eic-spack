# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright (C) 2026 G4OCCT Contributors

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class G4occt(CMakePackage):
    """Geant4 interface to OpenCASCADE Technology (OCCT)."""

    homepage = "https://github.com/eic/G4OCCT"
    git = "https://github.com/eic/G4OCCT.git"

    maintainers("wdconinc")

    version("main", branch="main")

    variant("tests", default=False, description="Build test suite")
    variant("benchmarks", default=False, description="Build benchmark suite")

    depends_on("cmake@3.16:", type="build")
    depends_on("geant4@11.3:")
    depends_on("opencascade@7.8:")

    def cmake_args(self):
        return [
            self.define_from_variant("BUILD_TESTING", "tests"),
            self.define_from_variant("BUILD_BENCHMARKS", "benchmarks"),
        ]
