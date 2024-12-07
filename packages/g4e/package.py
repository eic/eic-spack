# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class G4e(CMakePackage):
    """Geant for EIC."""

    homepage = "https://g4e.readthedocs.io/en/latest/"
    url = "https://gitlab.com/eic/escalate/g4e/-/archive/v1.3.2/g4e-v1.3.2.tar.gz"
    git = "https://gitlab.com/eic/escalate/g4e.git"
    list_url = "https://gitlab.com/eic/escalate/g4e/-/tags"

    maintainer = ["DraTeots"]

    tags = ["eic"]

    version("master", branch="master")
    version(
        "1.4.2",
        sha256="252928a819541fdffc70e522f5cf9160ed219f7be02d9dcd507ae958e9d376b3",
    )
    version(
        "1.4.1",
        sha256="2986100c30b061c267306fb73e5709b28609ee00ec686b2c1de3398acbc9ccd6",
    )
    version(
        "1.3.8",
        sha256="451dee2ae8e1f0824d4f0ed7672aaad5e2b76dd3a5a95e38f2820eb51ec216c6",
    )
    version(
        "1.3.7",
        sha256="98f5387f8169ec922a162d6073544c231e3989fe7a8e5cc2e3582cbc8f312095",
    )
    version(
        "1.3.6",
        sha256="051ce2b1ff87df314a6395c22b33da19e1555caddd94d3863687101cdafad72b",
    )
    version(
        "1.3.5",
        sha256="e92d95df4b873bff3dff9fcff8a5535410a19004ae00c4a166f3adab8bd90279",
    )
    version(
        "1.3.4",
        sha256="9958a08a7cb8a8ce8b44d96e5e3c9b0bf45b2cb7bb9736f73a00cd907b73ffc8",
    )
    version(
        "1.3.2",
        sha256="bf0c035e6e213d71aafd5851e35210f2c70742b82b7d3222b2f2fdf05c09c8f8",
    )
    version(
        "1.3.1",
        sha256="98afe3c3efe3dbad5b13b6d33964c600155a8a6684786a81181a987c0a358f50",
    )

    # This compatibility variant allows to use g4e with older root and geant versions
    variant(
        "validated",
        default=False,
        description="Validated working version with fixed dependencies",
    )

    depends_on("cxx", type="build")
    depends_on("cmake@3.0.0:", type="build", when="~validated")
    depends_on("root@6.00.00:", when="~validated")
    depends_on("geant4@10.6:", when="~validated")
    depends_on("vgm@4-7:", when="~validated")
    depends_on("hepmc@2.06:", when="~validated")
    depends_on("python", when="~validated")

    # This uses the latest versions consistent over escalate
    depends_on("cmake@3.0.0:", type="build", when="+validated")
    depends_on(
        "root@6.20.04 +vmc +pythia6 +pythia8 +root7 cxxstd=17", when="+validated"
    )
    depends_on("geant4@10.6.2 +opengl +python +qt cxxstd=17", when="+validated")
    depends_on("vgm@4-8", when="+validated")
    depends_on("hepmc@2.06.10", when="+validated")

    def cmake_args(self):
        args = []
        # >oO debug: from ppretty import ppretty
        # >oO debug: print(ppretty(self, seq_length=20))

        args.append(
            "-DCMAKE_CXX_STANDARD={}".format(self.spec["root"].variants["cxxstd"].value)
        )
        args.append("-DGEANT4_DIR={0}".format(self.spec["geant4"].prefix))
        args.append("-DVGM_DIRECTORY={0}".format(self.spec["vgm"].prefix))
        args.append("-DHEPMC_DIRECTORY={0}".format(self.spec["hepmc"].prefix))
        args.append("-DCERN_ROOT_DIRECTORY={0}".format(self.spec["root"].prefix))

        return args

    def setup_run_environment(self, env):
        env.append_path("G4E_MACRO_PATH", self.prefix)
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.set("G4E_HOME", self.prefix)
