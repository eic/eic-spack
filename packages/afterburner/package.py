# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Afterburner(CMakePackage):
    """An EIC Monte Carlo Afterburner for beam effects."""

    homepage = "https://eicweb.phy.anl.gov/monte_carlo/afterburner"
    url      = "https://eicweb.phy.anl.gov/monte_carlo/afterburner/-/archive/v0.0.1/afterburner-v0.0.1.tar.gz"
    list_url = "https://eicweb.phy.anl.gov/monte_carlo/afterburner/-/tags"
    git      = "https://eicweb.phy.anl.gov/monte_carlo/afterburner"

    maintainers = ['wdconinc', 'DraTeots']

    tags = ['eic']

    version('main', branch='main')
    version('0.1.2', sha256='dc0396b9494c9460ee2b62b9934f57c74d850f4eb92c9af47f60849de1a2e7aa')
    version('0.1.1', sha256='a77255b24a253b9f00a4335f9080ab2af05c30ee8f3ccad7e1deea12cf1d0d22')
    version('0.1.0', sha256='fa6d2778ebf16ba8d21e30d86ac0500d4729d218feb1b47432eb848bc0206757')
    version('0.0.2', sha256='76cdd518c99f6d66d712b483e72ef8eb810635533441e126968961eabce53ea6')
    version('0.0.1', sha256='58074f917bbe8b007d08c80190b9087b1705136b99abbbed6ebf285656b3e5cf')

    variant('root', default=False, description='Support reading ROOT files')
    variant('zlib', default=True, description='Support reading compressed files')

    depends_on('gsl')
    depends_on('hepmc3')
    depends_on('clhep')
    depends_on('yaml-cpp')
    depends_on('root', when='+root')
    depends_on('zlib', when='+zlib')

    root_cmakelists_dir = 'cpp'

    def patch(self):
        filter_file(
            r'add_subdirectory\(test\)',
            '#add_subdirectory(test)',
            'cpp/CMakeLists.txt')
        filter_file(
            r'enable_testing\(\)',
            '#enable_testing()',
            'cpp/CMakeLists.txt')

    def cmake_args(self):
        if '+root' in self.spec:
            cxxstd = self.spec['root'].variants['cxxstd'].value
        else:
            cxxstd = '11'
        args = [
            self.define("CMAKE_CXX_STANDARD", cxxstd)
        ]
        return args
