from spack_repo.builtin.packages.podio.package import Podio as BuiltinPodio

from spack.package import *


class Podio(BuiltinPodio):
    __doc__ = BuiltinPodio.__doc__

    patch(
        "https://github.com/AIDASoft/podio/pull/423.patch?full_index=1",
        sha256="a88278b99a579fa1e8b8027f5ce8baad85d5870f648620d19dd40cf35880aa9d",
        when="@0.16.4:0.16.5",
    )
    patch(
        "https://github.com/AIDASoft/podio/commit/9f9c5fc8d40bc3e037b0846d5133d9a0e4d15c36.patch?full_index=1",
        sha256="36b2f363c06103af276d490e7292a8688d0879f04995d28c46c37c3d6dd35bc4",
        when="@0.16.4:0.16.5",
    )
    patch(
        "https://github.com/AIDASoft/podio/pull/452.patch?full_index=1",
        sha256="47692dd40c30a76a565a20750e494b34d57fbd96bbae2d867cccbbbd9ff09636",
        when="@0.16.4:0.16.5",
    )
