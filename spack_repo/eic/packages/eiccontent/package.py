# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Eiccontent(CMakePackage):
    """Pandora algorithms and tools for Electron-Ion Collider event reconstruction."""

    url = "https://github.com/eic/LCContent/archive/refs/tags/v3.2.0.tar.gz"
    homepage = "https://github.com/eic/LCContent"
    git = "https://github.com/eic/LCContent.git"

    tags = ["eic"]

    maintainers("wdconinc")

    version("3.2.0", sha256="8bdcd08eca91d0cfdf6f62039305e8f536eb5194a927f262c889360aa5b0c430")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("pandorapfa")
    depends_on("pandorasdk")

    depends_on("pandoramonitoring", when="+monitoring")

    variant("monitoring", default=False, description="Enable Pandora Monitoring")

    def setup_build_environment(self, env):
        env.append_flags("CXXFLAGS", "-Wno-error")

    def cmake_args(self):
        args = [
            self.define("CMAKE_MODULE_PATH", self.spec["pandorapfa"].prefix.cmakemodules),
            self.define(
                "CMAKE_CXX_STANDARD",
                self.spec["root"].variants["cxxstd"].value if "root" in self.spec else 20,
            ),
            self.define_from_variant("PANDORA_MONITORING", "monitoring"),
        ]
        return args
