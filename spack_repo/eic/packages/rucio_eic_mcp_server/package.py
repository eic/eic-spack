# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class RucioEicMcpServer(PythonPackage):
    """An MCP server for querying Rucio data-management for the EIC.

    Talks to the Rucio REST API directly over requests, so it needs no
    rucio client install."""

    homepage = "https://github.com/eic/rucio-eic-mcp-server"
    git = "https://github.com/eic/rucio-eic-mcp-server.git"

    maintainers("wdconinc")

    tags = ["eic"]

    license("MIT", checked_by="aprozo")

    version("main", branch="main")
    # No release tag upstream yet; pin the current main for reproducibility.
    version("0.1.0", commit="e5b630bdebaa6d7156a71db5c6287d3fb425ee17")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")
    depends_on("py-wheel", type="build")

    depends_on("py-mcp+cli", type=("build", "run"))
    depends_on("py-requests@2.28:", type=("build", "run"))
