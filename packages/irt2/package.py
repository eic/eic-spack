# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Irt2(CMakePackage):
    """Indirect Ray Tracing library for EPIC Cherenkov detector reconstruction."""

    homepage = "https://github.com/eic/irt"
    url = "https://github.com/eic/irt/archive/refs/tags/v2.1.0.zip"
    list_url = "https://github.com/eic/irt/tags"
    git = "https://github.com/eic/irt.git"

    maintainers = ["chchatte92", "veprbl"]
    tags = ["eic"]

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
