# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class XrootdMcpServer(Package):
    """An MCP server that allows for querying XRootD servers by LLM agents."""

    homepage = "https://eic.github.io/xrootd-mcp-server/"
    url = "https://github.com/eic/xrootd-mcp-server/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/eic/xrootd-mcp-server.git"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("main", branch="main")
    version("0.1.0", sha256="320b2974e7e04815e76e5649ea9bf0722f6bdf04435c6ea0402e09555d3e6fb1")

    depends_on("node-js@22:", type=("build", "run"))
    depends_on("npm@10:", type="build")
    depends_on("xrootd")

    def install(self, spec, prefix):
        npm = which("npm", required=True)
        npm("install", "--global", f"--prefix={prefix}")
