from spack.package import *
from spack.pkg.builtin.py_jsonschema import PyJsonschema as BuiltInPyJsonschema

class PyJsonschema(BuiltinPyJsonschema):
     version("4.23.0", sha256="d71497fef26351a33265337fa77ffeb82423f3ea21283cd9467bb03999266bc4")
