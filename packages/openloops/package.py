# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Openloops(SConsPackage):
    """The OpenLoops 2 program is a fully automated implementation of
    the Open Loops algorithm combined with on-the-fly reduction methods,
    which allows for the fast and stable numerical evaluation of tree
    and one-loop matrix elements for any Standard Model process at NLO
    QCD and NLO EW."""

    homepage = "https://openloops.hepforge.org"
    url      = "https://openloops.hepforge.org/downloads?f=OpenLoops-2.1.1.tar.gz"

    maintainers = ['wdconinc']

    version('2.1.1', sha256='f1c47ece812227eab584e2c695fef74423d2f212873f762b8658f728685bcb91')

    depends_on('scons@2.3.0:', type='build')
    depends_on('python@3.5.0:')

    def build_args(self, spec, prefix):
        args = []
        return args
