# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Lhapdf(Package):
    """General purpose C++ interpolator, used for evaluating PDFs from discretised data file."""

    homepage = "http://lhapdf.hepforge.org/"
    url      = "http://gitlab.com/hepcedar/lhapdf/-/archive/lhapdf-6.2.3/lhapdf-lhapdf-6.2.3.tar.gz"
    git      = "http://gitlab.com/hepcedar/lhapdf/"

    version('6.2.3', sha256='37200a1ab70247250a141dfed7419d178f9a83bd23a4f8a38e203d4e27b41308')
    version('6.2.2', sha256='f20e1df02cf1ef8168d4228306911a7f6123f389046e734aa2cfc37382af0101')
    version('6.2.1', sha256='7910704066339b26c30ecfeafaaf296847d8c55c7b0ac0fc3b30c9e172de962b')
    version('6.2.0', sha256='633c6a987ab4d889e37dd8359f73a969004488158a9f608d39472757acba5c13')
    version('6.1.6', sha256='a45f73c95e0b25bb9d512ba3f195ff3cd0bc2a13841d02671a8ecc023fb99ff6')
    version('6.1.5', sha256='32b8be85ad1a859e8faed09aec36ca8c1df785ce2be86e9d0eb6d8b545d5ceb0')
    version('6.1.4', sha256='25e395730b5708f8a2a3ae8102ed4b295549c22dfc2346a35543b06247d1c3bf')
    version('6.1.3', sha256='d9cdfd8b8f021fdf84dd65a6b76d5aa30d52f83b651a3e34d1888f8872c8dc40')
    version('6.1.2', sha256='628582a35a8c3c6a6f941244ee0c9a1b338e468e103e6ae57f04c6647fcf58b2')
    version('6.1.1', sha256='520d9c92f0bfd82b52efc8f9c4ed9fe01df1a18a8735a47e10284fc5dd7542d7')
    version('6.1.0', sha256='338eb4843b4e9531a7a8410617e62bb5d536050b110020025f8032886a098200')
    version('6.0.5', sha256='50f654614b311e660a51f71fa81de618f20e667fe1c8c03d34d31e3c5fbaeef7')
    version('6.0.4', sha256='9223a1cfbbe06c3787d763726bdccce7d49051fc9273e424684ea08bcc16c66b')
    version('6.0.3', sha256='8ade0037aeb10d43011625aa85469d2056acfb2f2d5bf24e32724fa979775bcf')
    version('6.0.2', sha256='d4149256c129180850ea52a78c00c21be269aa529e48bb694665b64e8fc37455')
    version('6.0.1', sha256='76df27190f49619f7d8238ed6a1f1f25c430e58da42ddf765b7972f20eaf93f7')
    version('6.0.0', sha256='4e03abade212f817f6e34c9089626988fb65f94358833ac8035a0eb409b29aa5')

    def install(self, spec, prefix):
        configure('--prefix={0}'.format(prefix))
        make()
        make('install')
