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
    version("1.1", sha256="b71279829d88f690118725bbfcf378fccb6d0f79ba8a595932617a3c1e8b79aa")
    version("1.0", sha256="f981f84be6fe9bf6ae7420fecc16e5c7ac6905ad9f18c789f5c0ef1beec0cb46")

    depends_on("cxx", type="build")
    depends_on("cmake@3.20:", type="build")

    depends_on("root")
    depends_on("hepmc3 +rootio")
    depends_on("pythia8")
    depends_on("fastjet")

    root_cmakelists_dir = "Pythia8"
