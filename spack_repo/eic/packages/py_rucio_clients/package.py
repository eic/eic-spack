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
