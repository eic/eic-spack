# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class UprootMcpServer(PythonPackage):
    """An MCP server for inspecting and analyzing ROOT files with uproot."""

    homepage = "https://github.com/eic/uproot-mcp-server"
    url = "https://github.com/eic/uproot-mcp-server/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/eic/uproot-mcp-server.git"

    maintainers("wdconinc")

    tags = ["eic"]

    license("MIT", checked_by="aprozo")

    version("main", branch="main")
    version("0.1.0", sha256="b52485744f9e9112ada49c4455e51b6937a19922ca1c197be4b0d5656983b76f")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-mcp", type=("build", "run"))
    depends_on("py-uproot@5:", type=("build", "run"))
    depends_on("py-numpy@1.26.4:", type=("build", "run"))
    depends_on("py-awkward@2:", type=("build", "run"))
    depends_on("py-restrictedpython@8.1:", type=("build", "run"))
