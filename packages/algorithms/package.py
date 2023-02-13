# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Algorithms(CMakePackage):
    """Collection of Reconstruction Algorithms using DD4hep and EDM4hep."""

    homepage = "https://eic.github.io/algorithms"
    url = "https://github.com/eic/algorithms"
    git = "https://github.com/eic/algorithms.git"

    maintainers = ["wdconinc", "sly2j"]

    version("master", branch="master")

    depends_on("edm4hep")
    depends_on("edm4eic")
    depends_on("dd4hep +dddetectors +dddigi +ddrec")
