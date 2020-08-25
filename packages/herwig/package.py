# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Herwig(AutotoolsPackage):
    """Herwig is a multi-purpose particle physics event generator."""

    homepage = "https://herwig.hepforge.org"
    url      = "https://herwig.hepforge.org/downloads/Herwig-7.1.0.tar.bz2"

    maintainers = ['wdconinc']

    version('7.1.0', sha256='333d11d5bc448dd1cd1f24f6945adc29203f2b235e18db655ed09e237dc78974')

    variant('evtgen', default=False, description='Include evtgen event format support.')
    variant('pythia8', default=False, description='Include Pythia8 event generator support.')

    depends_on('thepeg')
    depends_on('fastjet')
    depends_on('gsl +external-cblas') # FIXME regular gsl fails to link cblas correctly
    depends_on('boost')

    depends_on('evtgen', when='+evtgen')
    depends_on('pythia8', when='+pythia8')
    # FIXME Optional dependencies:
    #        --with-vbfnlo=$INSTALL_LOC
    #        --with-njet=$INSTALL_LOC \
    #        --with-gosam=$INSTALL_LOC
    #        --with-openloops=/where/openloops/was/installed \
    #        --with-madgraph=/where/madgraph/was/installed  \

    def configure_args(self):
        args = []
        args.append('--with-gsl=' + self.spec['gsl'].prefix)
        args.append('--with-boost=' + self.spec['boost'].prefix)
        args.append('--with-thepeg=' + self.spec['thepeg'].prefix)
        args.append('--with-fastjet=' + self.spec['fastjet'].prefix)
        if self.spec.satisfies('+evtgen'):
            args.append('--with-evtgen=' + self.spec['evtgen'].prefix)
        if self.spec.satisfies('+pythia8'):
            args.append('--with-pythia=' + self.spec['pythia8'].prefix)
        return args
