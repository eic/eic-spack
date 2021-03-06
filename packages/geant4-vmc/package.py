# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Geant4Vmc(CMakePackage):
    """Geant4 Virtual Monte Carlo."""

    homepage = "http://github.com/vmc-project/geant4_vmc"
    url      = "http://github.com/vmc-project/geant4_vmc/archive/v5-1-p1.tar.gz"
    git      = "http://github.com/vmc-project/geant4_vmc.git"

    maintainer = ['wdconinc']

    version('master', branch='master')
    version('5-1-p1', sha256='2e3e4705134ea464e993156f71d478cb7d3817f5b6026bf8d9a37d32ec97590b')
    version('5-1',    sha256='ede71f360397dc4d045ec0968acf23b564fa81059c94eb40942b552eea8b5e00')
    version('5-0-p3', sha256='91df73e992bf9ae7e1b6b3c3deb12cd6661c7dd5153fa233eb28b8d8e1164ccb')
    version('5-0-p2', sha256='34578c5468173615de3fc077e85be3bf68f4aff4b4f37523ab67304dbc153d5f')
    version('5-0-p1', sha256='b66cbf86a96b6efe1643753a7606b1c4ebb9d45cca9f6b8e933762920f32831f')
    version('5-0',    sha256='9a3820ea4b68b5a0697c340bbbc0972b9c8e4205ceecdd87258a9bdfd249cd8b')
    version('4-0-p3', sha256='ec6699aa0deca903f143c593affec09832c33be736d9cddfa8d6f5cdfc3bc288')
    version('4-0-p2', sha256='cdd73c499cd296f13b6c0d37e161e7d94343f85617b2a7577ded8312248f9b9b')
    version('3-6-p6', sha256='e62a62ff7075ff9afb2ffe420610374f62136094a447bbbc5f739a2238ddb0f0')

    depends_on('cmake@3.3:', type='build')
    depends_on('geant4')
    depends_on('vmc')
