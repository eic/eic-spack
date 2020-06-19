# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Escalate(BundlePackage):
    """EIC Softare Consortium environment."""

    homepage = "http://gitlab.com/eic/escalate"

    version('1.0.1')
    # HENP
    depends_on('root@6.20.04', when='@1.0.1')
    depends_on('geant4@10.6.1', when='@1.0.1')
    depends_on('eigen@3.3.7', when='@1.0.1')
    #depends_on('clhep@2.3.2.2', when='@1.0.1') # FIXME geant4@10.6.1 depends_on clhep@2.4.1.3
    #depends_on('vgm@4.5', when='@1.0.1') # FIXME no package
    #depends_on('genfit@2020.1', when='@1.0.1') # FIXME no package
    depends_on('hepmc@2.06.09', when='@1.0.1')
    #depends_on('hepmc@3.2.1', when='@1.0.1') # FIXME Error: 2.06.09 does not satisfy 3.2.1
    depends_on('acts@0.22.0', when='@1.0.1')
    depends_on('delphes@3.4.2', when='@1.0.1')
    depends_on('fastjet@3.3.3', when='@1.0.1')
    # MCEG
    depends_on('lhapdf@6.2.3', when='@1.0.1')
    #depends_on('pythia8@8244', when='@1.0.1') # FIXME no version
    #depends_on('dire@2.004', when='@1.0.1') # FIXME no package
    #depends_on('cernlib@2006-12-20', when='@1.0.1') # FIXME no package
    #depends_on('lhapdf5@5.9.1.6', when='@1.0.1') # FIXME no version
    #depends_on('pythia6@RAD-CORR', when='@1.0.1') # FIXME no version
    # EIC
    #depends_on('ejpm@0.3.12', when='@1.0.1') # FIXME no package
    #depends_on('eic-smear@1.0.4f1', when='@1.0.1') # FIXME no version
    #depends_on('ejana@1.2.2', when='@1.0.1') # FIXME no package
    #depends_on('g4e@1.3.4', when='@1.0.1') # FIXME no package
    depends_on('jana2@2.0.2', when='@1.0.1')
