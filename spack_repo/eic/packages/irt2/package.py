# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Irt2(CMakePackage):
    """Indirect Ray Tracing library for EPIC Cherenkov detector reconstruction."""

    homepage = "https://github.com/eic/irt"
    url = "https://github.com/eic/irt/archive/refs/tags/v2.1.0.zip"
    list_url = "https://github.com/eic/irt/tags"
    git = "https://github.com/eic/irt.git"

    maintainers = ["chchatte92", "veprbl"]
    tags = ["eic"]

    version("2.1.2", sha256="93232b2c40f574410c4c3045c997c0f9c572280b6cfe2e30af589f36ea82106e")
    version("2.1.1", sha256="214ab5918b9fcf4a3bebc3f8fa5e06c0d0dc77ff7d2233d771c83967af5a634d")
    version("2.1.0", sha256="906a0cf7ec111bbf7e3f95d48daa8be6f0de592ffde2222aeec53f371abc2cb7")

    variant("root_io", default=False, description="Build dictionaries for ROOT IO")

    depends_on("cxx", type="build")

    depends_on("root@6: +root7")

    def cmake_args(self):
        args = [
            "-DEVALUATION=OFF",
            "-DDELPHES=OFF",
        ]
        args.append(self.define_from_variant("IRT_ROOT_IO", "root_io"))
        return args
