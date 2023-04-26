from spack import *
from spack.pkg.builtin.py_gssapi import PyGssapi as BuiltinPyGssapi


class PyGssapi(BuiltinPyGssapi):
    depends_on("krb5", type=("build", "link"))
