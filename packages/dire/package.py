# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Dire(Package)
    """Simulating radiation cascades for particle physics."""

    homepage = "http://dire.gitlab.io/"
    url      = "https://dire.gitlab.io/Downloads/DIRE-2.004.tar.gz"
    git      = "http://gitlab.com/dire/direforpythia"

    version('2.004')
    version('2.003')
    version('2.002')
    version('2.001')
    version('2.000')
    version('1.500')
    version('0.900')

    depends_on('zlib')
    depends_on('boost')
    #depends_on('lhapdf6') # FIXME no package
    #depends_on('hepmc@2') # FIXME version check
    depends_on('pythia8@8.212:', when='@:2.000')
    depends_on('pythia8@8.226:', when='@2.001:')

    def install(self, spec, prefix):
        configure("--prefix={0} --with-pythia8={1}".format(prefix,spec['pythia8'].prefix))
        make()
        make('install')
