# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PhonebookCli(Package):
    """Simple command line interface to the EICUG phonebook."""

    homepage = "https://github.com/eic/phonebook-cli"
    url = "https://github.com/eic/phonebook-cli/archive/refs/tags/v1.0.0.tar.gz"

    maintainers("wdconinc")

    version("1.0.0", sha256="fe5dcbeadbbcdc97c8921dccdb854eb4b88209c3e70fdda514da48bef26d4345")

    depends_on("jq")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("phonebook.sh", join_path(prefix.bin, "phonebook"))
