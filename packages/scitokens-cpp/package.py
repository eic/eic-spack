from spack import *
from spack.pkg.builtin.scitokens_cpp import ScitokensCpp as BuiltinScitokensCpp


class ScitokensCpp(BuiltinScitokensCpp):
    depends_on("pkgconfig", type="build")
