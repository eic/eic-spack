from spack import *
from spack.pkg.builtin.podio import Podio as BuiltinPodio


class Podio(BuiltinPodio):
    version(
        "0.16.2",
        sha256="faf7167290faf322f23c734adff19904b10793b5ab14e1dfe90ce257c225114b",
    )
    version(
        "0.16.1",
        sha256="23cd8dfd00f9cd5ae0b473ae3279fa2c22a2d90fb6c07b37d56e63a80dd76ab2",
    )
    patch(
        "https://patch-diff.githubusercontent.com/raw/AIDASoft/podio/pull/369.patch?full_index=1",
        sha256="a6651073f633c937450731129ce4f45428174a70f0b2328c200b56ce42872b65",
        when="@0.16.1:0.16.2",
    )
    patch(
        "https://github.com/AIDASoft/podio/pull/434/commits/9f9c5fc8d40bc3e037b0846d5133d9a0e4d15c36.patch?full_index=1",
        sha256="591aa122f55042b089303a4411418e2ac253469a8b6f6a79ebd14868fb88c1e5",
        when="@0.16.4:0.16.5",
    )
