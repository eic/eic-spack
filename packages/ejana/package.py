# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *



class Ejana(CMakePackage):
    """Implementation of EIC reconstruction in JANA."""

    homepage = "http://gitlab.com/eic/escalate/ejana/"
    url      = "http://gitlab.com/eic/escalate/ejana/-/archive/v1.2.1/ejana-v1.2.1.tar.gz"
    git      = "http://gitlab.com/eic/escalate/ejana.git"
    list_url = "https://gitlab.com/eic/escalate/ejana/-/tags"

    maintainer = ["wdconinc"]

    version('master', branch='master')
    version('1.2.3', sha256='552bd7bd536ecb33c55cc9c1dfb3f870c253fd355456d6cca26c3665f450920d')
    version('1.2.2', sha256='d6e906591159014cbfa9a2a4ebc0354fdd8948436dddb8c3edc0bdf5d9544b69')
    version('1.2.1', sha256='80c1c16f7e350747c7980526c6c863db44c9b5dca9aadfe8e1be40e8ba352acd')
    version('1.2.0', sha256='9390facfcf77702efb102d3fda7711e2da025c7637b23f45ee055507fabda71a')

    # This uses the latest versions consistent over escalate

        # This compatibility variant allows to use g4e with older root and geant versions
    variant('validated', default=False, description="Validated with exact versions of ROOT, etc.")
    depends_on('cmake@3.0.0:', type='build', when='~validated')
    depends_on('root@6.00.00: cxxstd=17', when='~validated')
    depends_on('hepmc3@3.2.1:', when='~validated')


    # This uses the latest versions consistent over escalate
    depends_on('cmake@3.0.0:', type='build', when='+validated')
    depends_on('root@6.20.04 +vmc +pythia6 +pythia8 +root7 cxxstd=17', when='+validated')
    depends_on('hepmc3@3.2.2', when='+validated')

    depends_on('eic-smear@1.1.0-rc2')
    depends_on('jana2@2.0.3')
    


    # variant('acts', default=False, description='Use ACTS')
    # variant('genfit', default=False, description='Use genfit')

    # depends_on('cmake@3.9:', type='build')
    # depends_on('jana2')
    # depends_on('hepmc3')
    # depends_on('root@6.00.00:')
    # depends_on('acts', when='+acts')
    # depends_on('genfit', when='+genfit')
    # depends_on('eic-smear')

    # FIXME acts should be variant only
    #depends_on('acts +identification +tgeo')

    # FIXME genfit should be variant only
    #depends_on('genfit')

    def cmake_args(self):
        args = []
        args.append('-DCMAKE_CXX_STANDARD=17')
        args.append('-DROOT_DIR={0}'.format(self.spec['root'].prefix))
        args.append('-DJANA_DIR={0}'.format(self.spec['jana2'].prefix))
        args.append('-DHepMC3_DIR={0}'.format(self.spec['hepmc3'].prefix))
        args.append('-DEIC_SMEAR_DIR={0}'.format(self.spec['eic-smear'].prefix))
        
        if '+acts' in self.spec:
            args.append('-DActs_DIR={0}'.format(self.spec['acts'].prefix))
        if '+genfit' in self.spec:
            args.append('-DGENFIT_DIR={0}'.format(self.spec['genfit'].prefix))

        return args
    
    def setup_run_environment(self, env):
        import os
        env.set('EJANA_HOME', self.prefix)
        env.append_path('JANA_PLUGIN_PATH', os.path.join(self.prefix, 'plugins'))

