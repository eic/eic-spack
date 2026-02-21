# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

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
        "https://github.com/google/farmhash/pull/25.patch",
        sha256="cbb6709d51d8d517d5df8a47e5c1867610dc5352152e78b64dec75620f95cc97",
    )
