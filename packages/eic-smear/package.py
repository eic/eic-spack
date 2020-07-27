# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class EicSmear(CMakePackage):
    """Monte Carlo analysis package originally
    developed by the BNL EIC task force."""

    homepage = "https://wiki.bnl.gov/eic/index.php/Monte_Carlo_and_Smearing"
    url      = "https://github.com/eic/eic-smear/archive/1.0.4.tar.gz"
    git      = "https://github.com/eic/eic-smear.git"

    maintainers = ['wdconinc']

    variant("pythia6", default=False, description="Include Pythia6 support")

    version('master', branch='master')
    version('1.1.0-rc1',  sha256='e3da232320522fb078f8795ee31f06032bae454ccc7c9368e393c94ab4b88db0')
    version('1.0.4-fix1', sha256='ae312f4440b7ec5eeda75631bea209d733186199eaa3cd76c757ba1337679392')
    version('1.0.4',      sha256='7d12a1d8b1c490502cd73737e1ce264880b04e74c16ee3b27cabad371c5b9e73')
    version('1.0.3',      sha256='74b0e7a690b8fe81eb2e2ea78f96cb75aadca1c8b08450e89a7ebf8963a4d44c')
    version('1.0.2',      sha256='5f33b8ba75120918023be458d9fb0f138e1d41dd37ca7107d3aa6e0ab51b691c')
    version('1.0.1',      sha256='60b4222e41c6cf5c9cbb30c85e388ce06f1e585c5a970d34ef4d1394c058ccdc')
    version('1.0.0',      sha256='be994c94b5b665f3802723a51e5983a0d9221ca3b13138146d68ba48eb0b2d93')

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
