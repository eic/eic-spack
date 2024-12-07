# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEpicCapybara(PythonPackage):
    """Scripts for ROOT file comparisons."""

    homepage = "https://github.com/eic/epic-capybara"
    url = "https://github.com/eic/epic-capybara"
    git = "https://github.com/eic/epic-capybara.git"

    tags = ["eic"]

    maintainers("veprbl")

    license("MIT")

    version("main", branch="main")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-awkward", type=("build", "run"))
    depends_on("py-bokeh", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-hist", type=("build", "run"))
    depends_on("py-pygithub", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-uproot", type=("build", "run"))
