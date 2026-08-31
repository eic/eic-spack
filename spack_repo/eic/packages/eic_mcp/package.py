# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class EicMcp(Package):
    """Service manager for the EIC MCP servers inside eic-shell.

    Starts/stops the installed MCP servers in their native streamable-HTTP
    mode and writes client configs, so an LLM client (opencode, Claude Code,
    Copilot, ...) can drive them over 127.0.0.1. Serves what is installed;
    it does not build, bridge, or fetch servers."""

    homepage = "https://github.com/eic/eic-mcp"
    git = "https://github.com/eic/eic-mcp.git"

    maintainers("wdconinc")

    tags = ["eic"]

    license("MIT", checked_by="aprozo")

    version("main", branch="main")
    # TODO(push): repoint to the feat/native-http-servers head; retag as 0.2.0.
    version("0.1.0", commit="4a5c610458dc1df94439aecce1b749f2ba11ad60")

    # The servers eic-mcp serves. They are runtime, not build, dependencies:
    # eic-mcp only launches their installed console entry points.
    depends_on("uproot-mcp-server", type="run")
    depends_on("rucio-eic-mcp-server", type="run")
    depends_on("xrootd-mcp-server", type="run")
    # stdio-only upstream for now; still usable by stdio clients.
    depends_on("zenodo-mcp-server", type="run")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path("bin", "eic-mcp"), join_path(prefix.bin, "eic-mcp"))
        set_executable(join_path(prefix.bin, "eic-mcp"))
