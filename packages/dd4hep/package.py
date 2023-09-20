from spack import *
from spack.pkg.builtin.dd4hep import Dd4hep as BuiltinDd4hep


class Dd4hep(BuiltinDd4hep):
    variant("frames", default=True, description="Use podio frames", when="@1.25.1")
    variant("frames", default=True, description="Use podio frames", when="@1.24")
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1157/commits/1c79b1492373dd66b17ea2530a63ec434396afa9.patch?full_index=1",
        sha256="e544cc11c7e1ac9ccacf6688f3d966e912b1a2e1a7460f7c16212a0a4df5b05e",
        when="@=1.26",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1158/commits/fecf99a2732a3f6aafc5fbf0f4a05af5bac196f8.patch?full_index=1",
        sha256="ecc8e5534a5c7e9a4e3008508e17646a578ce7a44897df514dfd2c9a449968b1",
        when="@=1.26",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1168/commits/0cdf506db8a9f47698129b5c8f52b66f53429818.patch?full_index=1",
        sha256="a75d89c86ab44ef1f3f86201e083c85e4e8f0b3120785d5a76fdc81256a937ac",
        when="@=1.26",
    )
    patch(
        "https://github.com/AIDASoft/DD4hep/pull/1161.diff?full_index=1",
        sha256="2f301aa18033bfbf53c4377e848764a5d6b9a96799e3e990cd17a2648883e141",
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
    @when('@1.25.1')
    def setup_run_environment(self, env):
        super().setup_run_environment(env)
        env.set("CXXFLAGS", "-DDD4HEP_FIELD_TYPE_OVERRIDE=field_type")
    @when('@1.25.1')
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
        "https://github.com/AIDASoft/DD4hep/commit/8693a29669d03dec5e06b61e6df7cc0df1e0aa5c.patch",
        sha256="28fb1c17eb1c06c24b304511308fd3b0af708f2ba3aec3e4cb13d7da6abbc51c",
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
