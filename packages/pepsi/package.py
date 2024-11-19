# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pepsi(MakefilePackage):
    """PEPSI (Polarised Electron Proton Scattering Interactions)
    is a Monte Carlo generator for polarised deep inelastic
    scattering (pDIS)."""

    homepage = "https://github.com/eic/pepsi"
    url = "https://github.com/eic/pepsi"
    list_url = "https://github.com/eic/pepsi/releases"
    git = "https://github.com/eic/pepsi.git"

    tags = ["eic"]

    version("master", branch="master")

    depends_on("fortran", type="build")

    depends_on("cernlib")

    def patch(self):
        filter_file("/cern64/pro/lib", self.spec["cernlib"].prefix.lib, "Makefile")
        filter_file("packlib_noshift", "packlib", "Makefile")
        if self.spec.satisfies("%gcc@10.0.0:"):
            filter_file("-g -m64", "-g -fallow-argument-mismatch", "Makefile")
        else:
            filter_file("-g -m64", "-g", "Makefile")

    def setup_build_environment(self, env):
        spec = self.spec
        env.set("EICDIRECTORY", self.spec.prefix)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        make()
        make("install")
        install_tree("pdf/", join_path(prefix.share, "pdf"))
        install_tree("STEER-FILES/", join_path(prefix.share, "STEER-FILES"))
