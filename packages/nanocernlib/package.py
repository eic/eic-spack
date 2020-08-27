# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Nanocernlib(CMakePackage):
    """nanocernlib is a collection of commonly used cernlib routines
    packaged with cmake to easily build on modern systems."""

    homepage = "http://github.com/sly2j/nanocernlib"
    url      = "http://github.com/sly2j/nanocernlib"
    git      = "http://github.com/sly2j/nanocernlib.git"

    version('master', branch='master')

    depends_on('cmake', type='build')
