from spack.package import *
from spack.pkg.builtin.py_minkowskiengine import (
    PyMinkowskiengine as BuiltinPyMinkowskiengine,
)


class PyMinkowskiengine(BuiltinPyMinkowskiengine):
    git = "https://github.com/NVIDIA/MinkowskiEngine"
    version("master", branch="master")
