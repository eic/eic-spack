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
    version("0.2.0", sha256="f1d27f87a4dc8c1ad0a3169d1b73e5cc7f4f2fddb574ae25e36f6b6c9bb218a8")
    version("0.1.0", sha256="b52485744f9e9112ada49c4455e51b6937a19922ca1c197be4b0d5656983b76f")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    # mcp 2 dropped mcp.server.fastmcp
    depends_on("py-mcp@1", type=("build", "run"))
    depends_on("py-mcp@1.10:", type=("build", "run"), when="@0.2:")
    depends_on("py-uproot@5:", type=("build", "run"))
    depends_on("py-numpy@1.26.4:", type=("build", "run"))
    depends_on("py-awkward@2:", type=("build", "run"))
    depends_on("py-restrictedpython@8.1:", type=("build", "run"))

    def setup_build_environment(self, env):
        # `--test root` runs the import test in this environment, set up before
        # the install; python-venv adds site-packages only once it exists
        venv = self.spec["python-venv"].package
        for d in {venv.platlib, venv.purelib}:
            env.prepend_path("PYTHONPATH", join_path(self.prefix, d))
