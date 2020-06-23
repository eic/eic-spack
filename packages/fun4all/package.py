# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Fun4all(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "http://github.com/eic/fun4all_coresoftware"
    url      = "http://github.com/eic/fun4all_coresoftware/archive/pro.3.tar.gz"

    version('3', sha256='0258b7e44b0162c1c1fbc2161b3e77cedaed58b78363a8a143c38ee525f31b8a')
    version('2', sha256='1b9a240204a9d82f86ae2a74eb53e0f81e20cca47ff4ace68398b3c78d813552')

    depends_on('autoconf', type='build', when='@master')
    depends_on('automake', type='build', when='@master')
    depends_on('libtool',  type='build', when='@master')
    depends_on('lzo')
    depends_on('root')

    resource(
        name='online_distribution',
        git='https://github.com/eic/online_distribution.git',
        branch='master',
        destination='.'
    )

    deptree = [
        'offline/packages/Half',
        'offline/framework/phool',
        'offline/database/pdbcal/base',
        'offline/database/pdbcal/pg',
        'offline/packages/vararray',
        'offline/framework/frog',
        'offline/framework/ffaobjects',
        'offline/framework/fun4all',
        'offline/QA/modules',
        'offline/packages/jetbackground',
        'offline/packages/Prototype2',
        'offline/packages/HelixHough',
        'offline/packages/Prototype3',
        'offline/packages/NodeDump',
        'offline/packages/PHGeometry',
        'offline/packages/PHGenFitPkg/PHGenFit',
        'offline/packages/PHGenFitPkg/GenFitExp',
        'offline/packages/trigger',
#        'generators/PHPythia6',
#        'generators/flowAfterburner',
#        'generators/PHPythia8',
#        'generators/hijing',
#        'generators/sHijing',
#        'generators/sHEPGen',
#        'generators/PHSartre',
#        'simulation/g4simulation/g4eval',
#        'simulation/g4simulation/g4decayer',
#        'simulation/g4simulation/g4cemc',
#        'simulation/g4simulation/g4vertex',
#        'simulation/g4simulation/g4picoDst',
#        'simulation/g4simulation/g4jets',
#        'simulation/g4simulation/g4dst',
#        'simulation/g4simulation/g4main',
#        'simulation/g4simulation/g4hough',
#        'simulation/g4simulation/g4bbc',
#        'simulation/g4simulation/g4detectors',
#        'simulation/g4simulation/g4field',
#        'simulation/g4simulation/g4gdml',
#        'simulation/g4simulation/phhepmc',
#        'simulation/g4simulation/g4histos',
    ]

    def install(self, spec, prefix):
        for dir in ['newbasic', 'pmonitor']:
            with working_dir(join_path('online_distribution', dir)):
                autogen = Executable('./autogen.sh')
                autogen('--prefix=%s' % self.spec.prefix)
                make()
                make('install')
        for dir in self.deptree:
            with working_dir(dir):
                autogen = Executable('./autogen.sh')
                # FIXME shouldn't need to override include flags
                cppflags = []
                cppflags.append('-I..')
                cppflags.append('-std=c++%s'
                    % self.spec['root'].variants['cxxstd'].value)
                autogen.add_default_env('CPPFLAGS', cppflags)
                autogen.add_default_env('OFFLINE_MAIN', self.spec.prefix)
                args = []
                args.append('--prefix=%s' % self.spec.prefix)
                autogen(*args)
                make()
                make('install')
