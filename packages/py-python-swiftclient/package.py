from spack.package import *

try:
    from spack_repo.builtin.packages.py_python_swiftclient.package import PyPythonSwiftclient as BuiltinPyPythonSwiftclient
except:
    from spack.pkg.builtin.py_python_swiftclient import PyPythonSwiftclient as BuiltinPyPythonSwiftclient

class PyPythonSwiftclient(BuiltinPyPythonSwiftclient):
    def url_for_version(self, version):
        if version < Version('4.7.0'):
            return f"https://files.pythonhosted.org/packages/source/p/python-swiftclient/python-swiftclient-{version}.tar.gz"
        else:
            return f"https://files.pythonhosted.org/packages/source/p/python-swiftclient/python_swiftclient-{version}.tar.gz"
          
    version("4.7.0", sha256="afd7575753d8e49617adcb11550187fd0b120fcd819f1e782c0b538f2d093773")
