# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Djangoh(MakefilePackage):
    """DJANGOH simulates deep inelastic lepton-proton scattering for
    NC and CC events, including QED and QCD radiative effects"""

    homepage = "http://gitlab.com/eic/mceg/DJANGOH-4.6.10"
    url      = "http://gitlab.com/eic/mceg/DJANGOH-4.6.10/-/archive/master/DJANGOH-4.6.10-master.tar.gz"
    git      = "http://gitlab.com/eic/mceg/DJANGOH-4.6.10.git"

    version('master', branch='master')

    depends_on('lhapdf5')
    #depends_on('cernlib')

    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')
        # makefile.filter('CC = .*', 'CC = cc')

    def setup_build_environment(self, env):
        spec = self.spec
        env.set('LHAPDF', spec['lhapdf5'].prefix)
        #env.set('CERN_ROOT', spec['cernlib'].prefix)
        env.set('EICDIRECTORY', spec.prefix)

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        make('install')
