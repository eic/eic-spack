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

    maintainer = ["DraTeots"]

    version('master',  branch='master')
    version('1.3.6', sha256='051ce2b1ff87df314a6395c22b33da19e1555caddd94d3863687101cdafad72b')
    version('1.3.5', sha256='e92d95df4b873bff3dff9fcff8a5535410a19004ae00c4a166f3adab8bd90279')
    version('1.3.4', sha256='9958a08a7cb8a8ce8b44d96e5e3c9b0bf45b2cb7bb9736f73a00cd907b73ffc8')
    version('1.3.2', sha256='bf0c035e6e213d71aafd5851e35210f2c70742b82b7d3222b2f2fdf05c09c8f8')
    version('1.3.1', sha256='98afe3c3efe3dbad5b13b6d33964c600155a8a6684786a81181a987c0a358f50')

    # This compatibility variant allows to use g4e with older root and geant versions
    variant('compat', default=False, description="Compatibility variant with older root, geant and others")
    depends_on('cmake@3.0.0:', type='build', when='+compat')
    depends_on('root@6.00.00:', when='+compat')
    depends_on('geant4@10.5:', when='+compat')
    depends_on('vgm@4-4:', when='+compat')
    depends_on('hepmc@2.06:', when='+compat')

    # This uses the latest versions consistent over escalate
    depends_on('cmake@3.0.0:', type='build', when='~compat')
    depends_on('root@6.20.04 +vmc +pythia6 +pythia8 +root7 cxxstd=17', when='~compat')
    depends_on('geant4@10.6.2 +opengl +python +qt cxxstd=17', when='~compat')
    depends_on('vgm@4-8', when='~compat')
    depends_on('hepmc@2.06.10', when='~compat')

    def cmake_args(self):
        args = []
        # >oO debug: from ppretty import ppretty
        # >oO debug: print(ppretty(self, seq_length=20))

        args.append('-DCMAKE_CXX_STANDARD=17')

        args.append('-DGEANT4_DIR={0}'.format(
            self.spec['geant4'].prefix))
        args.append('-DVGM_DIRECTORY={0}'.format(
            self.spec['vgm'].prefix))
        args.append('-DHEPMC_DIRECTORY={0}'.format(
            self.spec['hepmc'].prefix))
        args.append('-DCERN_ROOT_DIRECTORY={0}'.format(
            self.spec['root'].prefix))

        return args

    def setup_run_environment(self, env):
        env.append_path('G4E_MACRO_PATH', self.prefix)
        env.prepend_path('PYTHONPATH', self.prefix.python)
        env.set('G4E_HOME', self.prefix)
