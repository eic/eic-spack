# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bmf(CMakePackage):
    """BeAST magnetic field map and a C++ class to handle it."""

    homepage = "http://github.com/eic/BeastMagneticField"
    url      = "http://github.com/eic/BeastMagneticField"
    git      = "http://github.com/eic/BeastMagneticField.git"

    version('master', branch='master')
    version('2020-04-13', commit='d00c54dc812bfa1804acb5fe370bb9c27b3539f9')

    depends_on('cmake@2.8.10:', type='build')
