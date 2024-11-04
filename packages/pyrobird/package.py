# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import llnl.util.tty as tty

from spack.package import *


class Pyrobird(PythonPackage):
    """Phoenix based event display."""

    homepage = "https://eic.github.io/firebird/"
    pypi = "pyrobird/pyrobird-0.1.23.tar.gz"
    git = "https://github.com/eic/firebird.git"

    maintainers("wdconinc")

    license("LGPL-3.0-or-later", checked_by="wdconinc")

    version("0.1.23", sha256="ebc122af0b574e6f1a10831c9577084335c6674ca9c5b6fcb58b4ed26ea72c59")

    variant("test", default=False, description="Enable test functionality")
    variant("batch", default=False, description="Enable batch functionality")
    variant("xrootd", default=False, description="Enable XRootD functionality")

    depends_on("py-hatchling", type="build")
    depends_on("py-click", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-flask", type=("build", "run"))
    depends_on("py-flask-cors", type=("build", "run"))
    depends_on("py-flask-compress@1.8:", type=("build", "run"))
    depends_on("py-json5", type=("build", "run"))
    depends_on("py-uproot", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"), when="+test")
    depends_on("py-pyppeteer", type=("build", "run"), when="+batch")
    depends_on("py-fsspec-xrootd", type=("build", "run"), when="+xrootd")
    depends_on("xrootd +python", type=("build", "run"), when="+xrootd")

    @when("@:0.1.23")
    @run_before("install")
    def fix_link(self):
        symlink(self.build_directory, join_path(self.build_directory, "src"))
