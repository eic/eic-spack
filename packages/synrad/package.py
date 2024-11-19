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

    version(
        "1.4.32",
        sha256="5cf60abe26af51d3cbf873cf43bf9ebe51ec46dd9d4fb95b9ca396e1b44fac00",
    )
    version(
        "1.4.31",
        sha256="c6c3952c5ec229de4369bc71666732aded640a985bf8b55c1521717b4478b8d6",
    )
    version(
        "1.4.29",
        sha256="30cd3020d9be8a6add9ae182a6d72357973e29b3b8486f6114118a193b81a4c8",
    )

    variant("cli", default=True, description="Enable only the command line interface")

    depends_on("cxx", type="build")

    depends_on("curl")
    depends_on("gsl")
    depends_on("sdl2")
    depends_on("gtkplus")

    def patch(self):
        filter_file(
            # r"set\((OUTPUT_[A-Z]*_[A-Z]*) (\$\{OS_RELPATH\}/[a-z]*/)\$\{OS_NAME\}/[a-z]*/\)",
            r"^set\((OUTPUT_[A-Z]*_[A-Z]*) (\$\{OS_RELPATH\}/[a-z]*/).*\)",
            # r"set(\1 \2)",
            r"set(\1 \2)",
            "CMake/Synrad.cmake",
        )

    def cmake_args(self):
        args = [
            self.define_from_variant("NO_INTERFACE", "cli"),
        ]
        return args

    def install(self, spec, prefix):
        install_tree(join_path(self.build_directory, "bin"), prefix.bin)
        install_tree(join_path(self.build_directory, "lib"), prefix.lib)
        return
