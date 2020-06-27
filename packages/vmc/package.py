# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class Vmc(CMakePackage):
    """Virtual Monte Carlo core library"""

    homepage = "http://github.com/vmc-project/vmc"
    url      = "http://github.com/vmc-project/vmc/archive/v1-0-p2.tar.gz"
    git      = "http://github.com/vmc-project/vmc.git"

    maintainer = ['wdconinc']

    version('master', branch='master')
    version('1-0-p2', sha256='46b4c82b0b7516502e88db920732fc78f06f0393ac740a17816f2eb53f80e75e')
    version('1-0-p1', sha256='4a20515f7de426797955cec4a271958b07afbaa330770eeefb5805c882ad9749')
    version('1-0',    sha256='3da58518b32db1b503082e3205884802a1a263a915071b96e3fd67861db3ca40')
    version('0-1',    sha256='c966a48ceb014cfdac9272fd08a0f6ee07e6b7d6e8bb220ae2d150e0755541b5')

    depends_on('cmake@3.3:', type='build')
    depends_on('root')
