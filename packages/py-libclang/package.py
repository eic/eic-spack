from spack.package import *
from spack.pkg.builtin.py_libclang import PyLibclang as BuiltinPyLibclang


class PyLibclang(BuiltinPyLibclang):
    version("18.1.1", sha256="829f1afbf6a704da2130f541279e58d719eb9b67713a0641eb723a2970de1b66")
    version("17.0.6", sha256="dfdc19199ba3ed2169e7f9849bd1472d61fc1fdb8af699e3d083c27e53d394c3")
    version("16.0.6", sha256="626bc239e7568354c8bc5137541732ae81c4e65221b27d9021b9f13306a7a1b2")

    for ver in ["16", "17", "18"]:
        depends_on("llvm+clang@" + ver, when="@" + ver, type="build")