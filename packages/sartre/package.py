# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Sartre(CMakePackage):
    """Sartre is an event generator for exclusive diffractive vector
    meson production and DVCS in ep and eA collisions based on the
    dipole model."""

    homepage = "http://sartre.hepforge.org/"
    url      = "http://sartre.hepforge.org/downloads/?f=sartre-1.33-src.tgz"

    variant('kmw',  default=True,  description='Install data tables with KMW parameters')
    variant('hpmz', default=False, description='Install data tables with HPMZ parameters')

    resource(
        name='tables-KMW.gz',
        url='https://rhig.physics.yale.edu/~ullrich/sartre-tables/tables-KMW.gz',
        sha256='0b8718766496c2b730b74a22ebb0053ffbc311d4a84a1f5ac8c755eeaf7e3ac7',
        destination='tables',
        when='+kmw'
    )
    resource(
        name='tables-HPMZ.gz',
        url='https://rhig.physics.yale.edu/~ullrich/sartre-tables/tables-HPMZ.gz',
        sha256='0b8718766496c2b730b74a22ebb0053ffbc311d4a84a1f5ac8c755eeaf7e3ac7', # FIXME
        destination='tables',
        when='+hpmz'
    )

    version('1.33', sha256='f010dd6a9b4c310d9bf1ea7507eb91f179b0f0e676fc67112e249233554e3b01')

    depends_on('gsl')
    depends_on('root')
