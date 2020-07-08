# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install cernlib
#
# You can edit this file again by typing:
#
#     spack edit cernlib
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Cernlib(Package):
    """CERNLIB for x64 systems. 
    
    By famous Mark Ito CERNLIB build scripts with patches. 
    Should work for RHEL 6,7,8, Fedora, Ubuntu
    https://github.com/JeffersonLab/build_scripts/blob/1.57/Makefile_cernlib_Vogt
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "http://www-zeuthen.desy.de/linear_collider/cernlib/new/cernlib-2005-all-new.tgz"

    version('2005.2014.04.17', sha256='25bda7271dce6e7d199039e46bd044e7eb97fd9c1287ccbf6d7b5772749e78a9')

    def url_for_version(self, version):
        """This function is here to disable 'smart' spack version substitution in url"""
        return 'http://www-zeuthen.desy.de/linear_collider/cernlib/new/cernlib-2005-all-new.tgz'

    
    variant('debug', default=False, description="Patch cernlib as debug whatever it means...")


    resource(name='CORR_FILE',
            url='http://www.zeuthen.desy.de/linear_collider/cernlib/new/cernlib.2005.corr.2014.04.17.tgz',
            sha256='f6b7c55be0f21578449d510b4728259be1ac84d0587ed3d00a4a4079caa9e568')

    # resource(name='ALL_FILE',
    #         url='http://www-zeuthen.desy.de/linear_collider/cernlib/new/cernlib-2005-all-new.tgz',
    #         sha256='71fa249dbfd278eec2b95ce577af32e623e44caf0d993905ddc189e3beec21d0',
    #         placement='tools')
        
    resource(name='INSTALL_FILE',
            url='http://www-zeuthen.desy.de/linear_collider/cernlib/new/cernlib.2005.install.2014.04.17.tgz',
            sha256='6d27b37ce71c7530cab954b281f3e42f2e7acadcc34e4b763ce9813dc2c6a24b')

    patch('https://raw.githubusercontent.com/JeffersonLab/build_scripts/1.57/patches/cernlib/Install_cernlib.patch',
            sha256='6a0344032b0475a040b6aeb574a364d26e00c06edfd8e56b159232dcd702ef13',
            when="~debug")

    patch('https://raw.githubusercontent.com/JeffersonLab/build_scripts/1.57/patches/cernlib/Install_cernlib.debug.patch',
            sha256='1bde70f58b5ac27598358af0ed53994b29adaba8c5a54fce6cb3eb23a906db19',
            when='+debug')

    patch('https://raw.githubusercontent.com/JeffersonLab/build_scripts/1.57/patches/cernlib/kstring.h.patch',
            sha256='f908cbe628f65362f5c0d9dbd0f990e7fb1437a4370581aacc3369e220e99e6d',
            working_dir='2005/src/packlib/kuip/kuip')

    patch('https://raw.githubusercontent.com/JeffersonLab/build_scripts/1.57/patches/cernlib/Imake.cf.patch',
            sha256='aba474eabdd84b65554d70c7cbe942151e0445af7576d89a02e0b5a13f95f003',
            working_dir='2005/src/config')

    patch('https://raw.githubusercontent.com/JeffersonLab/build_scripts/1.57/patches/cernlib/Install_old_patchy4.patch',
            sha256='ed74d2efcbaff68e4c10eed86b0a1c8d7d1fe5736413b0a5e5ac78123f869cf7',
            working_dir='2005/src/config')



    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def setup_build_environment(self, env):
        env.append_flags('FFLAGS', '-std=legacy')


    def install(self, spec, prefix):

        with working_dir('spack-build', create=True):
            configure = Executable('../configure')
            configure('--prefix=%s' % prefix, *options)
            make()
            make('check')
            make('ptcheck')
            make('time')
            if '+shared' in spec:
                with working_dir('lib'):
                    make('shared_all')

            make("install")
            if self.run_tests:
                self.install_test()


        # mkdir('-p', '2005/src/lib')
        # install('$(LAPACK_HOME)/liblapack.a', '2005/src/lib/liblapack.a')
        
        # install('$(LAPACK_HOME)/librefblas.a', '2005/src/lib/libblas.a')
        # mkdir('-p', '2005/lib')
        # install('$(LAPACK_HOME)/liblapack.a', '2005/lib/liblapack3.a')
        # install('$(LAPACK_HOME)/librefblas.a', '2005/lib/libblas.a')
        # executable = Executable('./Install_cernlib')
        # executable()

