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

    maintainers("DraTeots")

    tags = ["eic"]

    license("LGPL-3.0-or-later", checked_by="wdconinc")

    # 0.2.7 is broken on pypi; https://pypi.org/project/pyrobird/0.2.7/#files 37.7 kb
    #version("0.2.7", sha256="907fe4db5b4b3ec84fbf05544957d5d4f26df5ceb99b0aa46f91eb3ee55948ad")
    version("0.2.7", sha256="907fe4db5b4b3ec84fbf05544957d5d4f26df5ceb99b0aa46f91eb3ee55948ad")
    version("0.2.6", sha256="aecdfbdcf21260cfa3db3b1350a08277a83097508a9d5f406aff61a0748c97ff")
    version("0.2.4", sha256="e75a4d20e4c35f30d6a60ce70a64872ade8cccddf7930cb5cca771b1d8f6da1d")
    version("0.2.3", sha256="94115a4180a46fc0c4660c7d74c138bac32b217ebafdbff5941311d038a7e98d")
    version("0.2.2", sha256="b1cf4ed69da590e42466c07ea815166fecb88951166b9015c981487de236c69d")
    version("0.2.1", sha256="b292217eb93d03b82128eebb066dc4520ccdf30fd8f8a4bf013c6d5cc1050869")
    version("0.2.0", sha256="d93508812c963627c5c153ebb58c45d29eca9646b644bab138d5b79c68729536")

    variant("test", default=False, description="Enable test functionality")
    variant("batch", default=False, description="Enable batch functionality")
    variant("xrootd", default=False, description="Enable XRootD functionality")

    depends_on("py-setuptools@61:76", type="build")
    depends_on("py-wheel", type="build")

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
