# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.build_systems.cmake import CMakePackage
except ImportError:
    from spack.build_systems.cmake import CMakePackage


class Algorithms(CMakePackage):
    """Collection of Reconstruction Algorithms using DD4hep and EDM4hep."""

    homepage = "https://eic.github.io/algorithms"
    url = "https://github.com/eic/algorithms/archive/refs/tags/v1.1.0.tar.gz"
    git = "https://github.com/eic/algorithms.git"

    maintainers = ["wdconinc", "sly2j"]

    version("main", branch="main")
    version("master", branch="master", deprecated=True)
    version("1.2.0", sha256="893da7948baf9aa778b1716b3ce7331cd14befa7e43f3cce810c6b49235c73fd")
    version("1.1.0", sha256="f7fef07ee4217b1d224bbe3f87e21e155e1e205356ad5a19b7d09558e7c5c024", deprecated=True)  # exposes log() function
    version("1.0.0", sha256="b36598ba539938c0f8e5d75170f770e5701a1ad81dbee929ccc36df15233a99d")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("dd4hep +ddrec")
    depends_on("edm4hep")
    depends_on("edm4eic")
    depends_on("cppgsl")
    depends_on("fmt")
