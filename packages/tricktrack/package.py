##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Tricktrack(CMakePackage):
    """TrickTrack aims to encapsulate the Cellular-Automaton based
    seeding code used in CMSSW in a standalone library."""

    homepage = "https://cern.ch/tricktrack"
    url      = "https://github.com/HEP-SF/TrickTrack/archive/v1.0.4.tar.gz"

    version('1.0.9', sha256='988cedbb28ec8f5cc95b762aa8a38e36d75cfc47bd009c9dc4ef365e9751b80d')
    version('1.0.8', sha256='fe5f8d178f8a0a28ac423ad6e9c449772ba547ec3ef7e365c4644d9b5b44cf85')
    version('1.0.7', sha256='e567de7c3c6e8096bd77873ac59fc4667661cdb380d089dcd6443a9d9834f3ef')
    version('1.0.6', sha256='c7c5d6c492f65acd020a600664c5fa75c5caf9de33bb392f46771abad7650398')
    version('1.0.5', sha256='5fe3f9ac523ca2381b11aef57057ec75b85aa9ee0a3fb6bac4710d2c76961692')
    version('1.0.4', sha256='de4b1245a94e0905bcb9387e4a3b675298de916e631d3136f32ac1ab9e01855d')
    version('1.0.1', sha256='4b7fbd3734a5ef30a3abecaf7b15318a1856ff31fac822775035e00669dc921d')

    depends_on('cmake@3.2:', type='build')
    depends_on('eigen', when="@1.0.4:")

    patch('eigen.patch', when="@1.0.4")
    patch('findeigen.patch', when="@1.0.4")
