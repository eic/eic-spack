# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pythia6m(CMakePackage):
    """Pythia6 modified to better describe lepton-nucleon scattering
    at intermediate energies."""

    homepage = "http://gitlab.com/eic/mceg/pythia6m"
    url      = "http://gitlab.com/eic/mceg/pythia6m/-/archive/master/pythia6m-master.tar.gz"
    git      = "http://gitlab.com/eic/mceg/pythia6m.git"

    version('master', branch='master')

    variant('cxxstd',
            default='11',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('cmake@2.8:', type='build')
    depends_on('boost cxxstd=11', when='cxxstd=11')
    depends_on('root cxxstd=11', when='cxxstd=11')
    depends_on('boost cxxstd=14', when='cxxstd=14')
    depends_on('root cxxstd=14', when='cxxstd=14')
    depends_on('boost cxxstd=17', when='cxxstd=17')
    depends_on('root cxxstd=17', when='cxxstd=17')
    depends_on('nanocernlib')

    def cmake_args(self):
        args = []
        # nanocernlib
        args.append('-Dnanocernlib_DIR=%s'
                    % self.spec['nanocernlib'].prefix)
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec.variants['cxxstd'].value)
        return args
