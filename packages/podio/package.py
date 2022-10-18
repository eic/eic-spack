from spack import *
from spack.pkg.builtin.podio import Podio as BuiltinPodio


class Podio(BuiltinPodio):
    version("0.16", sha256="4e149c2c9be9f9ca3a6d863498bb0f642dda1a43a19ac1afe7f99854ded5c510")
    version("0.15", sha256="6c1520877ba1bce250e35a2a56c0a3da89fae0916c5ed7d5548d658237e067d9")
    version("0.14.3", sha256="2a7a405dedc7f6980a0aad7df87b427a1f43bcf6d923a9bcce1698fd296359f7")
