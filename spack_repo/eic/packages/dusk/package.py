# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Dusk(CMakePackage):
    """From dawn till dusk: dusk is an OCCT-based replacement for the
    legacy dawn detector visualization tool. It reads STEP files (.stp)
    and produces SVG vector graphics of cross-section and
    perspective/isometric views."""

    homepage = "https://eic.github.io/dusk/"
    url = "https://github.com/eic/dusk/archive/refs/tags/v0.1.0.tar.gz"

    maintainers("wdconinc")

    tags = ["eic"]

    license("LGPL-2.1-or-later", checked_by="wdconinc")

    version("0.1.0", sha256="f4d5d861767a64491cffc98227fa75f809b04ab922f092790e0270f418236ad8")

    depends_on("cxx", type="build")
    depends_on("cmake@3.16:", type="build")

    depends_on("opencascade")

    def cmake_args(self):
        args = [
            self.define("DUSK_BUILD_APPS", True),
            self.define("DUSK_ENABLE_TESTS", self.run_tests),
        ]
        return args
