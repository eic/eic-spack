# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


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
        "acts +examples+digitization+json+identification+dd4hep+fatras+geant4+hepmc3"
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

    version("1.1.0")
    # Dev
    depends_on("cmake@3.17.0", when="@1.1.0")
    depends_on("boost@1.70.0", when="@1.1.0")
    depends_on("python@3.7.5", when="@1.1.0")
    # HENP
    depends_on("root@6.20.04 -vmc +pythia6 +pythia8 +root7 cxxstd=17", when="@1.1.0")
    depends_on("geant4@10.6.1 +opengl +qt cxxstd=17", when="@1.1.0")
    depends_on("eigen@3.3.7", when="@1.1.0")
    # FIXME geant4@10.6.1 depends_on clhep@2.4.1.3
    # depends_on('clhep@2.3.2.2', when='@1.1.0')
    depends_on("vgm@4-5", when="@1.1.0")
    depends_on("genfit@2020-06-03", when="@1.1.0")
    depends_on("hepmc@2.06.09", when="@1.1.0")
    depends_on("hepmc3@3.2.1 +interfaces +python +rootio", when="@1.1.0")
    depends_on("acts@0.22.1", when="@1.1.0")
    depends_on("delphes@3.4.2", when="@1.1.0")
    depends_on("fastjet@3.3.3", when="@1.1.0")
    # MCEG
    depends_on("lhapdf@6.2.3", when="@1.1.0")
    depends_on("pythia8@8244", when="@1.1.0")
    depends_on("dire@2.004", when="@1.1.0")
    # depends_on('cernlib@2006-12-20', when='@1.1.0')  # FIXME no package
    depends_on("lhapdf5@5.9.1", when="@1.1.0")
    depends_on("pythia6@6.4.28 +root", when="@1.1.0")  # FIXME was version RAD-CORR
    # EIC
    # depends_on('ejpm@0.3.21', when='@1.1.0')  # FIXME no package
    depends_on("eic-smear@1.0.4-fix1 +pythia6", when="@1.1.0")
    depends_on("ejana@1.2.3 +acts +genfit", when="@1.1.0")
    depends_on("g4e@1.3.5 ~validated", when="@1.1.0")
    depends_on("jana2@2.0.3 +root", when="@1.1.0")

    version("1.0.1")
    # Dev
    depends_on("cmake@3.17.0", when="@1.0.1")
    depends_on("boost@1.70.0", when="@1.0.1")
    depends_on("python@3.7.5", when="@1.0.1")
    # HENP
    depends_on("root@6.20.04 -vmc +pythia6 +pythia8 +root7 cxxstd=17", when="@1.0.1")
    depends_on("geant4@10.6.1 +opengl +qt cxxstd=17", when="@1.0.1")
    depends_on("eigen@3.3.7", when="@1.0.1")
    # FIXME geant4@10.6.1 depends_on clhep@2.4.1.3
    # depends_on('clhep@2.3.2.2', when='@1.0.1')
    depends_on("vgm@4-5", when="@1.0.1")
    depends_on("genfit@2020-06-03", when="@1.0.1")
    depends_on("hepmc@2.06.09", when="@1.0.1")
    depends_on("hepmc3@3.2.1 +interfaces +python +rootio", when="@1.0.1")
    depends_on("acts@0.22.0", when="@1.0.1")
    depends_on("delphes@3.4.2", when="@1.0.1")
    depends_on("fastjet@3.3.3", when="@1.0.1")
    # MCEG
    depends_on("lhapdf@6.2.3", when="@1.0.1")
    depends_on("pythia8@8244", when="@1.0.1")
    depends_on("dire@2.004", when="@1.0.1")
    # depends_on('cernlib@2006-12-20', when='@1.0.1')  # FIXME no package
    depends_on("lhapdf5@5.9.1", when="@1.0.1")  # FIXME was version 5.9.1.6
    depends_on("pythia6@6.4.28 +root", when="@1.0.1")  # FIXME was version RAD-CORR
    # EIC
    # depends_on('ejpm@0.3.12', when='@1.0.1')  # FIXME no package
    depends_on("eic-smear@1.0.4-fix1 +pythia6", when="@1.0.1")
    depends_on("ejana@1.2.2 +acts +genfit", when="@1.0.1")
    depends_on("g4e@1.3.4 ~validated", when="@1.0.1")
    depends_on("jana2@2.0.2 +root", when="@1.0.1")
