# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Pyrobird(PythonPackage):
    """Phoenix based event display."""

    homepage = "https://eic.github.io/firebird/"
    pypi = "pyrobird/pyrobird-0.1.23.tar.gz"
    git = "https://github.com/eic/firebird.git"

    maintainers("wdconinc")

    tags = ["eic"]

    license("LGPL-3.0-or-later", checked_by="wdconinc")

    version("0.2.6", sha256="aecdfbdcf21260cfa3db3b1350a08277a83097508a9d5f406aff61a0748c97ff")
    version("0.2.4", sha256="e75a4d20e4c35f30d6a60ce70a64872ade8cccddf7930cb5cca771b1d8f6da1d")
    version("0.2.3", sha256="94115a4180a46fc0c4660c7d74c138bac32b217ebafdbff5941311d038a7e98d")
    version("0.2.2", sha256="b1cf4ed69da590e42466c07ea815166fecb88951166b9015c981487de236c69d")
    version("0.2.1", sha256="b292217eb93d03b82128eebb066dc4520ccdf30fd8f8a4bf013c6d5cc1050869")
    version("0.2.0", sha256="d93508812c963627c5c153ebb58c45d29eca9646b644bab138d5b79c68729536")
    version("0.1.27", sha256="cd359b7bb795a533aee9369a46579cb753004654883d3892c2fd76c9d4c35343")
    version("0.1.24", sha256="f6ab7197aacc6615024bb644b21dc8a35f9a6fb39688a59745f0ad360f82e1ce")
    version("0.1.23", sha256="ebc122af0b574e6f1a10831c9577084335c6674ca9c5b6fcb58b4ed26ea72c59")

    variant("test", default=False, description="Enable test functionality")
    variant("batch", default=False, description="Enable batch functionality")
    variant("xrootd", default=False, description="Enable XRootD functionality")

    with when("@0.2:"):
        depends_on("py-setuptools@61:", type="build")
        depends_on("py-wheel", type="build")
    with when("@0.1"):
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
