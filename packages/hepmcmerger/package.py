# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Hepmcmerger(Package):
    """An EIC HepMC merger to combine signal and background events."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/eic/HEPMC_Merger"
    url = "https://github.com/eic/HEPMC_Merger/releases/tag/v1.0.4"
    list_url = "https://github.com/eic/HEPMC_Merger/tags"
    git = "https://github.com/eic/HEPMC_Merger"

    maintainers = ["kkauder"]

    tags = ["eic"]

    version("main", branch="main")
    version("v1.0.4", sha256="2255363aecdf53ad926002656dd404319b77d287127b82894aa54c91ae482688")
    version("v1.0.3", sha256="d09c3ce65cc41a5f0bed4111deaa2d0d0e37173725c4caf873fd8f312f37096e")
    version("v1.0.2", sha256="50d8be2b69cf87460c69bf261cf61c64587ea5aadcfe344aec1b0a1d8b59b386")
    version("v1.0.1", sha256="f244ff4de311c164597eaedf547a7305b6d3cc1e6b2bc6e6d9acb8e603a44a4b")
    version("v1.0.0", sha256="c6088ba6ce73a92d165bc82e19f6670a1545fcfb6f352cdf5629c395a95c16af")

    depends_on("hepmc3")
    depends_on("root")

    def cmake_args(self):
        args = []
        args.append(
            "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value
        )
        return args