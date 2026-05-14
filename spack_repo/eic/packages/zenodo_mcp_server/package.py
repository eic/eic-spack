# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class ZenodoMcpServer(Package):
    """An MCP server that allows for querying Zenodo repositories by LLM agents."""

    homepage = "https://eic.github.io/zenodo-mcp-server/"
    url = "https://github.com/eic/zenodo-mcp-server/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/eic/zenodo-mcp-server.git"

    maintainers("wdconinc")

    tags = ["eic"]

    license("MIT", checked_by="wdconinc")

    version("main", branch="main")
    version("0.1.0", sha256="254bffa4ca24996d9947ac88688b9cf407142ec5024919b49efd6e737092dd14")

    depends_on("node-js@22:", type=("build", "run"))
    depends_on("npm@10:", type="build")

    def install(self, spec, prefix):
        npm = which("npm", required=True)
        npm("install", "--global", f"--prefix={prefix}", ".")
