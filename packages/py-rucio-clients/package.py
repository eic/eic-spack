from spack.package import *
from spack.pkg.builtin.py_rucio_clients import PyRucioClients as BuiltinPyRucioClients

class PyRucioClients(BuiltinPyRucioClients):
    version(
        "37.3.0", sha256="b4bca8d451bc34528797ca188884a0c8b5ddfef2d32803765e6333455879f819"
    )

    depends_on("py-requests@2.32.2:", type=("build", "run"), when="@:36")
    depends_on("py-urllib3@1.26.18:", type=("build", "run"), when="@:36")
    depends_on("py-requests@2.32.3:", type=("build", "run"), when="@37:")
    depends_on("py-urllib3@2.3.0:", type=("build", "run"), when="@37:")
    depends_on("py-jsonschema@4.20.0:", type=("build", "run"), when="@:36")
    depends_on("py-jsonschema@4.23.0:", type=("build", "run"), when="@37:")
    depends_on("py-packaging@24.2:", type=("build", "run"), when="@37:")
    depends_on("py-rich@13.9.4:", type=("build", "run"), when="@37:")
    depends_on("py-typing-extensions@4.12.2:", type=("build", "run"))
    depends_on("py-click@8.1.7:", type=("build", "run"), when="@37:")

    with when("+ssh"):
        depends_on("py-paramiko@3.4.0:", when="@:36")
        depends_on("py-paramiko@3.5.1:", when="@37:")

    with when("+kerberos"):
        depends_on("py-requests-kerberos@0.14.0:", when="@:36")
        depends_on("py-requests-kerberos@0.15.0:", when="@37:")

    with when("+swift"):
        depends_on("py-python-swiftclient@4.4.0:", when="@:36")
        depends_on("py-python-swiftclient@4.7.0:", when="@37:")

    with when("+argcomplete"):
        depends_on("py-argcomplete@3.1.6:", when="@:36")
        depends_on("py-argcomplete@3.5.3:", when="@37:")
