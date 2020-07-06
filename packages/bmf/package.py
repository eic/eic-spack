# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bmf(CMakePackage):
    """BeAST magnetic field map and a C++ class to handle it."""

    homepage = "http://gihub.com/eic/BeastMagneticField"
    url      = "http://gihub.com/eic/BeastMagneticField"
    git      = "http://gihub.com/eic/BeastMagneticField.git"

    version('master', branch='master')

    depends_on('cmake@2.8.10:', type='build')
