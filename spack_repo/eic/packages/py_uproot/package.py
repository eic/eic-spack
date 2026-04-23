from spack.package import *

try:
    from spack_repo.builtin.packages.py_uproot.package import PyUproot as BuiltinPyUproot
except ImportError:
    from spack.pkg.builtin.py_uproot import PyUproot as BuiltinPyUproot


class PyUproot(BuiltinPyUproot):
    __doc__ = BuiltinPyUproot.__doc__

    # Support RNTuple v1.0.1.0 format (attribute set record frame)
    patch(
        "https://github.com/scikit-hep/uproot5/commit/88e69d47caa8cdb1ab0f47ffa27b2a6d113896d9.patch?full_index=1",
        sha256="a5120c569b5402870851d38ad4a0ed357629519010f4e38e0770acdd6a7eeb8e",
        when="@5.5.2:5.7.1",
    )
    # Fix RNTuple _from_zigzag to apply bit shift on unsigned integers
    # https://github.com/scikit-hep/uproot5/pull/1593
    patch(
        "https://github.com/scikit-hep/uproot5/commit/ee1b1d550802ad9579a8c64d6a63903c7adbb06d.patch?full_index=1",
        sha256="094390ad52b3e28dc6c91a93b855b3ffe2e460adaf79f877b8389cfd28599aa0",
        when="@5.5.0:5.7.1",
    )
