# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Milou(MakefilePackage):
    """MILOU is a Monte Carlo generator for deeply virtual
    Compton scattering (DVCS)."""

    homepage = "https://gitlab.com/eic/mceg/milou"
    url = "https://gitlab.com/eic/mceg/milou"
    list_url = "https://gitlab.com/eic/mceg/milou/-/tags"
    git = "https://gitlab.com/eic/mceg/milou.git"

    tags = ["eic"]

    version("master", branch="master")

    depends_on("cernlib")
    depends_on("pythia6")
    # depends_on('jetset')

    def setup_build_environment(self, env):
        env.set("EICDIRECTORY", self.spec.prefix)

    def edit(self, spec, prefix):
        # ./Makefile
        makefile = FileFilter("Makefile")
        makefile.filter("BITS = 32", "#BITS = 32")
        makefile.filter(r"-m\$\(BITS\) ", "")
        makefile.filter(
            "CERN_LIBS = .*", "CERN_LIBS = {0}/lib".format(spec["cernlib"].prefix)
        )
        makefile.filter(
            "PYTHIA = .*", "PYTHIA = -L{0}/lib -lPythia6".format(spec["pythia6"].prefix)
        )
        if spec.satisfies("%gcc@10:"):
            makefile.filter("F_FLAGS = -g", "F_FLAGS = -g -fallow-argument-mismatch")
        # ./bases51/Makefile
        makefile = FileFilter("bases51/Makefile")
        makefile.filter("BITS = 32", "#BITS = 32")
        makefile.filter(r"-m\$\(BITS\) ", "")
        if spec.satisfies("%gcc@10:"):
            makefile.filter("F_FLAGS = -g", "F_FLAGS = -g -fallow-argument-mismatch")

    def make(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        mkdirp(join_path(self.spec.prefix.bin))
        make("install")
