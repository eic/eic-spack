# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class OnlineDistribution(Package):
    """sPHENIX/EIC online data distribution system including event libraries
    and performance monitoring tools."""

    homepage = "https://github.com/sPHENIX-Collaboration/online_distribution"
    git = "https://github.com/sPHENIX-Collaboration/online_distribution.git"

    maintainers("wdconinc")

    license("UNKNOWN", checked_by="wdconinc")

    version("ePIC", branch="ePIC")

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
                make()
                make("install")

    def setup_run_environment(self, env):
        env.set("ONLINE_MAIN", self.prefix)
