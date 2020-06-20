# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class EicSmear(CMakePackage):
    """Monte Carlo analysis package originally
    developed by the BNL EIC task force."""

    homepage = "https://wiki.bnl.gov/eic/index.php/Monte_Carlo_and_Smearing"
    url      = "https://gitlab.com/eic/eic-smear"
    git      = "https://gitlab.com/eic/eic-smear.git"

    maintainers = ['wdconinc']

    variant("pythia6", default=False, description="Include Pythia6 support")

    version('master', branch='master')
    version('1.0.4',  branch='1.0.4')
    version('1.0.3',  branch='1.0.3')
    version('1.0.2',  branch='1.0.2')
    version('1.0.1',  branch='1.0.1')

    depends_on('root')
    depends_on('cmake', type='build')
    depends_on('pythia6', when='+pythia6')

    def cmake_args(self):
        args = []

        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec['root'].variants['cxxstd'].value)
        if '+pythia6' in self.spec.variants:
            args.append('-DPYTHIA6_LIBDIR={0}'.format(
                self.spec['pythia6'].prefix.lib))

        return args
