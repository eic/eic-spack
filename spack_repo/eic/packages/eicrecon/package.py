# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

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
    version("1.37.0", sha256="a17617726718b7eb9c71862427f3685c7f9aaf5387539d7c4f426e09b07716a6")
    version("1.36.1", sha256="c5bc6344ee19a6d8826d8b4ec9879812f10204f945de0f582ebe7db3d7c12d70")
    version("1.36.0", sha256="5d31d142805d4d6d4568cb0a5d00be220979a51666e1ba4c531694bd8830f492")
    version("1.35.2", sha256="f03059a60756ad61d885eb350a57a339890c39fd0471a9f777db47bd6057df34")
    version("1.35.1", sha256="11a6eed2e20d64359b726cade4003deec3f51eb906ef1a5fe323b1caacf1c105")
    version("1.35.0", sha256="dbecf22f8a95d1af1932d8e53ffdc251e73db0a430af6f254375f5c54b531749")
    version("1.34.0", sha256="2c5910faec93543c67c4ff4605bff1e24bf6b496633b56d608d9c8fcbc230d36")
    version("1.33.1", sha256="c9fdb32e4be2a15558d7a8bc7d973665a2c349c974fc7aaf984302ee3baaeab8")
    version("1.33.0", sha256="bf87745da1ff237b7ffbef476358cc0230ba016378e7b6242abca45846bdef52")
    version("1.32.0", sha256="47ccd336984b0c01a43ca60859b0760b6576a045be0cd6de95bfa9f95f1df42e")
    version("1.31.0", sha256="d417ce403bb631d20b14d9ea65ac9203a6d049bb234f631a8912eeebf679ea65")
    version("1.30.2", sha256="127a05a448b777aca9f73e047ac8cca054a46f59821743d2e39c2c8ea4e18533")
    version("1.30.1", sha256="2cdbe2b20a26e35f7db15ab003fa99fdb7b16f14037381ba8c77bfe34b849bba")
    version("1.30.0", sha256="72b7af4521d83f454650a096b53936e795ca8292f7268100d392a217ec84e809")
    version("1.29.1", sha256="41999a3be2234a0d84f9b7b68fa34830b40845346cebb0f4e4121c8f6d006e56")
    version("1.29.0", sha256="434d64d61e4d497fbfca8f338f0345f831aae8dbdfc5cbcaf42b2f014e185b9a")
    version("1.28.0", sha256="3dc35a7e5bf0f2f9fb60a95fcf4ce2a940428553eb07b55f243058c5d3cb39f2")
    version("1.27.1", sha256="2e09004d6a6b45da7125a749350be3bd1af6c152f25fe1c731f2f5b30f6aec07")
    version("1.27.0", sha256="073d76da7540f2c8432f76925d66b38778b2aec8e57264cb8562d456b760ed3d")
    version("1.26.1", sha256="68022617abcdd00eaa2d8db941ebf53e2f9bdd180ae1398995b1c98406f2f019")
    version("1.26.0", sha256="032e9051602c24bdcd2536b24f600a7a25268e1798fcfe1798ed8fa26538a379")
    version("1.25.0", sha256="ecef50842387c8fb25ea21faad474811ccc500290a38cd132f005684db09807e")
    version("1.24.2", sha256="19d6f0b81fdf631dbf1f9a73e798079a3a40ff7bfed5b25c2f3656cb8bc5aaeb")
    version("1.24.1", sha256="910d5098cc7c49c30656a53df241183b9f10b0bc1352472fca9dd803b1774cb2")
    version("1.24.0", sha256="c38a947b71be7de31d2148afdcacdfe13c112d693ecf6005d22e29bf41eb4137")
    version("1.23.1", sha256="952f1397af8c8555b67c7e34a0fc2641f836dfa92f050a2498c3b24b663b6e07")
    version("1.23.0", sha256="2ffabcc1ea16dfd9ef9f81304b19cd756d5ac65349b97ba4c595e25ff49ebb99")
    version("1.22.0", sha256="3206fd194d810a1f57ce378442ee9c9fae330cda8070777cb6db25f2f2145acf")
    version("1.21.0", sha256="4ef7b7144728019a5d7564067da8ac86d30347e6c4ff420efd58076e112bdde2")
    version("1.20.0", sha256="e0f87635330d7ab3abf5f2c39e26d4ef2cb428a7fe4e10ea712936de7712e394")
    version("1.19.0", sha256="db4cacba6f7c6818f15a0cfa83882a0ac3a8663dda28ee41c75adeeb6bd5425e")
    version("1.18.1", sha256="f4ca7e104fb8bfe960a7e339b67240d5885dcf248eb0bb6a5a81b928b2a58701")
    version("1.18.0", sha256="1110ba2bab25980c7ac843ffb07b00c9d5b30c270e5998d1cc755f2cc262ca5e")
    version("1.17.0", sha256="016b5e10f076e97d10d216a1952c9363d97f9b8f8fd8eb6a44fb49ed551d3eba")
    version("1.16.1", sha256="b0b98694f87c0b84fda5e3fe014e176e02881c5fb74a9e0bf1eb849d506a60c9")
    version("1.16.0", sha256="7296bf565ca787f7a4b538272c59a23e99469f8f2ed931698010def8169e9f6e")

    variant("asan", default=False, description="Enable address sanitizer")
    variant("lsan", default=False, description="Enable leak sanitizer", when="+asan")
    variant("tsan", default=False, description="Enable thread sanitizer")
    variant("ubsan", default=False, description="Enable undefined behavior sanitizer")

    depends_on("cxx", type="build")
    depends_on("cmake@3.16:", type="build")

    depends_on("jana2 +podio +root +zmq")
    depends_on("dd4hep +ddrec +edm4hep")
    depends_on("edm4eic")
    depends_on("edm4hep")
    depends_on("podio")

    depends_on("acts +dd4hep +examples +json")
    depends_on("acts@30:")

    depends_on("root")
    depends_on("root +tmva", when="@1.14:1.36")
    depends_on("fastjet")
    depends_on("fjcontrib")
    depends_on("fmt")
    depends_on("irt")
    depends_on("irt2", when="@1.33.0:")
    depends_on("spdlog")
    depends_on("catch2")
    depends_on("cppgsl")
    depends_on("cppzmq", when="@1.37.0:")
    depends_on("algorithms")
    depends_on("py-onnxruntime")

    def cmake_args(self):
        return [
            self.define("VERSION", self.version),
            self.define_from_variant("USE_ASAN", "asan"),
            self.define_from_variant("USE_TSAN", "tsan"),
            self.define_from_variant("USE_UBSAN", "ubsan"),
        ]

    def setup_run_environment(self, env):
        env.prepend_path("JANA_PLUGIN_PATH", join_path(self.prefix, "lib", "EICrecon", "plugins"))

        if self.spec.satisfies("+asan"):
            env.set(
                "ASAN_OPTIONS",
                (
                    f"suppressions={self.prefix}/share/EICrecon/asan.supp:"
                    "malloc_context_size=20:detect_leaks=1:verify_asan_link_order=0:"
                    "detect_stack_use_after_return=1:detect_odr_violation=1:"
                    "new_delete_type_mismatch=0:intercept_tls_get_addr=0"
                ),
            )

        if self.spec.satisfies("+lsan"):
            env.set("LSAN_OPTIONS", (f"suppressions={self.prefix}/share/EICrecon/lsan.supp"))

        if self.spec.satisfies("+ubsan"):
            env.set(
                "UBSAN_OPTIONS",
                (
                    f"suppressions={self.prefix}/share/EICrecon/ubsan.supp:"
                    "print_stacktrace=1:silence_unsigned_overflow=1:"
                    "report_error_type=1"
                ),
            )
