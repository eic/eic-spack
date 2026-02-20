from spack.package import *

try:
    from spack_repo.builtin.packages.py_minkowskiengine.package import (
        PyMinkowskiengine as BuiltinPyMinkowskiengine,
    )
except ImportError:
    from spack.pkg.builtin.py_minkowskiengine import PyMinkowskiengine as BuiltinPyMinkowskiengine

class PyMinkowskiengine(BuiltinPyMinkowskiengine):
    git = "https://github.com/NVIDIA/MinkowskiEngine"
    version("master", branch="master")
