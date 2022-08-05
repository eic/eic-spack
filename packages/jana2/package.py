# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Jana2(CMakePackage):
    """Multi-threaded HENP Event Reconstruction."""

    homepage = "https://jeffersonlab.github.io/JANA2/"
    url      = "https://github.com/JeffersonLab/JANA2/archive/v2.0.3.tar.gz"
    list_url = "https://github.com/JeffersonLab/JANA2/releases"
    git      = "https://github.com/JeffersonLab/JANA2.git"

    maintainer = ["wdconinc"]

    tags = ['eic']

    version('master', branch='master')
    version('2.0.6', sha256='122ceba6e9541949803073b6e51fb594500132cf7535808d635bdc193e95a9e2')
    version('2.0.5', sha256='2e7297dfb0bd7f4a2f2fa3bca6b1c10b2553d321dec6060e48b0d75a5ed6717d')
    version('2.0.4', sha256='848adffcb881beb7835d01ce47a58991bb4f92664c9477196960ce8cfd94a3ca')
    version('2.0.3', sha256='fd34c40e2d6660ec08aca9208999dd9c8fe17de21c144ac68b6211070463e415')
    version('2.0.2', sha256='161d29c2b1efbfb36ec783734b45dff178b0c6bd77a2044d5a8829ba5b389b14')
    version('2.0.1', sha256='1471cc9c3f396dc242f8bd5b9c8828b68c3c0b72dbd7f0cfb52a95e7e9a8cf31')

    variant('root',
            default=False,
            description='Use ROOT for janarate.')
    variant('zmq',
            default=False,
            description='Use zeroMQ for janacontrol.')

    depends_on('cmake@3.9:', type='build')
    depends_on('cppzmq', when='+zmq')
    depends_on('root', when='+root')
    depends_on('xerces-c')

    def cmake_args(self):
        args = []
        # ZeroMQ directory
        if '+zmq' in self.spec:
            args.append('-DZEROMQ_DIR=%s'
                        % self.spec['cppzmq'].prefix)
        # C++ Standard
        if '+root' in self.spec:
            args.append('-DCMAKE_CXX_STANDARD=%s'
                        % self.spec['root'].variants['cxxstd'].value)
        else:
            args.append('-DCMAKE_CXX_STANDARD=11')

        return args

    def setup_run_environment(self, env):
        import os
        env.append_path('JANA_PLUGIN_PATH', os.path.join(self.prefix, 'plugins'))
        env.set('JANA_HOME', self.prefix)
