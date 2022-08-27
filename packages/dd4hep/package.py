from spack import *
from spack.pkg.builtin.dd4hep import Dd4hep as BuiltinDd4hep


class Dd4hep(BuiltinDd4hep):
    patch(
        "https://github.com/AIDASoft/DD4hep/commit/8693a29669d03dec5e06b61e6df7cc0df1e0aa5c.patch",
        sha256="28fb1c17eb1c06c24b304511308fd3b0af708f2ba3aec3e4cb13d7da6abbc51c",
        when="@1.21:",
    )
