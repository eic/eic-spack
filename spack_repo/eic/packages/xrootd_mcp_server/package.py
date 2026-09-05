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

    tags = ["eic"]

    license("MIT", checked_by="wdconinc")

    version("main", branch="main")
    version("0.2.2", sha256="6300491ec47e5e14a13d0f97b2e81c33dfedf55ceefdc67b1f5b07c2fd940ee1")
    version("0.2.1", sha256="59b16e8f126e17354545603c390b117f64c48c266a1cdf0c402c782eb6ec61a2", deprecated=True)
    version("0.2.0", sha256="fee4a4ac95debe4f662b0e975ffd7edc7148798127fd3db46135b3bb1b1a06f4")
    version("0.1.0", sha256="320b2974e7e04815e76e5649ea9bf0722f6bdf04435c6ea0402e09555d3e6fb1")

    depends_on("node-js@22:", type=("build", "run"))
    depends_on("npm@10:", type="build")
    depends_on("xrootd", type=("build", "run"))

    def install(self, spec, prefix):
        npm = which("npm", required=True)
        npm("install", "--global", f"--prefix={prefix}", ".")
