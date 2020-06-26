# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pepsi(MakefilePackage):
    """PEPSI (Polarised Electron Proton Scattering Interactions)
    is a Monte Carlo generator for polarised deep inelastic
    scattering (pDIS)."""

    homepage = "http://github.com/eic/pepsi"
    url      = "http://github.com/eic/pepsi"
    git      = "http://github.com/eic/pepsi.git"

    version('master', branch='master')

    depends_on('nanocernlib')

    def setup_build_environment(self, env):
        spec = self.spec
        env.set('EICDIRECTORY', self.spec.prefix)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        make()
        make('install')
        install_tree('pdf/', join_path(prefix.share, 'pdf'))
        install_tree('STEER-FILES/', join_path(prefix.share, 'STEER-FILES'))
