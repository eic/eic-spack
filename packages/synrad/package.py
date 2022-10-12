# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Synrad(CMakePackage):
    """SynRad+ is a modification of MolFlow+. Instead of molecules, it traces
    photons to calculate flux and power distribution on a surface caused by
    synchrotron radiation."""

    homepage = "https://molflow.web.cern.ch"
    url = "https://gitlab.cern.ch/molflow_synrad/synrad/-/archive/v1.4.29/synrad-v1.4.29.zip"
    list_url = "https://gitlab.cern.ch/molflow_synrad/synrad/-/tags"
    git = "https://gitlab.cern.ch/molflow_synrad/synrad"

    maintainers = ["wdconinc"]

    version("1.4.29", commit="77398271b037200431667f7ef0df50730712d796", submodules=True)

    variant("cli", default=True, description="Enable only the command line interface")

    depends_on("curl")
    depends_on("gsl")
    depends_on("sdl2")
    depends_on("gtkplus")

    def cmake_args(self):
        args = [
            self.define_from_variant("NO_INTERFACE", "cli"),
        ]
        return args
