from spack.package import *

try:
    from spack_repo.builtin.packages.py_uproot.package import PyUproot as BuiltinPyUproot
except:
    from spack.pkg.builtin.py_uproot import PyUproot as BuiltinPyUproot

class PyUproot(BuiltinPyUproot):
    # Backport upstream commit adding ROOT RNTuple v1.0.1.0 support to uproot.
    patch(
        "https://github.com/scikit-hep/uproot5/commit/88e69d47caa8cdb1ab0f47ffa27b2a6d113896d9.patch?full_index=1",
        sha256="a5120c569b5402870851d38ad4a0ed357629519010f4e38e0770acdd6a7eeb8e",
        when="@5.5.2:5.7.1",
    )
