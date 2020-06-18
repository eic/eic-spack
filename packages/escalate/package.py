# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Escalate(BundlePackage):
    """EIC Softare Consortium environment."""

    homepage = "http://gitlab.com/eic/escalate"

    version('1.0.1')
    depends_on('root@6.20.04',when='@1.0.1')
    depends_on('geant4@10.6.1',when='@1.0.1')

