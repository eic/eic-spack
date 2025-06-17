from spack.package import *
from spack.pkg.builtin.py_packaging import PyPackaging as BuiltinPyPackaging

class PyPackaging(BuiltinPyPackaging):
    version("24.2", sha256="c228a6dc5e932d346bc5739379109d49e8853dd8223571c7c5b55260edc0b97f")
