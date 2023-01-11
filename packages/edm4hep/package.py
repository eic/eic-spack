from spack import *
from spack.pkg.builtin.edm4hep import Edm4hep as BuiltinEdm4hep


class Edm4hep(BuiltinEdm4hep):
    version("0.7.2", sha256="e289280d5de2c0a3b542bf9dfe04b9f6471b0a0fcf33f5c8101ea7252e2a7643")
    version("0.7.1", sha256="82e215a532f548a73a6f6094eaa8b436c553994e135f6d63a674543dc89a9f1b")
