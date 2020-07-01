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

    depends_on('cmake@2.8:', type='build')
    depends_on('nanocernlib')
    depends_on('root')

    def cmake_args(self):
        args = []
        # nanocernlib
        args.append('-Dnanocernlib_DIR=%s'
                    % self.spec['nanocernlib'].prefix)
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec['root'].variants['cxxstd'].value)
        return args
