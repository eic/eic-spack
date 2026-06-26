# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Eicsimubeameffects(CMakePackage):
    """EIC beam effects simulation studies and utilities."""

    homepage = "https://github.com/eic/eicSimuBeamEffects"
    url = (
        "https://github.com/eic/eicSimuBeamEffects/archive/refs/tags/production_2021-09-27.tar.gz"
    )
    list_url = "https://github.com/eic/eicSimuBeamEffects/tags"
    git = "https://github.com/eic/eicSimuBeamEffects.git"

    maintainers = ["rahmans1"]

    tags = ["eic"]

    version("master", branch="master")
    version(
        "2021-09-27", sha256="445a637ecc5ad35d4d0b60a7049abf8e66c3c2d6f6778accd5094ed1e092f9be"
    )
    version(
        "2021-08-06", sha256="cadcfa748dea80ec12c5388aa98e74780aaab79051743f2302d62d681eee859a"
    )
    version(
        "production_2021-09-27",
        sha256="445a637ecc5ad35d4d0b60a7049abf8e66c3c2d6f6778accd5094ed1e092f9be",
        deprecated=True,
    )

    depends_on("cxx", type="build")
    depends_on("cmake@3.20:", type="build")

    depends_on("root")
    depends_on("hepmc3 +rootio")
    depends_on("pythia8")
    depends_on("fastjet")

    root_cmakelists_dir = "Pythia8"
