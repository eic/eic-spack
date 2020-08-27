# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import tarfile


class Cernlib(Package):
    """The CERN Program Library is a large collection of general purpose libraries and modules """

    homepage = "http://cernlib.web.cern.ch/cernlib/"
    url      = "http://www-zeuthen.desy.de/linear_collider/cernlib/new/cernlib-2005-all-new.tgz"

    maintainers = ['DraTeots', 'wdconinc']

    version(
        '2014.04.17',
        sha256='25bda7271dce6e7d199039e46bd044e7eb97fd9c1287ccbf6d7b5772749e78a9',
        url='http://www-zeuthen.desy.de/linear_collider/cernlib/new/cernlib-2005-all-new.tgz'
    )

    resource(
        name='cernlib.2005.corr.2014.04.17.tgz',
        url='http://www-zeuthen.desy.de/linear_collider/cernlib/new/cernlib.2005.corr.2014.04.17.tgz',
        sha256='f6b7c55be0f21578449d510b4728259be1ac84d0587ed3d00a4a4079caa9e568',
        destination='resources',
        placement='corr',
        expand=False,
        when='@2014.04.17'
    )
    resource(
        name='cernlib.2005.install.2014.04.17.tgz',
        url='http://www-zeuthen.desy.de/linear_collider/cernlib/new/cernlib.2005.install.2014.04.17.tgz',
        sha256='6d27b37ce71c7530cab954b281f3e42f2e7acadcc34e4b763ce9813dc2c6a24b',
        destination='resources',
        placement='install',
        expand=False,
        when='@2014.04.17'
    )

    resource(
        name='build_scripts',
        git='https://github.com/JeffersonLab/build_scripts',
        tag='2.1',
        destination='resources',
        placement='build_scripts',
    )

    depends_on('makedepend', type='build')
    depends_on('imake', type='build')
    depends_on('gmake', type='build')
    depends_on('netlib-lapack')

    phases = ['unpack', 'repatch', 'build', 'install']

    def setup_build_environment(self, env):
        env.set('CERN',
                self.stage.source_path)
        env.set('BUILD_SCRIPTS',
                join_path(self.stage.source_path,
                          'resources/build_scripts'))

    def unpack(self, spec, prefix):
        # Untar inner tar files
        install_tar = tarfile.open(
            'resources/install/cernlib.2005.install.2014.04.17.tgz')
        install_tar.extractall()

        # Update corr tar file
        copy('resources/corr/cernlib.2005.corr.2014.04.17.tgz',
             'cernlib.2005.corr.tgz')

        # Unpack cernlib src
        install_cernlib_src = Executable('./Install_cernlib_src')
        install_cernlib_src()

    def repatch(self, spec, prefix):
        # Apply patches
        src = self.stage.source_path
        patches = join_path(src, 'resources/build_scripts/patches')
        patch = which('patch')
        with working_dir(src):
            patch('-i', join_path(patches, 'cernlib/Install_cernlib.patch'))
            patch('-i', join_path(patches, 'cernlib/Install_old_patchy4.patch'))
        with working_dir(join_path(src, '2005/src/packlib/kuip/kuip')):
            patch('-i', join_path(patches, 'cernlib/kstring.h.patch'))
        with working_dir(join_path(src, '2005/src/config')):
            patch('-i', join_path(patches, 'cernlib/Imake.cf.patch'))
        if self.spec.satisfies('%gcc@9:'):
            with working_dir(join_path(src, '2005/src/pawlib/paw/fmotif')):
                patch('Imakefile',
                      '-i', join_path(patches, 'cernlib/Imakefile_fmotif.patch'))
        if self.spec.satisfies('%gcc@10:'):
            with working_dir(join_path(src, '2005/src/config')):
                patch('linux-lp64.cf',
                      '-i', join_path(patches, 'cernlib/linux-lp64.cf.patch'))

    def build(self, spec, prefix):
        # Copy lapack and blas to their cernlib locations
        lapack_dirs = ['2005/src/lib', '2005/lib']
        lapack_files = ['liblapack.a', 'libblas.a']
        for lapack_dir in lapack_dirs:
            mkdirp(lapack_dir)
            for lapack_file in lapack_files:
                install(join_path(spec['netlib-lapack'].prefix.lib, lapack_file),
                        join_path(lapack_dir, lapack_file))

        # Install (i.e. build) cernlib
        install_cernlib = Executable('./Install_cernlib')
        install_cernlib()

    def install(self, spec, prefix):
        # Install tree to final location
        level='2005'
        for dir in ['bin', 'lib', 'include']:
            install_tree(join_path(level, dir),
                         join_path(prefix, dir))
        # Link level to prefix
        symlink(prefix, join_path(prefix, level))

    def setup_run_environment(self, env):
        env.set('CERN', self.prefix)
        env.set('CERN_LEVEL', '2005')
