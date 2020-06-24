# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class EictoymodelGit(CMakePackage):
    """EicToyModel (ETM) is a C++ ROOT-based software suite
    for EIC Central Detector configuration purposes."""

    homepage = "http://github.com/eic/EicToyModel"
    url      = "http://github.com/eic/EicToyModel.git"
    git      = "http://github.com/eic/EicToyModel.git"

    version('master', branch='master')

    depends_on('root')
    depends_on('vgm')
    depends_on('oce')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                % self.spec['root'].variants['cxxstd'].value)
        args.append('-DOPENCASCADE=%s'
                % self.spec['oce'].prefix)
        return args

