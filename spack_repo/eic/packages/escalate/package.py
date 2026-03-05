# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack_repo.builtin.build_systems.bundle import BundlePackage


class Escalate(BundlePackage):
    """EIC Escalate environment."""

    homepage = "https://gitlab.com/eic/escalate"

    maintainer = ["wdconinc"]

    tags = ["eic"]

    version("develop", preferred=True)

    depends_on("cxx", type="build")

    # Dev
    depends_on("cmake")
    depends_on("boost")
    depends_on("python")
    # HENP
    depends_on("root@6.20.00: -vmc +pythia6 +pythia8 +root7 cxxstd=17")
    depends_on("geant4 +opengl +python +qt cxxstd=17")
    depends_on("clhep cxxstd=17")
    depends_on("eigen")
    depends_on("vgm")
    depends_on("genfit")
    depends_on("hepmc")
    depends_on("hepmc3 +interfaces +python +rootio")
    depends_on(
        "acts +examples+digitization+json+dd4hep+fatras+geant4+hepmc3"
    )
    depends_on("delphes")
    depends_on("fastjet")
    # MCEG
    depends_on("lhapdf")
    depends_on("pythia8")
    depends_on("cernlib")
    depends_on("lhapdf5")
    depends_on("pythia6 +root")
    # EIC
    depends_on("eic-smear +pythia6")
    depends_on("ejana +acts +genfit")
    depends_on("g4e")
    depends_on("jana2 +root")
    # Jupyter
    depends_on("py-jupyterlab")
