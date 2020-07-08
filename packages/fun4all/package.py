# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import glob


class Fun4all(Package):
    """Fun4All is the core software framework of the sPHENIX collaboration."""

    homepage = "http://github.com/eic/fun4all_utilities"
    url      = "http://github.com/eic/fun4all_utilities"
    git      = "http://github.com/eic/fun4all_utilities.git"

    # FIXME versions
    version('master', branch='master')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('bmf')
    depends_on('lzo')
    depends_on('rdbc')
    depends_on('lhapdf5')
    depends_on('fastjet')
    depends_on('hepmc')
    depends_on('cgal')
    depends_on('eigen')
    depends_on('pythia6')
    depends_on('pythia8')
    depends_on('sartre')
    depends_on('root')
    depends_on('geant4')

    # FIXME grab repositories from utilities
    # grep -v \# fun4all_utilities/utils/rebuild/eic-repositories.txt | sed  -e "s|\(.*\)|        '\1',|"
    repositories = []
    repository_names = [
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
    for r in repository_names:
        repositories.append(
            resource(
                name=r,
                git='https://github.com/eic/' + r + '.git',
                branch='master',
                destination='.'
            )
        )

    # FIXME grab packages from utilities
    # grep -v \# fun4all_utilities/utils/rebuild/eic-packages.txt | cut -d\| -f1 | sed -e "s|\(.*\)|        '\1',|"
    packages = [
# fails due to no autogen.sh
#        'fun4all_acts',
        'fun4all_coresoftware/offline/packages/Half',
        'online_distribution/newbasic',
        'online_distribution/pmonitor',
        'fun4all_coresoftware/offline/framework/phool',
        'fun4all_coresoftware/offline/framework/phoolraw',
        'fun4all_coresoftware/offline/database/pdbcal/base',
        'fun4all_coresoftware/offline/database/pdbcal/pg',
        'fun4all_coresoftware/offline/database/PHParameter',
        'fun4all_coresoftware/offline/packages/vararray',
        'fun4all_coresoftware/offline/framework/frog',
        'fun4all_coresoftware/offline/framework/ffaobjects',
        'fun4all_coresoftware/offline/framework/fun4all',
        'fun4all_coresoftware/offline/framework/fun4allraw',
        'fun4all_coresoftware/generators/JEWEL',
        'fun4all_coresoftware/generators/hijing',
        'fun4all_coresoftware/generators/sHijing',
        'fun4all_coresoftware/generators/flowAfterburner',
        'fun4all_coresoftware/offline/packages/PHGeometry',
        'fun4all_coresoftware/offline/packages/PHField',
#        'fun4all_coresoftware/generators/phhepmc',
#        'fun4all_coresoftware/generators/PHPythia8',
#        'fun4all_coresoftware/generators/PHPythia6',
#        'fun4all_coresoftware/generators/PHSartre',
#        'fun4all_coresoftware/simulation/g4simulation/EICPhysicsList',
#        'fun4all_coresoftware/simulation/g4simulation/g4decayer',
#        'fun4all_coresoftware/simulation/g4simulation/g4gdml',
#        'fun4all_coresoftware/simulation/g4simulation/g4main',
#        'fun4all_coresoftware/simulation/g4simulation/g4detectors',
#        'fun4all_coresoftware/offline/packages/CaloBase',
#        'fun4all_coresoftware/offline/packages/trackbase',
#        'fun4all_coresoftware/offline/packages/trackbase_historic',
#        'fun4all_coresoftware/offline/packages/mvtx',
#        'fun4all_coresoftware/offline/packages/intt',
#        'fun4all_coresoftware/offline/packages/tpc',
#        'fun4all_coresoftware/offline/packages/HelixHough', # depends on trackbase, was before PHGeometry
#        'fun4all_coresoftware/simulation/g4simulation/g4tpc',
#        'fun4all_coresoftware/simulation/g4simulation/g4mvtx',
#        'fun4all_coresoftware/simulation/g4simulation/g4intt',
#        'fun4all_coresoftware/simulation/g4simulation/g4bbc',
#        'fun4all_coresoftware/simulation/g4simulation/g4calo',
#        'fun4all_coresoftware/offline/packages/trigger',
#        'fun4all_coresoftware/offline/packages/PHGenFitPkg/GenFitExp',
#        'fun4all_coresoftware/offline/packages/PHGenFitPkg/PHGenFit',
#        'fun4all_coresoftware/simulation/g4simulation/g4vertex',
#        'fun4all_coresoftware/simulation/g4simulation/g4jets',
#        'fun4all_coresoftware/offline/packages/jetbackground',
#        'fun4all_coresoftware/simulation/g4simulation/g4eval',
#        'fun4all_coresoftware/simulation/g4simulation/g4trackfastsim',
#        'fun4all_coresoftware/simulation/g4simulation/g4histos',
#        'fun4all_coresoftware/offline/packages/trackreco',
#        'fun4all_coresoftware/offline/packages/PHTpcTracker',
#        'fun4all_coresoftware/offline/packages/tpccalib',
#        'fun4all_coresoftware/offline/packages/CaloReco',
#        'fun4all_coresoftware/offline/packages/ClusterIso',
#        'fun4all_coresoftware/offline/packages/particleflow',
#        'fun4all_coresoftware/offline/QA/modules',
#        'fun4all_coresoftware/offline/packages/NodeDump',
#        'fun4all_coresoftware/simulation/g4simulation/g4dst',
#        'fun4all_eicdetectors/source',
#        'fun4all_g4jleic/source',
#        'g4lblvtx/source',
#        'qinhua/source',
#        'g4hakanvtx/source',
    ]

    build_directory = '../spack-build'

    def patch(self):
        # Collect all Makefile.am
        makefiles = glob.glob('**/Makefile.am', recursive=True)
        # Add CPPFLAGS to all rootcint commands
        filter_file('AM_CPPFLAGS\)',
                    'AM_CPPFLAGS) $(CPPFLAGS)',
                    *makefiles)
        # Replace OFFLINE_MAIN for dependencies
        for dir, dep in zip(['HepMC'], ['hepmc']):
            filter_file('\$\(OFFLINE_MAIN\)/include/{0}/'.format(dir),
                        '{0}/{1}/'.format(self.spec[dep].prefix.include, dir),
                        *makefiles)

    def setup_environment(self, spack_env, run_env):
        spack_env.set('OFFLINE_MAIN', self.prefix)

    def install(self, spec, prefix):
        # Set cppflags and ldflags for packages that fail to find them
        cppflags = []
        ldflags = []
        for dep in ['hepmc']:
            cppflags.append('-I' + self.spec[dep].prefix.include)
            ldflags.append('-L' + self.spec[dep].prefix.lib)
        # Loop over packages
        for package in self.packages:
            print(package)
            with working_dir(join_path(self.build_directory, package), create=True):
                autogen = Executable(join_path(self.stage.source_path, package, 'autogen.sh'))
                args = []
                args.append('--prefix=%s' % self.spec.prefix)
                args.append('CPPFLAGS=' + ' '.join(cppflags))
                args.append('LDFLAGS=' + ' '.join(ldflags))
                autogen(*args)
                make()
                make('install')