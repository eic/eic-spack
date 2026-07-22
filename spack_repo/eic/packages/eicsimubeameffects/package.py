# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Eicsimubeameffects(CMakePackage):
    """EIC beam effects simulation studies and utilities."""

    homepage = "https://github.com/eic/eicSimuBeamEffects"
    url = "https://github.com/eic/eicSimuBeamEffects/archive/refs/tags/v1.0.tar.gz"
    list_url = "https://github.com/eic/eicSimuBeamEffects/tags"
    git = "https://github.com/eic/eicSimuBeamEffects.git"

    maintainers = ["rahmans1"]

    tags = ["eic"]

    version("master", branch="master")
    version("1.0", sha256="0000000000000000000000000000000000000000000000000000000000000000")

    depends_on("cxx", type="build")
    depends_on("cmake@3.20:", type="build")

    depends_on("root")
    depends_on("hepmc3 +rootio")
    depends_on("pythia8")
    depends_on("fastjet")

    root_cmakelists_dir = "Pythia8"
