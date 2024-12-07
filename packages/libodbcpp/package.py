# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Libodbcpp(AutotoolsPackage):
    """libodbc++ is a C++ class library for accessing SQL databases."""

    homepage = "https://sourceforge.net/projects/libodbcxx"
    url = "https://sourceforge.net/projects/libodbcxx/files/libodbc%2B%2B/0.2.5/libodbc%2B%2B-0.2.5.tar.bz2/download"
    list_url = "https://sourceforge.net/projects/libodbcxx/files"

    tags = ["eic"]

    version(
        "0.2.5",
        sha256="ba3030a27b34e4aafbececa2ddbbf42a38815e9534f34c051620540531b5e23e",
    )

    depends_on("cxx", type="build")

    def patch(self):
        filter_file("ODBCXX_STRING_PERCENT", '"%"', "src/dtconv.h")

    def configure_args(self):
        args = []
        return args
