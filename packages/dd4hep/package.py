from spack import *
from spack.pkg.builtin.dd4hep import Dd4hep as BuiltinDd4hep


class Dd4hep(BuiltinDd4hep):
    version("1.21", sha256="0f9fe9784bf28fa20ce5555ff074430da430e9becc2566fe11e27c4904a51c94")
