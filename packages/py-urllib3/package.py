from spack.package import *

try:
    from spack_repo.builtin.packages.py_urllib3.package import PyUrllib3 as BuiltinPyUrllib3
except:
    from spack.pkg.builtin.py_urllib3 import PyUrllib3 as BuiltinPyUrllib3

class PyUrllib3(BuiltinPyUrllib3):
    version("2.3.0", sha256="f8c5449b3cf0861679ce7e0503c7b44b5ec981bec0d1d3795a07f1ba96f0204d")

    depends_on("python@3.8:", when="@2.1.0:2.2", type=("build", "run"))
    depends_on("python@3.9:", when="@2.3:", type=("build", "run"))
    depends_on("py-hatch-vcs@0.4.0", when="@2.3:", type="build")
