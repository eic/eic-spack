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

    version('7.2.1', sha256='d4fff32f21c5c08a4b2e563c476b079859c2c8e3b78d853a8a60da96d5eea686')

    variant('evtgen', default=False, description='Include evtgen event format support.')
    variant('pythia8', default=False, description='Include Pythia8 event generator support.')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

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

    force_autoreconf = True

    def patch(self):
        if self.spec.satisfies('%gcc@10.0.0:'):
            filter_file('-ffixed-line-length-none',
                        '-ffixed-line-length-none -fallow-argument-mismatch',
                        'Looptools/Makefile.am')

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
