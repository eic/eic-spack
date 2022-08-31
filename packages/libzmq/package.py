from spack import *
from spack.pkg.builtin.libzmq import Libzmq as BuiltinLibzmq


class Libzmq(BuiltinLibzmq):
    # Fix build issues with gcc-12
    patch(
        "https://github.com/zeromq/libzmq/pull/4334.patch?full_index=1",
        sha256="edca864cba914481a5c97d2e975ba64ca1d2fbfc0044e9a78c48f1f7b2bedb6f",
        when="@4.3.4 %gcc@12:",
    )
