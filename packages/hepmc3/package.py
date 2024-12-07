from spack.package import *
from spack.pkg.builtin.hepmc3 import Hepmc3 as BuiltinHepmc3


class Hepmc3(BuiltinHepmc3):
    version(
        "3.2.5",
        sha256="cd0f75c80f75549c59cc2a829ece7601c77de97cb2a5ab75790cac8e1d585032",
    )
    patch(
        "ReaderPlugin.patch",
        sha256="66354530bea9f68a1eb5a1fcceb829e5df6844ee0e0ea67aec2af55d5e4cfa78",
        when="@3.2.5",
    )
