# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Dire(Package):
    """Simulating radiation cascades for particle physics."""

    homepage = "http://dire.gitlab.io/"
    url      = "http://dire.gitlab.io/Downloads/DIRE-2.004.tar.gz"
    git      = "http://gitlab.com/dire/direforpythia"
    list_url = "http://dire.gitlab.io/Downloads.html"

    version('2.004',             sha256='8cc1213b58fec744fdaa50834560a14b141de99efb2c3e3d3d47f3d6d84b179f')
    version('2.003',             sha256='98ee082718504c0f514a5c377310c4a2a34bb9625c999d3690d92342e52b532a')
    version('2.002',             sha256='7fba480bee785ddacd76446190df766d74e61a3c5969f362b8deace7d3fed8c1')
    version('2.001',             sha256='d9d5f8ff6829c51fefc008a78f4fa0ac3f4be99cd2a03ef01ca9fb84f4319836')
    version('2.000',             sha256='ce30477474709496d3c9a31806c12872fb003cdeec412ec4027245da6aa8b40b')
    version('1.500',             sha256='3b6e711a8b161e60f84168a3560bf71b3cf89f566f3b536631208e475fdc512f')
    version('0.900',             sha256='fd675cd96b79c9e98e886b1158c73587c05765f9bc599c87cfe7a8aef9513963')

    # FIXME openmp variant
    #variant('openmp')

    depends_on('zlib')
    depends_on('boost')
    depends_on('lhapdf')
    depends_on('hepmc@:2.06.10')
    depends_on('pythia8@8212:', when='@:2.000')
    depends_on('pythia8@8226:', when='@2.001:')

    def install(self, spec, prefix):
        configure("--prefix={0} --with-pythia8={1}".format(prefix,spec['pythia8'].prefix))
        make()
        make('install')
