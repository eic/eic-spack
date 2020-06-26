# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Milou(MakefilePackage):
    """MILOU is a Monte Carlo generator for deeply virtual
    Compton scattering (DVCS)."""

    homepage = "http://gitlab.com/eic/mceg/milou"
    url      = "http://gitlab.com/eic/mceg/milou"
    git      = "http://gitlab.com/eic/mceg/milou.git"

    version('master', branch='master')

    depends_on('cernlib')
    depends_on('pythia6')
    #depends_on('jetset')

    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')
        makefile.filter('CERN_LIBS = .*',
                        'CERN_LIBS = {0}/lib'.format(spec['cernlib'].prefix))
        makefile.filter('PYTHIA = .*',
                        'PYTHIA = -L{0}/lib -lPythia6'.format(spec['pythia6'].prefix))

    def make(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        make('install')
