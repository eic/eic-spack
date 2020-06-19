# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Eicroot(CMakePackage):
    """EicRoot software framework"""

    homepage = "https://github.com/eic/EicRoot"
    url      = "https://github.com/eic/EicRoot"
    git      = "https://github.com/eic/EicRoot.git"

    version('master')

    depends_on('root@6.00.00:')
    depends_on('geant4-vmc')

    def cmake_args(self):
        spec = self.spec

        args = []
        args.append('-DCAD2ROOT=no')
        args.append('-DHTC=no')

        return args
