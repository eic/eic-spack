# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.build_systems.cmake import CMakePackage
except ImportError:
    from spack.build_systems.cmake import CMakePackage


class ClangBuildAnalyzer(CMakePackage):
    """Clang build analysis tool using -ftime-trace."""

    homepage = "https://github.com/aras-p/ClangBuildAnalyzer"
    url = "https://github.com/aras-p/ClangBuildAnalyzer/archive/refs/tags/v1.6.0.tar.gz"

    maintainers("wdconinc")

    license("Unlicense", checked_by="wdconinc")

    version("1.6.0", sha256="868a8d34ecb9b65da4e5874342062a12c081ce4385c7ddd6ce7d557a0c5c292d")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
