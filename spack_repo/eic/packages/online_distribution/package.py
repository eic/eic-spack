# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class OnlineDistribution(Package):
    """EIC/ePIC online data distribution system including event libraries
    and performance monitoring tools."""

    homepage = "https://github.com/eic/online_distribution"
    url = "https://github.com/eic/online_distribution/archive/refs/tags/2026.11.14.tar.gz"
    git = "https://github.com/eic/online_distribution.git"

    maintainers("wdconinc", "mpurschke")

    tags = ["eic"]

    license("UNKNOWN", checked_by="wdconinc")

    version(
        "2026.11.14", sha256="225fa73d1a4f18b6efb15aa76e4df9b972d5a9727b841267d11a846898b4ba2f"
    )
    version(
        "ePIC",
        branch="ePIC",
        git="https://github.com/sPHENIX-Collaboration/online_distribution.git",
        deprecated=True,
    )

    depends_on("cxx", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("gmake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    depends_on("root")
    depends_on("boost")
    depends_on("lzo")
    depends_on("zlib-api")
    depends_on("bzip2")

    def patch(self):
        # Remove hardcoded /opt/local paths from eventlibraries/Makefile.am
        filter_file(r" -L/opt/local/lib", "", "eventlibraries/Makefile.am")
        filter_file(r" -I/opt/local/include", "", "eventlibraries/Makefile.am")

    def install(self, spec, prefix):
        for subdir in ["eventlibraries", "pmonitor"]:
            with working_dir(subdir):
                autoreconf = Executable("autoreconf")
                autoreconf("-fvi")
                configure = Executable("./configure")
                configure(f"--prefix={prefix}")
                make("CPPFLAGS=-DLinux -DHAVE_GETOPT_H=1")
                make("install")

    def setup_run_environment(self, env):
        env.set("ONLINE_MAIN", self.prefix)

    def test_dlist(self):
        """list the packets in one event from the built-in test stream"""
        dlist = which(join_path(self.prefix.bin, "dlist"), required=True)
        out = dlist("-T", "-i", "-n", "1", output=str, error=str)
        assert "Event" in out
        for packet in ["1001", "1002", "1003", "1008"]:
            assert f"Packet  {packet}" in out, f"packet {packet} missing in:\n{out}"
