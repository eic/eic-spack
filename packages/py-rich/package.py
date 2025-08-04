from spack.package import *

try:
    from spack_repo.builtin.packages.py_rich.package import PyRich as BuiltinPyRich
except:
    from spack.pkg.builtin.py_rich import PyRich as BuiltinPyRich

class PyRich(BuiltinPyRich):
    version("13.9.4", sha256="439594978a49a09530cff7ebc4b5c7103ef57baf48d5ea3184f21d9a2befa098")
