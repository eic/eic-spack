# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Farmhash(AutotoolsPackage):
    """FarmHash is a family of hash functions."""

    homepage = "https://github.com/google/farmhash"
    url = "https://github.com/google/farmhash"
    git = "https://github.com/google/farmhash"

    maintainers = ["wdconinc"]

    version("master", branch="master")

    depends_on("cxx", type="build")

    depends_on("autoconf", type="build", when="@master")
    depends_on("automake", type="build", when="@master")
    depends_on("libtool", type="build", when="@master")

    force_autoreconf = True

    patch(
        "https://github.com/google/farmhash/pull/25.patch?full_index=1",
        sha256="161b82eb5408c70c82f633ab76f564e4b6e4a495756e423d4ba08fb5b9fbf5ef",
    )
