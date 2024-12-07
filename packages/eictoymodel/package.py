# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Eictoymodel(CMakePackage):
    """EicToyModel (ETM) is a C++ ROOT-based software suite
    for EIC Central Detector configuration purposes."""

    homepage = "https://github.com/eic/EicToyModel"
    url = "https://github.com/eic/EicToyModel/archive/v1.0.0.tar.gz"
    list_url = "https://github.com/eic/EicToyModel/releases"
    git = "https://github.com/eic/EicToyModel.git"

    maintainer = ["wdconinc"]

    tags = ["eic"]

    version("master", branch="master")
    version(
        "1.0.0",
        sha256="633b3566c7c24af970a0ccb2487207a9f9b43ab84404ccead95ffd30f21a8b94",
    )

    depends_on("cxx", type="build")

    depends_on("opencascade")
    depends_on("root")
    depends_on("vgm")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value
        )
        args.append("-DOPENCASCADE=%s" % self.spec["opencascade"].prefix)
        return args
