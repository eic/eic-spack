from spack import *
from spack.pkg.builtin.dd4hep import Dd4hep as BuiltinDd4hep


class Dd4hep(BuiltinDd4hep):
    version("1.23", sha256="64e4f213e500147e4067301b03143b872381e2ae33710cb6eea8c578529dd596")
    version("1.22", sha256="0e729b8897b7a9c348bc3304c63d4efd1a88e032a2ff5a8c4daf6c927fd7f8ee")
    version("1.21", sha256="0f9fe9784bf28fa20ce5555ff074430da430e9becc2566fe11e27c4904a51c94")
    patch(
        "https://github.com/AIDASoft/DD4hep/commit/8693a29669d03dec5e06b61e6df7cc0df1e0aa5c.patch",
        sha256="28fb1c17eb1c06c24b304511308fd3b0af708f2ba3aec3e4cb13d7da6abbc51c",
        when="@1.21:1.22",
    )
