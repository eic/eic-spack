from spack import *
from spack.pkg.builtin.podio import Podio as BuiltinPodio


class Podio(BuiltinPodio):
    patch(
        "https://github.com/AIDASoft/podio/pull/434/commits/9f9c5fc8d40bc3e037b0846d5133d9a0e4d15c36.patch?full_index=1",
        sha256="591aa122f55042b089303a4411418e2ac253469a8b6f6a79ebd14868fb88c1e5",
        when="@0.16.4:0.16.5",
    )
