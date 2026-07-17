# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.py_pyjwt.package import PyPyjwt as BuiltinPyPyjwt

from spack.package import *


class PyPyjwt(BuiltinPyPyjwt):
    __doc__ = BuiltinPyPyjwt.__doc__

    # py-mcp needs pyjwt>=2.10.1; builtin stops at 2.4.0. Newer sdists use the
    # PEP 625 lowercase filename, so the version carries its own url.
    version(
        "2.10.1",
        sha256="3cc5772eb20009233caf06e9d8a0577824723b44e6648ee0a2aedb6cf9381953",
        url="https://files.pythonhosted.org/packages/source/p/pyjwt/pyjwt-2.10.1.tar.gz",
    )

    depends_on("python@3.9:", when="@2.10:", type=("build", "run"))
