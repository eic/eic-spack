# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Supergateway(Package):
    """Run MCP stdio servers over SSE and Streamable HTTP, and vice versa."""

    homepage = "https://github.com/supercorp-ai/supergateway"
    url = "https://registry.npmjs.org/supergateway/-/supergateway-3.4.3.tgz"

    maintainers("wdconinc")

    tags = ["eic"]

    license("MIT", checked_by="aprozo")

    # The npm registry tarball ships a prebuilt dist/, so no TypeScript build
    # is needed; install with --ignore-scripts to skip the (dev-only) prepare.
    version("3.4.3", sha256="d26391996026bb5967a77e877474cdffa9431ed59c65186d557064de98f5ab84")

    depends_on("node-js@20:", type=("build", "run"))
    depends_on("npm@10:", type="build")

    def install(self, spec, prefix):
        npm = which("npm", required=True)
        npm("install", "--global", "--ignore-scripts", f"--prefix={prefix}", ".")
