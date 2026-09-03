# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Eiccontent(CMakePackage):
    """Pandora algorithms and tools for Electron-Ion Collider event reconstruction."""

    url = "https://github.com/eic/lccontent/archive/v03-01-05.tar.gz"
    homepage = "https://github.com/eic/lccontent"
    git = "https://github.com/eic/lccontent.git"

    tags = ["eic"]

    maintainers("wdconinc")

    version("eic", branch="eic")

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
                self.spec['root'].variants['cxxstd'].value if 'root' in self.spec else 20
            ),
            self.define_from_variant("PANDORA_MONITORING", "monitoring"),
        ]
        return args

    def url_for_version(self, version):
        # contrary to ilcsoftpackages, here the patch version is kept when 0
        base_url = self.url[: self.url.rfind("/")]

        if version.isdevelop():
            return f"{base_url}/refs/heads/{version}.tar.gz"

        major = str(version[0]).zfill(2)
        minor = str(version[1]).zfill(2)
        patch = str(version[2]).zfill(2)
        url = base_url + "/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url
