# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Eicrecon(CMakePackage):
    """EIC Reconstruction - JANA based."""

    homepage = "https://github.com/eic/eicrecon"
    url      = "https://github.com/eic/eicrecon"
    git      = "https://github.com/eic/eicrecon.git"

    maintainers = ['wdconinc']

    version('main', branch='main')

    depends_on('cmake@3.8:', type='build')
    depends_on('jana2')
    depends_on('dd4hep')
    depends_on('edm4hep@0.5:')
    depends_on('fmt')

