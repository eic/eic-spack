# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright (C) 2026 G4OCCT Contributors

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class G4occt(CMakePackage):
    """Geant4 interface to OpenCASCADE Technology (OCCT)."""

    homepage = "https://github.com/eic/G4OCCT"
    url = "https://github.com/eic/G4OCCT/archive/refs/tags/v0.3.0.tar.gz"
    git = "https://github.com/eic/G4OCCT.git"

    maintainers("wdconinc")

    tags = ["eic"]

    version("main", branch="main")
    version("0.3.0", sha256="5c0d201449d7b35300269284af5c8ae54a5dea6357ad1dbf152a01f424f1d07d")
    version("0.2.1", sha256="cd2d178fa2cab8150b4239df7022f9766b492b23e36c5f8c60b3d28fa7b57987")
    version("0.2.0", sha256="c6e16221128cad2338fd2e0f09100f9e133d0657a02528ce7f1f39d9f79a33bd")
    version("0.1.0", sha256="eed942c96927461921b76129316d8439909b325b4c2dff84836dcd5474007606")

    variant("tests", default=False, description="Build test suite")
    variant("benchmarks", default=False, description="Build benchmark suite")
    variant("dd4hep", default=False, description="Build DD4hep plugin")

    depends_on("cmake@3.16:", type="build")
    depends_on("geant4@11.3:")
    depends_on("opencascade@7.8:")
    depends_on("dd4hep", when="+dd4hep")

    def cmake_args(self):
        return [
            self.define_from_variant("BUILD_TESTING", "tests"),
            self.define_from_variant("BUILD_BENCHMARKS", "benchmarks"),
            self.define_from_variant("BUILD_DD4HEP_PLUGIN", "dd4hep"),
        ]
