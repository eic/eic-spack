# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Geant3Vmc(CMakePackage):
    """Geometry and Tracking."""

    homepage = "https://github.com/vmc-project/geant3"
    url = "https://github.com/vmc-project/geant3/archive/v3-4.tar.gz"
    list_url = "https://github.com/vmc-project/geant3/releases"
    git = "https://github.com/vmc-project/geant3.git"

    maintainer = ["wdconinc"]

    tags = ["eic"]

    version("master", branch="master")
    version(
        "3-8", sha256="6ff6745eef59139d791bef043b405f6d515be1d98096cf4e82ac4c1f61f737dc"
    )
    version(
        "3-7", sha256="36cd57c6e5a54ff11e8687b30f54d774b676e06c55658cbc1ad787d1fadbe509"
    )
    version(
        "3-6", sha256="e2c8f2c8397431218f90e03cafe54aa0de0474536cb9de921573ca670abfd0e0"
    )
    version(
        "3-5", sha256="5bec0b442bbb3456d5cd1751ac9f90f1da48df0fcb7f6bf0a86c566bfc408261"
    )
    version(
        "3-4", sha256="c7b487ab4fb4e6479c652b9b11dcafb686edf35e2f2048045c501e4f5597d62c"
    )
    version(
        "3-3", sha256="d33098594c4dd41addcdc6bcac5c7ade962a41a3eb6fae49069a4fc91f7c8e06"
    )
    version(
        "3-2", sha256="e63810f82fd63f480c16563becb1f58afa66b3c7011875d4b648134349884fa8"
    )
    version(
        "3-1", sha256="9316cfe2fac05885a83ac0910b7818d2c66343e5e2b897c149c1226c20049f12"
    )
    version(
        "3-0", sha256="1cb39bd54541ad928788b3c7f3ae07f0ab5d0b7a2ec9ea010d697d5785871855"
    )
    version(
        "2-7-p2",
        sha256="bbc9c4c63947b59c8d572391034b68efa5f094aa3a4a685726485b5688e64be1",
    )
    version(
        "2-7-p1",
        sha256="969fa0d522aadd6e9c25ccb198da4bbed02d7655619e03c524ce05571d9367d4",
    )
    version(
        "2-7", sha256="102c15e0bb5be43049456a91839cc2f166d85a6040038d9794cf57ce47387b55"
    )
    version(
        "2-6", sha256="c2e30fed0f36d5cda88a060bea9a490861eb5a02506b67d7067685b94d84b3d0"
    )
    version(
        "2-5", sha256="453ccbc9f5f66f70d0dd92f60f7473a670fa8d75704beaeb776d178c9abe9171"
    )
    version(
        "2-4", sha256="c4619ee404cf3e9ca9c0dde51722184268edd7df1d868533278a9c16a67a8715"
    )

    depends_on("root")
    depends_on("vmc")

    def setup_build_environment(self, env):
        if self.spec.satisfies("@:3-6 %gcc@10:"):
            env.append_flags("FFLAGS", "-fallow-invalid-boz")

    def cmake_args(self):
        args = []
        args.append("-DROOT_DIR={0}".format(self.spec["root"].prefix))
        return args
