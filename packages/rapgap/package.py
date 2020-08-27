# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Rapgap(AutotoolsPackage):
    """Hadron level Monte Carlo generator for ep
    and selected processes in pp scattering."""

    homepage = "http://rapgap.hepforge.org/"
    url      = "http://rapgap.hepforge.org/downloads/?f=rapgap-3.303.tar.gz"

    maintainer = ['mdiefent']

    version('3.303', sha256='7e8076a91e1d1c55a09f48c7e4f84eacd6653602cc43f7d72f88d7b0e5f1badd')
    version('3.302', sha256='84634ffa6fb89b33c5f12aa5227d65543b61a2ba7a374ca1681f8bb563e12662')
    version('3.301', sha256='c85afafdebd4e2e0645dff3e2cca0371b2a6363487a468eb5213e6030edf9663')
    version('3.203', sha256='ac54fb78c78c3bb8ab8bc13139677d6daa155406c50acc74d05b4ec536b92e07')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('pythia6')
    depends_on('lhapdf5')
    depends_on('hepmc')

    force_autoreconf = True

    def patch(self):
        # Search for libPythia, not libpythia
        filter_file('libpythia6',
                    'libPythia6',
                    'configure.ac')
        # Link libPythia6, not libpythia6
        filter_file('-lpythia6 -lpythia6_dummy',
                    '-lPythia6',
                    'configure.ac')

    def configure_args(self):
        args = []
        args.append('--with-pythia6={0}'.format(
            self.spec['pythia6'].prefix))
        args.append('--with-lhapdf={0}'.format(
            self.spec['lhapdf5'].prefix))
        args.append('--with-hepmc={0}'.format(
            self.spec['hepmc'].prefix))
        return args
