from spack_repo.builtin.packages.py_minkowskiengine.package import (
    PyMinkowskiengine as BuiltinPyMinkowskiengine,
)

from spack.package import *


class PyMinkowskiengine(BuiltinPyMinkowskiengine):
    __doc__ = BuiltinPyMinkowskiengine.__doc__

    git = "https://github.com/NVIDIA/MinkowskiEngine"
    version("master", branch="master")
