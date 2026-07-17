# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

# Upstream ships a self-contained (Bun single-file) binary per platform.
# The npm wrapper package (opencode-ai) resolves its platform binary in a
# postinstall script via optionalDependencies, which does not work in an
# offline spack install phase — so install the GitHub release binary instead
# (same pattern as the builtin cudnn-style per-platform version tables).
_versions = {
    "1.18.3": {
        "Linux-x86_64": "60f27b2679f00a511b6539f97e02448afaf58d9c66e2448285ea0c517ca84583",
        "Linux-aarch64": "da0a631174eba380b2a1d51f9d364fa3812da433e72743c72471d4b5da59c69d",
    }
}

_arch_map = {"x86_64": "x64", "aarch64": "arm64"}


class Opencode(Package):
    """opencode — an open-source AI coding agent for the terminal.

    Runs as a TUI or headless CLI against MCP servers and LLM providers, so
    agentic workflows work on machines without a graphical client (farm
    nodes, CI reproducers, ...)."""

    homepage = "https://opencode.ai"
    url = (
        "https://github.com/anomalyco/opencode/releases/download/v1.18.3/opencode-linux-x64.tar.gz"
    )

    maintainers("wdconinc")

    tags = ["eic"]

    license("MIT", checked_by="aprozo")

    for _ver, _shas in _versions.items():
        _key = f"{platform.system()}-{platform.machine()}"
        if _key in _shas:
            _arch = _arch_map[platform.machine()]
            version(
                _ver,
                sha256=_shas[_key],
                url=f"https://github.com/anomalyco/opencode/releases/download/v{_ver}/opencode-linux-{_arch}.tar.gz",
            )

    def install(self, spec, prefix):
        # The tarball contains the single `opencode` binary at its root.
        mkdirp(prefix.bin)
        install("opencode", join_path(prefix.bin, "opencode"))
        set_executable(join_path(prefix.bin, "opencode"))
