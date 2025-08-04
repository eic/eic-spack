from spack.package import *

try:
    from spack_repo.builtin.packages.py_argcomplete.package import PyArgcomplete as BuiltinPyArgcomplete
except:
    from spack.pkg.builtin.py_argcomplete import PyArgcomplete as BuiltinPyArgcomplete

class PyArgcomplete(BuiltinPyArgcomplete):
    version("3.5.3", sha256="c12bf50eded8aebb298c7b7da7a5ff3ee24dffd9f5281867dfe1424b58c55392")

    depends_on("py-setuptools@67.7.2:", when="@3.1:3.5.2", type="build")
    depends_on("py-setuptools", when="@:3.0", type="build")
    depends_on("py-setuptools-scm+toml@6.2:", when="@3.1:3.5.2", type="build")

    depends_on("py-hatchling", when="@3.5.3:", type="build")
    depends_on("py-hatch-vcs", when="@3.5.3:", type="build")
