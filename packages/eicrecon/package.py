# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Eicrecon(CMakePackage):
    """EIC Reconstruction - JANA based."""

    homepage = "https://github.com/eic/eicrecon"
    url      = "https://github.com/eic/EICrecon/archive/refs/tags/v0.1.0.zip"
    git      = "https://github.com/eic/eicrecon.git"
    list_url = "https://github.com/eic/EICrecon/releases"

    maintainers = ['wdconinc']

    version('main', branch='main')
    version("0.1.0", sha256="dcc8b60530a627c825413c07472659ba155600339ef8b8e742e3c997bcc504ae")

    depends_on('cmake@3.16:', type='build')

    depends_on('jana2 +root +zmq')
    depends_on('dd4hep +ddrec +edm4hep')
    depends_on('edm4eic')
    depends_on('edm4hep')
    depends_on('podio')
    depends_on('acts +dd4hep +edm4hep +identification +tgeo')
    depends_on('root')
    depends_on('fmt')
