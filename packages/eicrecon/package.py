# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Eicrecon(CMakePackage):
    """EIC Reconstruction - JANA based."""

    homepage = "https://github.com/eic/eicrecon"
    url = "https://github.com/eic/EICrecon/archive/refs/tags/v0.1.0.zip"
    git = "https://github.com/eic/eicrecon.git"
    list_url = "https://github.com/eic/EICrecon/tags"

    maintainers = ["wdconinc"]

    version("main", branch="main")
    version(
        "0.4.0",
        sha256="0b7e2cef2427110151b76711bc0e02aa44cfce055f96507bad64561206ccb4de",
    )
    version(
        "0.3.7",
        sha256="6499661af54703b280410b4bd71324aea756379fca269eaed53f047d1acb0475",
    )
    version(
        "0.3.6.2",
        sha256="a6a3e12a8fc98355b8a469d5fb5d789839bdbb0e403e376e00ffee7fa5603341",
    )
    version(
        "0.3.6.1",
        sha256="bc38b1b354dd9fbe97e98ddd4bc677aee6173121240df77ade8db1f680eb82a4",
    )
    version(
        "0.3.6",
        sha256="dac1ad140d0f9cd7d86e7df3fb2160f430b7971b20339281658b86c4450321d9",
    )
    version(
        "0.3.5",
        sha256="59ab7f3dda714dcea461c60cc60ab47825c3f91729de0f4f390898b934bfb09b",
    )
    version(
        "0.3.4",
        sha256="00f8dd172f8ddf5a1c7630eccf0e70a3efc43429c873f7d05918735fb526a3d5",
    )
    version(
        "0.3.3",
        sha256="a5a4ca7b36c132ccd4c3505c083b48d701dd0c487e57fb19d839d99b8cec362f",
    )
    version(
        "0.3.2",
        sha256="e89d64181c3b988e920df99e97d433365f865f1063561d0098f2ccfd13c5f5f5",
    )
    version(
        "0.3.1",
        sha256="3c153f8fbf06212b55a15cd34243bd9712e344163781bbbf8504d1a0a435646b",
    )
    version(
        "0.3.0",
        sha256="2efe99ea82c6f93cab1d9db32243c5c4138a3e32e7c051c1a206de9d59dd58d9",
    )
    version(
        "0.2.8",
        sha256="6c64f845566dc7b1cecaf4250193495256dce9f5c6a6d2742c35ce7fa882ba11",
    )
    version(
        "0.2.7",
        sha256="afcb8addea452c610b7ab1e5bfc179e062de0f1407605a7ae36b68bc55a2bc3a",
    )
    version(
        "0.2.6",
        sha256="819982d86cfb6f51661eb113af7eba337adda8d694cabfcd79dfc7f794f73226",
    )
    version(
        "0.2.5",
        sha256="c87970284130590049e4b40ad595fceab31daf22143e7e1afb08836b8c68170c",
    )
    version(
        "0.2.4",
        sha256="d8c55f54767f783eea8bf4939ef837fc73373ed71bd1509fdd5ae46aca4d8fa5",
    )
    version(
        "0.2.3",
        sha256="2660cb18272a932555ee1f690bcd904335feb1a6d8969859834307b24a937fd0",
    )
    version(
        "0.2.2",
        sha256="de8e5ef71465027226debfe4d42b8a4f883ffcb03ce2bfee0a0d247a4a1e89f2",
    )
    version(
        "0.2.1",
        sha256="097fef82cacd45453770f30e7e0ae382a11660b8bd4dfe478e7488a8988b8816",
    )
    version(
        "0.2.0",
        sha256="3fc0b812637d6bca9587cb4dadcd4b2ca386458ff6d46551ed8cf291335b4780",
    )
    version(
        "0.1.0",
        sha256="dcc8b60530a627c825413c07472659ba155600339ef8b8e742e3c997bcc504ae",
    )

    depends_on("cmake@3.16:", type="build")

    depends_on("jana2 +root +zmq")
    depends_on("dd4hep +ddrec +edm4hep")
    depends_on("edm4eic")
    depends_on("edm4hep")
    depends_on("podio")
    depends_on("acts +dd4hep +identification +tgeo")
    depends_on("root")
    depends_on("fmt")
    depends_on("irt", when="@0.2.8:")
    depends_on("spdlog")

    def setup_run_environment(self, env):
        env.prepend_path(
            "JANA_PLUGIN_PATH", join_path(self.prefix, "lib", "EICrecon", "plugins")
        )
