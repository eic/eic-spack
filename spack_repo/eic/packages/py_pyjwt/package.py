# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

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

    def test_imports(self):
        python = self.spec["python"].command
        site_packages = []
        for directory in (
            self.spec["python"].package.platlib,
            self.spec["python"].package.purelib,
        ):
            path = join_path(self.prefix, directory)
            if os.path.isdir(path):
                site_packages.append(path)

        env = os.environ.copy()
        env["PYTHONPATH"] = os.pathsep.join(
            site_packages + ([env["PYTHONPATH"]] if env.get("PYTHONPATH") else [])
        )

        python(
            "-c",
            """
import importlib
import sys

for module in sys.argv[1:]:
    print(module)
    importlib.import_module(module)
""",
            "jwt",
            env=env,
        )
