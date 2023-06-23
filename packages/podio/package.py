from spack import *
from spack.pkg.builtin.podio import Podio as BuiltinPodio


class Podio(BuiltinPodio):
    patch(
        "https://github.com/AIDASoft/podio/pull/423.patch?full_index=1",
        sha256="a88278b99a579fa1e8b8027f5ce8baad85d5870f648620d19dd40cf35880aa9d",
        when="@0.16.4:0.16.5",
    )
    patch(
        "https://github.com/AIDASoft/podio/pull/434.patch?full_index=1",
        sha256="8150062022c2489e07dbedbf073cf7a15fec8d43c3f4c472c3ad7ecd413232fc",
        when="@0.16.4:0.16.5",
    )
