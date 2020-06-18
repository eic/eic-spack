# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Lhapdf5(Package):
    """General purpose Fortran 77/90 interpolator, used for evaluating PDFs from discretised data files."""

    homepage = "https://lhapdf.hepforge.org/lhapdf5/"
    url      = "http://www.hepforge.org/archive/lhapdf/lhapdf-5.9.1.tar.gz"
    list_url = "https://lhapdf.hepforge.org/lhapdf5/"

    version('5.9.1', sha256='3ec36bab4a0c2a01082ebc9c2d74b75c16f266387773c262fcf5a39036ac4d70')
    version('5.9.1', sha256='134f31ad4c23b5a951db2543d8f360a0705af817ed5df4f0f6898ae377631fc4')
    version('5.9.0', sha256='3c694d7a02cb8b8cbfcb570be7d85315443596ec10665e37ebdee97c57d31cf4')
    version('5.8.9', sha256='30421428c280350b011d63cbb1acf97bd68f7c24ca2543edefae6167ed682702')
    version('5.8.8', sha256='65d00d2b69c62b8ca798e18b7ad9ad9c766ec7abf389281fde36bf10ca2fd16e')
    version('5.8.7', sha256='30dfddfbd63b007b4b3529ac347f984b7f14cb6f38bc46810b5803aa2c95e17f')
    version('5.8.6', sha256='ec336caebcd288712fe2aca1565e22060f4cbd83696f37c63ce22990e1f8413c')
    version('5.8.5', sha256='94168beabdb07acf3d7a6691e1eb51d4ee56d6484fdb807660c96ccf76c03a41')
    version('5.8.4', sha256='81f82234ce27389aa685bcce3ccdcdda18981905cae3cbba11da7597faca2266')
    version('5.8.3', sha256='0df68881ddf35264c619530068359bcd29141dad07ebdb59e3f2ea6ad9c75fa9')
    version('5.8.2', sha256='fbbafdaaf321a40c5a5513576689afb1e6a39bd61d9b55c2f6888ab114c98ee1')
    version('5.8.1', sha256='f4591178ce8ef64d69fdaf88d9fdfb988c73d23906f6c5eccd7d2a6eda5c4f12')
    version('5.8.0', sha256='220eb22d49203e18219f1ac2babc2a6a8542999fb96fce92f3f86192ab01d916')
    version('5.7.1', sha256='fa96046b2e9e6d3604f533875df69bdf26486281d012fd31b111de3b0ad53f74')

    depends_on('foo')

    def install(self, spec, prefix):
        configure("--prefix={0}".format(prefix))
        make()
        make('install')
