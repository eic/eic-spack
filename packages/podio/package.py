from spack.package import *
from spack.pkg.builtin.podio import Podio as BuiltinPodio


class Podio(BuiltinPodio):
    patch(
        "https://github.com/AIDASoft/podio/pull/423.patch?full_index=1",
        sha256="a88278b99a579fa1e8b8027f5ce8baad85d5870f648620d19dd40cf35880aa9d",
        when="@0.16.4:0.16.5",
    )
    patch(
        "https://github.com/AIDASoft/podio/pull/434/commits/9f9c5fc8d40bc3e037b0846d5133d9a0e4d15c36.patch?full_index=1",
        sha256="591aa122f55042b089303a4411418e2ac253469a8b6f6a79ebd14868fb88c1e5",
        when="@0.16.4:0.16.5",
    )
    patch(
        "https://github.com/AIDASoft/podio/pull/452.patch?full_index=1",
        sha256="47692dd40c30a76a565a20750e494b34d57fbd96bbae2d867cccbbbd9ff09636",
        when="@0.16.4:0.16.5",
    )
