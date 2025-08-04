from spack.package import *

try:
     from spack_repo.builtin.packages.py_jsonschema.package import PyJsonschema as BuiltinPyJsonschema
except:
     from spack.pkg.builtin.py_jsonschema import PyJsonschema as BuiltinPyJsonschema

class PyJsonschema(BuiltinPyJsonschema):
     version("4.23.0", sha256="d71497fef26351a33265337fa77ffeb82423f3ea21283cd9467bb03999266bc4")
