# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class G4e(CMakePackage):
    """Geant for EIC."""

    homepage = "https://g4e.readthedocs.io/en/latest/"
    url      = "https://gitlab.com/eic/escalate/g4e/-/archive/v1.3.2/g4e-v1.3.2.tar.gz"
    git      = "https://gitlab.com/eic/escalate/g4e.git"
    list_url = "https://gitlab.com/eic/escalate/g4e/-/tags"

    version('1.3.2', sha256='bf0c035e6e213d71aafd5851e35210f2c70742b82b7d3222b2f2fdf05c09c8f8')
    version('1.3.1', sha256='98afe3c3efe3dbad5b13b6d33964c600155a8a6684786a81181a987c0a358f50')

    depends_on('cmake@3.0.0:', type='build')
    depends_on('root@6.00.00:')
    depends_on('geant4') # FIXME minimum version
    depends_on('vgm') # FIXME minimum version
    depends_on('hepmc@2.06.10,2.06.09,2.06.08,2.06.07,2.06.06,2.06.05') # no strictly less than

    def cmake_args(self):
        args = []

        args.append('-DGEANT4_DIR={0}'.format(
            self.spec['geant4'].prefix))
        args.append('-DVGM_DIRECTORY={0}'.format(
            self.spec['vgm'].prefix))
        args.append('-DHEPMC_DIRECTORY={0}'.format(
            self.spec['hepmc2'].prefix))
        args.append('-DCERN_ROOT_DIRECTORY={0}'.format(
            self.spec['root'].prefix))

        return args
