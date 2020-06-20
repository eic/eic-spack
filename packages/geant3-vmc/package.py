# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Geant3Vmc(CMakePackage):
    """Geometry and Tracking."""

    homepage = "https://root.cern.ch/installing-geant3"
    url      = "https://github.com/vmc-project/geant3/archive/v3-4.tar.gz"

    version('3-4',    sha256='c7b487ab4fb4e6479c652b9b11dcafb686edf35e2f2048045c501e4f5597d62c')
    version('3-3',    sha256='d33098594c4dd41addcdc6bcac5c7ade962a41a3eb6fae49069a4fc91f7c8e06')
    version('3-2',    sha256='e63810f82fd63f480c16563becb1f58afa66b3c7011875d4b648134349884fa8')
    version('3-1',    sha256='9316cfe2fac05885a83ac0910b7818d2c66343e5e2b897c149c1226c20049f12')
    version('3-0',    sha256='1cb39bd54541ad928788b3c7f3ae07f0ab5d0b7a2ec9ea010d697d5785871855')
    version('2-7-p1', sha256='969fa0d522aadd6e9c25ccb198da4bbed02d7655619e03c524ce05571d9367d4')
    version('2-7',    sha256='102c15e0bb5be43049456a91839cc2f166d85a6040038d9794cf57ce47387b55')
    version('2-6',    sha256='c2e30fed0f36d5cda88a060bea9a490861eb5a02506b67d7067685b94d84b3d0')
    version('2-5',    sha256='453ccbc9f5f66f70d0dd92f60f7473a670fa8d75704beaeb776d178c9abe9171')
    version('2-4',    sha256='c4619ee404cf3e9ca9c0dde51722184268edd7df1d868533278a9c16a67a8715')

    depends_on("root")

    def cmake_args(self):
        args = []
        args.append('-DROOT_DIR={0}'.format(
            self.spec['root'].prefix))
        return args
