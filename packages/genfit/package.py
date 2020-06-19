# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Genfit(CMakePackage):
    """A generic track-fitting toolkit."""

    homepage = "http://github.com/GenFit/GenFit"
    url      = "http://github.com/GenFit/GenFit"
    git      = "http://github.com/GenFit/GenFit.git"

    version('master',  branch='master')
    version('2020-06-03', commit='8290f902ccaa657dbe49da871e78500b343ad080')
    version('2020-05-29', commit='36c46498d7cbdb6e1d25cdb7f7358c15433c03ff')

    #variant('rave', default=False, description="Include rave support") # FIXME
    variant('cxxstd',
            default='17',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('cmake@2.8:', type='build')
    depends_on('root@6.00.00: cxxstd=11', when='cxxstd=11')
    depends_on('root@6.00.00: cxxstd=14', when='cxxstd=14')
    depends_on('root@6.00.00: cxxstd=17', when='cxxstd=17')
    depends_on('eigen')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec.variants['cxxstd'].value)
        return args
