# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import glob


class Sartre(CMakePackage):
    """Sartre is an event generator for exclusive diffractive vector
    meson production and DVCS in ep and eA collisions based on the
    dipole model."""

    homepage = "http://sartre.hepforge.org/"
    url      = "http://sartre.hepforge.org/downloads/?f=sartre-1.33-src.tgz"

    variant('kmw',  default=True,  description='Install data tables with KMW parameters (170 MB)')
    variant('hpmz', default=False, description='Install data tables with HPMZ parameters (1.9 GB)')

    resource(
        name='tables-KMW.gz',
        url='https://rhig.physics.yale.edu/~ullrich/sartre-tables/tables-KMW.gz',
        sha256='0b8718766496c2b730b74a22ebb0053ffbc311d4a84a1f5ac8c755eeaf7e3ac7',
        destination='.',
        extension='tar.gz',
        when='+kmw'
    )
    resource(
        name='tables-HPMZ.gz',
        url='https://rhig.physics.yale.edu/~ullrich/sartre-tables/tables-HPMZ.gz',
        sha256='8933853f37973bc7ec7448fcaa7c93b4491337eb4a0b28e8d3bd05aefc464e55',
        destination='.',
        extension='tar.gz',
        when='+hpmz'
    )

    version('1.33', sha256='f010dd6a9b4c310d9bf1ea7507eb91f179b0f0e676fc67112e249233554e3b01')

    depends_on('gsl')
    depends_on('root')

    def patch(self):
        # Collect all CMakeLists.txt
        makefiles = glob.glob('**/CMakeLists.txt', recursive=True)
        # Remove explicit sartre directory from install prefix
        filter_file('DESTINATION sartre/',
                    'DESTINATION ${CMAKE_INSTALL_PREFIX}/',
                    *makefiles)
        filter_file('DESTINATION \$\{CMAKE_INSTALL_PREFIX\}/sartre',
                    'DESTINATION ${CMAKE_INSTALL_PREFIX}/',
                    *makefiles)
