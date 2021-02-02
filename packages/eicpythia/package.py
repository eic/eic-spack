# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Eicpythia(CMakePackage):
    """Pythia6 modified to better describe lepton-nucleon scattering
    at intermediate energies."""

    homepage = "https://gitlab.com/eic/mceg/PYTHIA-RAD-CORR"
    url      = "https://gitlab.com/eic/mceg/PYTHIA-RAD-CORR/-/archive/master/PYTHIA-RAD-CORR-master.tar.gz"
    git      = "https://gitlab.com/eic/mceg/PYTHIA-RAD-CORR.git"

    version('master', branch='master', submodules=True)

    depends_on('cmake@3.0:', type='build') # older may be ok too
    depends_on('lhapdf5@5.9.0:5.9.99', type='link')
    # depends_on('root')

    def cmake_args(self):
        args = []
        # args.append('-DCMAKE_CXX_STANDARD=%s'
        #            % self.spec['root'].variants['cxxstd'].value)
        # C++ Standard
        # args.append('-DCMAKE_CXX_STANDARD=%s'
        #            % self.spec['root'].variants['cxxstd'].value)
        return args
