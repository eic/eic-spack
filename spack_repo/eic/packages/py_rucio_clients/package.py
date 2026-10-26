# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.py_rucio_clients.package import (
    PyRucioClients as BuiltinPyRucioClients,
)

from spack.package import *


class PyRucioClients(BuiltinPyRucioClients):
    __doc__ = BuiltinPyRucioClients.__doc__

    patch("token-upload-client-40.2.0.patch", when="@40.2.0")

    @property
    def skip_modules(self):
        # rucio.common.schema imports rucio.db, which is only in the server package
        modules = ["rucio.common.schema"]
        # rucio.common.dumper imports magic (py-python-magic)
        if not self.spec.satisfies("+dumper"):
            modules.append("rucio.common.dumper")
        return modules

    def setup_build_environment(self, env):
        # python-venv adds the site-packages directory of a dependent to PYTHONPATH
        # only if it exists when the environment is set up, so it is missing while
        # the package itself is built and the install-time test_imports fails with
        # "No module named 'rucio'"
        venv = self.spec["python-venv"].package
        for directory in {venv.platlib, venv.purelib}:
            env.prepend_path("PYTHONPATH", join_path(self.prefix, directory))

    def test_token_upload(self):
        """check that the clients provide token-based upload"""
        if not self.spec.satisfies("@40.2.0"):
            raise SkipTest("Token upload patch only applies to 40.2.0")
        python = self.spec["python"].command
        python(
            "-c",
            "from rucio.client.credentialclient import CredentialClient\n"
            "from rucio.client.uploadclient import UploadClient\n"
            "assert hasattr(CredentialClient, 'get_upload_token')\n"
            "assert hasattr(CredentialClient, 'get_download_token')\n",
        )
