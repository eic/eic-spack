# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Fun4all(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "http://github.com/eic/fun4all_coresoftware"
    url      = "http://github.com/eic/fun4all_coresoftware"
    git      = "http://github.com/eic/fun4all_coresoftware.git"

    version('master', branch='master')

    depends_on('autoconf', type='build', when='@master')
    depends_on('automake', type='build', when='@master')
    depends_on('libtool',  type='build', when='@master')
    depends_on('bmf')
    depends_on('lzo')
    depends_on('unixodbc')
    depends_on('libodbcpp')
    depends_on('lhapdf5')
    depends_on('root')
    depends_on('geant4')

    resource(
        name='fun4all_utilities',
        git='https://github.com/eic/fun4all_utilities.git',
        branch='master',
        destination='.'
    )

    # grep -v \# fun4all_utilities/utils/rebuild/eic-repositories.txt | sed  -e "s|\(.*\)|        '\1',|"
    repositories = [
        'calibrations',
        'fun4all_acts',
        'fun4all_coresoftware',
        'fun4all_eicdetectors',
        'fun4all_g4jleic',
        'g4hakanvtx',
        'g4lblvtx',
        'online_distribution',
        'qinhua',
    ]
    resource(
        name='calibrations',
        git='https://github.com/eic/calibrations.git',
        branch='master',
        destination='.'
    )
    resource(
        name='fun4all_acts',
        git='https://github.com/eic/fun4all_acts.git',
        branch='master',
        destination='.'
    )
    resource(
        name='fun4all_coresoftware',
        git='https://github.com/eic/fun4all_coresoftware.git',
        branch='master',
        destination='.'
    )
    resource(
        name='fun4all_eicdetectors',
        git='https://github.com/eic/fun4all_eicdetectors.git',
        branch='master',
        destination='.'
    )
    resource(
        name='online_distribution',
        git='https://github.com/eic/online_distribution.git',
        branch='master',
        destination='.'
    )



    # grep -v \# fun4all_utilities/utils/rebuild/eic-packages.txt | cut -d\| -f1 | sed -e "s|\(.*\)|        '\1',|"
    packages = [
# fails due to no autogen.sh
#        'fun4all_acts',
        'fun4all_coresoftware/offline/packages/Half',
        'online_distribution/newbasic',
        'online_distribution/pmonitor',
        'fun4all_coresoftware/offline/framework/phool',
        'fun4all_coresoftware/offline/framework/phoolraw',
# fails due to missing ROOT TSQL.h, likely depends_on root +mysql
#        'fun4all_coresoftware/offline/database/pdbcal/base',
#        'fun4all_coresoftware/offline/database/pdbcal/pg',
#        'fun4all_coresoftware/offline/database/PHParameter',
        'fun4all_coresoftware/offline/packages/vararray',
        'fun4all_coresoftware/offline/framework/frog',
        'fun4all_coresoftware/offline/framework/ffaobjects',
        'fun4all_coresoftware/offline/framework/fun4all',
        'fun4all_coresoftware/offline/framework/fun4allraw',
        'fun4all_coresoftware/generators/JEWEL',
        'fun4all_coresoftware/generators/hijing',
        'fun4all_coresoftware/generators/sHijing',
        'fun4all_coresoftware/generators/flowAfterburner',
        'fun4all_coresoftware/offline/packages/HelixHough',
        'fun4all_coresoftware/offline/packages/PHGeometry',
        'fun4all_coresoftware/offline/packages/PHField',
        'fun4all_coresoftware/generators/phhepmc',
        'fun4all_coresoftware/generators/PHPythia8',
        'fun4all_coresoftware/generators/PHPythia6',
        'fun4all_coresoftware/generators/PHSartre',
        'fun4all_coresoftware/simulation/g4simulation/EICPhysicsList',
        'fun4all_coresoftware/simulation/g4simulation/g4decayer',
        'fun4all_coresoftware/simulation/g4simulation/g4gdml',
        'fun4all_coresoftware/simulation/g4simulation/g4main',
        'fun4all_coresoftware/simulation/g4simulation/g4detectors',
        'fun4all_coresoftware/offline/packages/CaloBase',
        'fun4all_coresoftware/offline/packages/trackbase',
        'fun4all_coresoftware/offline/packages/trackbase_historic',
        'fun4all_coresoftware/offline/packages/mvtx',
        'fun4all_coresoftware/offline/packages/intt',
        'fun4all_coresoftware/offline/packages/tpc',
        'fun4all_coresoftware/simulation/g4simulation/g4tpc',
        'fun4all_coresoftware/simulation/g4simulation/g4mvtx',
        'fun4all_coresoftware/simulation/g4simulation/g4intt',
        'fun4all_coresoftware/simulation/g4simulation/g4bbc',
        'fun4all_coresoftware/simulation/g4simulation/g4calo',
        'fun4all_coresoftware/offline/packages/trigger',
        'fun4all_coresoftware/offline/packages/PHGenFitPkg/GenFitExp',
        'fun4all_coresoftware/offline/packages/PHGenFitPkg/PHGenFit',
        'fun4all_coresoftware/simulation/g4simulation/g4vertex',
        'fun4all_coresoftware/simulation/g4simulation/g4jets',
        'fun4all_coresoftware/offline/packages/jetbackground',
        'fun4all_coresoftware/simulation/g4simulation/g4eval',
        'fun4all_coresoftware/simulation/g4simulation/g4trackfastsim',
        'fun4all_coresoftware/simulation/g4simulation/g4histos',
        'fun4all_coresoftware/offline/packages/trackreco',
        'fun4all_coresoftware/offline/packages/PHTpcTracker',
        'fun4all_coresoftware/offline/packages/tpccalib',
        'fun4all_coresoftware/offline/packages/CaloReco',
        'fun4all_coresoftware/offline/packages/ClusterIso',
        'fun4all_coresoftware/offline/packages/particleflow',
        'fun4all_coresoftware/offline/QA/modules',
        'fun4all_coresoftware/offline/packages/NodeDump',
        'fun4all_coresoftware/simulation/g4simulation/g4dst',
        'fun4all_eicdetectors/source',
#        'fun4all_g4jleic/source',
#        'g4lblvtx/source',
#        'qinhua/source',
#        'g4hakanvtx/source',
    ]

    build_directory = 'spack-build'

    def setup_environment(self, spack_env, run_env):
        spack_env.set('OFFLINE_MAIN', self.prefix)

    def install(self, spec, prefix):
        for package in self.packages:
            print(package)
            with working_dir(join_path(self.build_directory, package), create=True):
                autogen = Executable(join_path(self.stage.source_path, package, 'autogen.sh'))
                # FIXME shouldn't need to override include flags
                #cppflags = []
                #cppflags.append('-I' % self.spec['unixodbc'].prefix.include)
                #cppflags.append('-std=c++%s'
                #    % self.spec['root'].variants['cxxstd'].value)
                #autogen.add_default_env('CPPFLAGS', cppflags)
                args = []
                args.append('--prefix=%s' % self.spec.prefix)
                autogen(*args)
                make()
                make('install')
