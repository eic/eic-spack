# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Nanocernlib(CMakePackage):
    """nanocernlib is a collection of commonly used cernlib routines
    packaged with cmake to easily build on modern systems."""

    homepage = "http://github.com/sly2j/nanocernlib"
    url      = "https://github.com/sly2j/nanocernlib/archive/v1.0.0.tar.gz"
    git      = "http://github.com/sly2j/nanocernlib.git"

    version('master', branch='master')
    version('1.0.0', sha256='00b23d2613272951c1771d917ec0a7c30920e9d114caf1b421c44a806a06356a')

    depends_on('cmake', type='build')
