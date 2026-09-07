# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class RucioEicMcpServer(PythonPackage):
    """An MCP server for querying Rucio data-management for the EIC (REST API, no rucio client)."""

    homepage = "https://github.com/eic/rucio-eic-mcp-server"
    url = "https://github.com/eic/rucio-eic-mcp-server/archive/refs/tags/v0.2.0.tar.gz"
    git = "https://github.com/eic/rucio-eic-mcp-server.git"

    maintainers("wdconinc")

    tags = ["eic"]

    license("MIT", checked_by="aprozo")

    version("main", branch="main")
    version("0.1.0", commit="e5b630bdebaa6d7156a71db5c6287d3fb425ee17")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")
    depends_on("py-wheel", type="build")

    # no mcp[cli] (click pin conflicts); mcp 2 dropped mcp.server.fastmcp
    depends_on("py-mcp@1.10.1:1", type=("build", "run"))
    depends_on("py-requests@2.28:", type=("build", "run"))

    def setup_build_environment(self, env):
        # `--test root` runs the import test in this environment, set up before
        # the install; python-venv adds site-packages only once it exists
        venv = self.spec["python-venv"].package
        for d in {venv.platlib, venv.purelib}:
            env.prepend_path("PYTHONPATH", join_path(self.prefix, d))
