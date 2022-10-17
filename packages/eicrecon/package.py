# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Eicrecon(CMakePackage):
    """EIC Reconstruction - JANA based."""

    homepage = "https://github.com/eic/eicrecon"
    url = "https://github.com/eic/EICrecon/archive/refs/tags/v0.1.0.zip"
    git = "https://github.com/eic/eicrecon.git"
    list_url = "https://github.com/eic/EICrecon/tags"

    maintainers = ["wdconinc"]

    version("main", branch="main")
    version(
        "0.2.2",
        sha256="de8e5ef71465027226debfe4d42b8a4f883ffcb03ce2bfee0a0d247a4a1e89f2",
    )
    version(
        "0.2.1",
        sha256="097fef82cacd45453770f30e7e0ae382a11660b8bd4dfe478e7488a8988b8816",
    )
    version(
        "0.2.0",
        sha256="3fc0b812637d6bca9587cb4dadcd4b2ca386458ff6d46551ed8cf291335b4780",
    )
    version(
        "0.1.0",
        sha256="dcc8b60530a627c825413c07472659ba155600339ef8b8e742e3c997bcc504ae",
    )

    depends_on("cmake@3.16:", type="build")

    depends_on("jana2 +root +zmq")
    depends_on("dd4hep +ddrec +edm4hep")
    depends_on("edm4eic")
    depends_on("edm4hep")
    depends_on("podio")
    depends_on("acts +dd4hep +identification +tgeo")
    depends_on("root")
    depends_on("fmt")
    depends_on("spdlog")
