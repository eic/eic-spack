from spack import *


class Juggler(CMakePackage):
    """Concurrent event processor for NP experiments, based on the Gaudi framework."""

    homepage = "https://eicweb.phy.anl.gov/EIC/juggler"
    url      = "https://eicweb.phy.anl.gov/EIC/juggler/-/archive/v1.8.0/juggler-v1.8.0.tar.gz"
    git      = "https://eicweb.phy.anl.gov/EIC/juggler.git"

    maintainers = ['wdconinc']

    version('master', branch='master')
    version('1.8.0', sha256='b0259a0c59c6b46007d15c1d72a839006962b0720a5299b12ea11848b87bcf49')

    depends_on('gaudi@33.0:34.0')
    depends_on('acts@8.01.0: +identification +geant4 +tgeo +dd4hep')
    depends_on('podio@0.11.0:')
    depends_on('npdet')
    depends_on('eicd')
    depends_on('root +geo')
    depends_on('geant4')
    depends_on('genfit')
    depends_on('dd4hep +geant4')

