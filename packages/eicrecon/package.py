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

    tags = ["eic"]

    maintainers = ["wdconinc"]

    version("main", branch="main")
    version("1.19.0", sha256="db4cacba6f7c6818f15a0cfa83882a0ac3a8663dda28ee41c75adeeb6bd5425e")
    version("1.18.1", sha256="f4ca7e104fb8bfe960a7e339b67240d5885dcf248eb0bb6a5a81b928b2a58701")
    version("1.18.0", sha256="1110ba2bab25980c7ac843ffb07b00c9d5b30c270e5998d1cc755f2cc262ca5e")
    version("1.17.0", sha256="016b5e10f076e97d10d216a1952c9363d97f9b8f8fd8eb6a44fb49ed551d3eba")
    version("1.16.1", sha256="b0b98694f87c0b84fda5e3fe014e176e02881c5fb74a9e0bf1eb849d506a60c9")
    version("1.16.0", sha256="7296bf565ca787f7a4b538272c59a23e99469f8f2ed931698010def8169e9f6e")
    version("1.15.0", sha256="3a553bf9643828cd3b6e64c9324dc40b50c6c2cddb9ac618316afcc7529dc254")
    version("1.14.1", sha256="2a9445482d47b461ced8fcbaa8cf55903f4fec24d323b90b5fb3e9bc64c28f9e")
    version("1.14.0", sha256="f90e3a5bc55d7696f86a2b86cd38b585553b3e13bc0323ca4a2971688ecda58c")
    version("1.13.2", sha256="24ac2172b4834a2fa30ff13290e9c7c946f51472d57d4223711d2f86360eb926")
    version("1.13.1", sha256="66e9767e520ebcd6dc12f616d7a9e1262db0574e5b7e6a90df282ccd3e28612d")
    version("1.12.0", sha256="7b1fbf72a0756cd7338c179096c329b20611018b19e5fd73ce311e415adad47f")
    version("1.11.0", sha256="4442248864ed432762f267dc4d03eb1ddfecc3155d5b7c3d7f9a2dbc7b1427f7")
    version("1.10.0", sha256="f7469c5d62fd8614b1fb5a22be533d8fcc28ebdb955189f6b839caaac7a6be03")
    version("1.9.1", sha256="7d06d0fa14213525a06d5633b15d63d1c0827515a3e22f1e952e610cf90bb4d7")
    version("1.9.0", sha256="58c32f6953940277c4c01b563cac878b0aae01b09b88e7960d8500aa6080f745")
    version("1.8.1", sha256="7bc073d87fa6b619330bb3c1ce751e0535d04f9db3d04f13108b147759a29d6d")
    version("1.8.0", sha256="f0769d816e4119322e5429db9b9262ecb3cf8b140fa9f07707a6cdf5c77d0832")
    version("1.7.0", sha256="60732169f76d215ad111a9b34affb64b0f1adafa4aba372b53acb39fe50c6b07")
    version(
        "1.6.2",
        sha256="725d53bc4527486fd15d600b1bd329228502ef83c0ff118cc4600eac7cc2d148",
    )
    version(
        "1.6.1",
        sha256="fb3cffe9882d912288d40fcb0dc08a24bbe8adf57a53f05a7ab3559baa4c30cb",
    )
    version(
        "1.6.0",
        sha256="f099e4ad400b617f597ca7e1869b9fc5fb2ec6ab13af7dd66972b16ae194106d",
    )
    version(
        "1.5.1",
        sha256="3e77b6fc5dfa269f782bb8b3e33112f3cb7c7be9459a8efa6996c189463fad6e",
    )
    version(
        "1.5.0",
        sha256="b91339f39747ebda4e52a0e9d65e3af36e0e5d626335120dd73afe7a1bf0af62",
    )
    version(
        "1.4.1",
        sha256="3587fe257d8dcb6aa16a90ea6ab23a62b0894671fa91531a084611006719b234",
    )
    version(
        "1.4.0",
        sha256="714d5556499bbc067682970168fdd5e7a1b9ea3895f8153451032c5933747019",
    )
    version(
        "1.3.2",
        sha256="3abf080f8eb416ca6963ef9a1c5a039727119eea80d4eed2cceb8af3446bf9a2",
    )
    version(
        "1.3.1",
        sha256="e2acf781f34990f3602a078a65127b846f90a54dfbdbbdb63349931ed19e161e",
    )
    version(
        "1.3.0",
        sha256="b000c9f1f482b82c6a8b8f9daa5e7d4ce8c350fe09380f708d4c4077e22442bb",
    )
    version(
        "1.2.1",
        sha256="6a3ef0115a40369fc70c11218bccc957196730554f7ccf59da70e3dcdb12dcb9",
    )
    version(
        "1.2.0",
        sha256="89b1226248bca10ecb1677e065ffceae71921be0685988d66a0b7a0a13dbbbb3",
    )
    version(
        "1.1.1",
        sha256="05b7488481a6614b3a933786badd7b8f5eba97023047e35f63098ace427f5219",
    )
    version(
        "1.1.0",
        sha256="16bae53095bdf485824a6ff4b186b3f4435a21efd6ee3342604c0515cbf3ed4f",
    )
    version(
        "1.0.0",
        sha256="f7616b39150378ad8697e1b797edddce2f91181d1105b00b1dd66d618100c632",
    )
    version(
        "0.6.3",
        sha256="bd0bb106c4951fc472100538e6624eae1c9b568de4a2f35606b82f3bf462d0a2",
    )
    version(
        "0.6.2",
        sha256="47a0047f340f8c8384c01a97c69d85569084ce1b43941eabe69bd46e1dd4dadd",
    )
    version(
        "0.6.1",
        sha256="a1ec19101cb283d8af06c9236a069a6a9652bbd480be43f59a9612319567897b",
    )
    version(
        "0.6.0",
        sha256="498585c4ed5a4f5e8371bcb14971278aa2d5dce1d6fa15f03bb49164594ecaa6",
    )
    version(
        "0.5.4",
        sha256="79f4618ac2de44a876a13196790c9ce9d6e26bade4e71b44385cff321dedf18d",
    )
    version(
        "0.5.3",
        sha256="722988227f3b9f42932ee246a4bf28478d1221aa534e47eee1638c2a23198ebb",
    )
    version(
        "0.5.2",
        sha256="1a449ac1d93da6c85b52f2f1ff2f1d71034a00a437e48b261878a2380f3c7b33",
    )
    version(
        "0.5.1",
        sha256="546f4ceb05b957a5189ef1ccb3ff20f73c794a9e5d8f2b34eaa3ce8bfeade154",
    )
    version(
        "0.5.0",
        sha256="741836e51949168f1a542a3a1bb15735c54d997de158e1ef4adcf6ef12bfa269",
    )
    version(
        "0.4.2",
        sha256="ffc2ccee5a4634af10719966b41d464e95c67447efa79def4745472e8407ddc0",
    )
    version(
        "0.4.1",
        sha256="2653d381ebf5edfbe2bd9c962017685408001ca01fb296f62643c2d9645a1f1d",
    )
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

    depends_on("acts +dd4hep +identification +tgeo", when="@:1.15")
    depends_on("acts +dd4hep +json", when="@1.16:")
    depends_on("acts@30:", when="@1.8:")
    depends_on("acts@:30", when="@:1.9.0")

    depends_on("root")
    depends_on("fastjet")
    depends_on("fjcontrib", when="@1.13:")
    depends_on("fmt")
    depends_on("irt", when="@0.2.8:")
    depends_on("spdlog")
    depends_on("catch2", when="@1.0.0:")
    depends_on("cppgsl", when="@1.7:")
    depends_on("algorithms", when="@1.7:")
    depends_on("py-onnxruntime", when="@1.13:")

    def cmake_flags(self):
        return [f"-DVERSION={self.version}"]
    
    def setup_run_environment(self, env):
        env.prepend_path(
            "JANA_PLUGIN_PATH", join_path(self.prefix, "lib", "EICrecon", "plugins")
        )
