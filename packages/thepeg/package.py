# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Thepeg(AutotoolsPackage):
    """ThePEG is a Toolkit for High Energy Physics Event Generation."""

    homepage = "https://thepeg.hepforge.org/"
    url      = "https://thepeg.hepforge.org/downloads/ThePEG-2.2.1.tar.bz2"

    maintainers = ['wdconinc']

    version('2.2.1', sha256='63abc7215e6ad45c11cf9dac013738e194cc38556a8368b850b70ab1b57ea58f')

    depends_on('zlib')
    depends_on('fastjet')
    depends_on('hepmc')
    depends_on('lhapdf')
    #depends_on('rivet')

    def configure_args(self):
        args = []
        args.append('--with-lhapdf=' + self.spec['lhapdf'].prefix)
        args.append('--with-hepmc=' + self.spec['hepmc'].prefix)
        return args
