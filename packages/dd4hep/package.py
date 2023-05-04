from spack import *
from spack.pkg.builtin.dd4hep import Dd4hep as BuiltinDd4hep


class Dd4hep(BuiltinDd4hep):
    variant("frames", default=True, description="Use podio frames")
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
        "revert-Geant4Output2EDM4hep-dd4hep-1-24-to-1-23.patch",
        sha256="d2077dbb83f18e9873c396309773dc0de4bf63b9b807ca464572e10ad5fa0797",
        when="@1.24 -frames",
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
        "pr1106.1.25.1.patch",
        sha256="73932633e95272f77c1f6ad8edf06d426b198c30a9c9467167c04f3a3f7f5d12",
        when="@1.25.1",
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
