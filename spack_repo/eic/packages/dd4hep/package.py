from spack_repo.builtin.packages.dd4hep.package import Dd4hep as BuiltinDd4hep

from spack.package import *


class Dd4hep(BuiltinDd4hep):
    __doc__ = BuiltinDd4hep.__doc__

    version("1.32.1", sha256="f47fbede967b609e142c3116d23b4993f9d57fbae28a1739b5333503bc498883")
    version("1.32", sha256="8bde4eab9af9841e040447282ea7df3a16e4bcec587c3a1e32f41987da9b1b4d")

    variant("g4hepem", default=True, description="Build G4HepEm plugin", when="@1.36: +ddg4")
    variant("frames", default=True, description="Use podio frames", when="@1.25.1")
    variant("frames", default=True, description="Use podio frames", when="@1.24")

    depends_on("g4hepem", when="+g4hepem")

    # G4HepEm plugin, https://github.com/AIDASoft/DD4hep/pull/1641
    patch(
        "https://github.com/eic/DD4hep/compare/b6b45d502d0e24cf0d3f9c18bc1b6079c43bbe87...940a469142c90ecd95d673b777dd8b89789dc63e.patch?full_index=1",
        sha256="4c3137d80c96b00e3f26da52d9f65c597e92069c94fde3a9efeedf5ce225e43c",
        when="@1.36:1.37"
    )
    patch("Geant4TVUserParticleHandler_compatibility_notice.patch", when="@1.30:")
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1574.diff?full_index=1",
        sha256="f6e099bcf43c7e711f78fc17e9e4db31afe1a642099e814afb54faf436142357",
        when="@=1.35",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1598.diff?full_index=1",
        sha256="2f2c1790431eb9947d652576c56c698e9051d1fdc8f3da9ffb758c8c0b1c3da0",
        when="@=1.35",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1566.diff?full_index=1",
        sha256="190ddf3e8538d7194589556ed7e455503bf93374cd98a2f077f920b5d2f2762c",
        when="@=1.35",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1540.diff?full_index=1",
        sha256="c3babcb1fe3ebe8520f2cd8c218dd2726563ab0450e6d623de17f6eecbe2038c",
        when="@:1.34",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1495.diff?full_index=1",
        sha256="e9de70d2c4702147c769da7dc729ec78e0bd0858af9a2d3eb68310667fa21c02",
        when="@:1.32.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1476.diff?full_index=1",
        sha256="d72251d248f657e28e3138cf38cf70d865db78611fa5d4826ea399c7ab419a6d",
        when="@1.31:1.32.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1471.diff?full_index=1",
        sha256="6e294a17df753944c2db91729967d82f4f215efa627a50b98c098ac3e2f6e5bc",
        when="@1.31:1.32.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1449.diff?full_index=1",
        sha256="15f24738f223add8c4d4376c771863cac4b476d1779811f8020a2533ad9890e6",
        when="@1.20:1.32.0",
    )
    patch("DDCorePlugins-install-headers.patch", when="@1.26:")
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1365.diff?full_index=1",
        sha256="fe28edb4059647e4f18141d08f7ba8470b5e99dc03048d4faf404170285d89fd",
        when="@=1.30",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1294.diff?full_index=1",
        sha256="252579cceb1f66edc20e4e14b3390d2b8ec231450aad0f9e1d3c585e34284a1c",
        when="@=1.29",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1283.diff?full_index=1",
        sha256="40124c528c68b4056d3c5af536683ed9f2f9e9bfa750d41e50471895aa58fc4b",
        when="@=1.29",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1190.diff?full_index=1",
        sha256="d6273e4f0367f72b9572b337338d1269a154b948b72f31ff69ad62f850e0d4ac",
        when="@=1.27",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/commit/1c79b1492373dd66b17ea2530a63ec434396afa9.patch?full_index=1",
        sha256="626243986fdc253aad275ef2dc8a41bc90a20670a7e384e20471e5238e6a5481",
        when="@=1.26",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/commit/fecf99a2732a3f6aafc5fbf0f4a05af5bac196f8.patch?full_index=1",
        sha256="fc9863a471d939484ab9b0088b5f13ef9f073479702e7c94352db0c3dcd4518c",
        when="@=1.26",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/commit/0cdf506db8a9f47698129b5c8f52b66f53429818.patch?full_index=1",
        sha256="8d392e1529c3f024fee0d2823f9511f514639b914d567bbdd4638f92cc44e7e6",
        when="@=1.26",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1161.diff?full_index=1",
        sha256="4139360e84eb220f2067b85f2dc477b4cd179fb98d7e117a98f43b1fa0baa395",
        when="@=1.26",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1170.diff?full_index=1",
        sha256="dc6985f7f92cb2292b18cb5b7059226c475d3c930f834c40b49e415bbd7a2946",
        when="@=1.26",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1086.patch?full_index=1",
        sha256="6b049415e2c6989f3927ff2c56e4764de1650cad6ed301d8ac0f047f4e0039c5",
        when="@1.24:1.25.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/compare/f4c63132f509f80e7c81a624cdf46e024131cf2a..3c6ede06ea338e3ea6a01b664fb16089ac4548e5.patch?full_index=1",
        sha256="abefeb866a42baca653ea4329c984e19aeab349e5c610bf38a495083379f9ec5",
        when="@1.24",
    )
    patch(
        "revert-Geant4Output2EDM4hep-dd4hep-1-25-1-to-1-23.patch",
        sha256="1958c7951ed53538631ae6bc0d6663ea092e19f63367ed0fe1ab2bb00ddf4903",
        when="@1.25.1 -frames",
    )
    patch(
        "revert-Geant4Output2EDM4hep-dd4hep-1-24-to-1-23.patch",
        sha256="1c5697eabab65d4c2d49d710c14a33673e92b0349ed8299041c9da2d7878831b",
        when="@1.24 -frames",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1066.patch?full_index=1",
        sha256="c6df47768279c65f6a9d3cee57b038f37cb35c845deef22476876ea607ff14a1",
        when="@1.25.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1068.patch?full_index=1",
        sha256="401a349435ca6673a2817c32c39e2fa73ca17241fb2bf3f836c110a2f1c90431",
        when="@1.24:1.25.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1070.patch?full_index=1",
        sha256="d84db1f3a8eb3e8b9398db9aab3753569855bc5753f9f15faf62bfdbe28f8f5c",
        when="@1.24:1.25.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1071.patch?full_index=1",
        sha256="8a71caf957a4b0ecb05a2fc5e39265e79e0af0d98e89b75406957815442c7b30",
        when="@1.25.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1074.patch?full_index=1",
        sha256="1c0737cc941995c4f28591ac34b5007e8b3b23f7d54251d8db277e9aff8da411",
        when="@1.25.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1080.patch?full_index=1",
        sha256="2dde47795f8534fcbfb9454b3b729a5a758e2dc90b6bd9f5f8bdc8940e2da0f7",
        when="@1.25.1",
    )

    @when("@1.25.1")
    def setup_run_environment(self, env):
        super().setup_run_environment(env)
        env.set("CXXFLAGS", "-DDD4HEP_FIELD_TYPE_OVERRIDE=field_type")

    @when("@1.25.1")
    def setup_dependent_build_environment(self, env, dependent_spec):
        super().setup_dependent_build_environment(env, dependent_spec)
        env.set("CXXFLAGS", "-DDD4HEP_FIELD_TYPE_OVERRIDE=field_type")

    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1081.patch?full_index=1",
        sha256="07522f7fac0fc38513cb08b663ef7425936e940c55f277eb2112916b194f5a68",
        when="@1.25.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1105.patch?full_index=1",
        sha256="bcfa71a74368034818ff4810cd5738a13fc56d1d49742b19abe7397de1531596",
        when="@1.19:1.25.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1106.patch?full_index=1",
        sha256="5a0ed96babc56d01663f157e50455a746bba63a4a7f27779325fa5e097cf7bb5",
        when="@:1.25.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1142.patch?full_index=1",
        sha256="12bca1354871caad6f6d86710ad926a44d3a8e4090f15b41e98a5c09faabf0de",
        when="@:1.25.1",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/commit/8693a29669d03dec5e06b61e6df7cc0df1e0aa5c.patch?full_index=1",
        sha256="2d3c94c74e8af9d885aedbc3ff8ee5339154f2dfbd41dc550c81fff5b043d08e",
        when="@1.21:1.22",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/983.patch?full_index=1",
        sha256="969fbdd9a35a07fe91d6376517621d3ddba28f13668d139fd9405052e3e6f1a6",
        when="@:1.23",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/989.patch?full_index=1",
        sha256="b29bec9faac4461f799f0ed12b85bf929ae4126fbf591fa8e2cca51fffae12e7",
        when="@1.23",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1011.patch?full_index=1",
        sha256="15f4b9cc6e36aea836191b2154c0609a1ab55f085a0836609dfca804cbe78c6d",
        when="@1.23",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1017.patch?full_index=1",
        sha256="66aa2be073a58cdc3c3cb912c2dcf943c65b4e7af91ebe7bb1479827433380b7",
        when="@1.23",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1357.patch?full_index=1",
        sha256="3858ac2bb558e410db994d4b42b68012d17fe83ae2247cb70bb5460009e2ae4d",
        when="@:1.30.1",
    )

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define_from_variant("DD4HEP_USE_G4HEPEM", "g4hepem"))
        return args
