# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Cernlib(Package):
    """The CERN Program Library is a large collection of general purpose libraries and modules """

    homepage = "http://cernlib.web.cern.ch/cernlib/"
    url      = "https://github.com/JeffersonLab/build_scripts/archive/2.0.tar.gz"

    maintainers = ['DraTeots', 'wdconinc']

    version('2.0',  sha256='83dc64f3db376ef23abd863f8f2a556f4c5c2a0ff522840d88014d6ec374a415')
    version('1.59', sha256='6c68f89bd0cf684709931d9e7392cacd08d691399f5e2d3b04019aaef15ec879')

    
    depends_on('netlib-lapack')
    depends_on('imake', when='build')

    # Openstf has "Makefile" and "Makefile_gcc".
    # "Makefile" is used only in Windows development environment.
    # The build in Windows development environment is not confirmed.
    def build(self, spec, prefix):
        #import pdb; pdb.set_trace()
        print("===============build===============")

        # with working_dir('src'):
        #     if '%gcc' in self.spec:
        #         make('-f', 'Makefile_gcc')
        #     elif '%fj' in self.spec:
        #         make('-f', 'Makefile_gcc')
        #     else:
        #         make()

    def install(self, spec, prefix):
        print("install===")
        #print(dir(spec))
        
        print(os.listdir(self.stage.source_path))
        print(os.getcwd())
        lapack_dir = os.path.join(prefix, 'lapack')
        os.mkdir(lapack_dir)

        with working_dir(lapack_dir):
            print("lapack_dir!!!!!!!!!!!!!!!!")
            print(os.getcwd())
            bash("make", "-f", "jopa")
            make("VERBOSE=1","-f",  self.stage.source_path + '/Makefile_lapack')

        with working_dir(prefix):
            print("HERE!!!!!!!!!!!!!!!!")
            print(os.getcwd())
            make("VERBOSE=1","-f",  self.stage.source_path + '/Makefile_cernlib_Vogt')
        
        #import pdb; pdb.set_trace()

    #     # FIXME: Unknown build system
    #     make()
    #     make('install')


    def setup_build_environment(self, env):
        #print(dict(self.spec))
        #env.set('LAPACK_HOME', os.path.join(self.spec['netlib-lapack'].prefix, 'lib'))
        env.set('LAPACK_HOME', os.path.join(self.spec.prefix, 'lapack'))
        env.set('BUILD_SCRIPTS', self.stage.source_path)
        
