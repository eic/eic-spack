from spack import *


class Juggler(CMakePackage):
    """Concurrent event processor for NP experiments, based on the Gaudi framework."""

    homepage = "https://eicweb.phy.anl.gov/EIC/juggler"
    url      = "https://eicweb.phy.anl.gov/EIC/juggler/-/archive/v1.8.0/juggler-v1.8.0.tar.gz"
    git      = "https://eicweb.phy.anl.gov/EIC/juggler.git"
    list_url = "https://eicweb.phy.anl.gov/EIC/juggler/-/tags"

    maintainers = ['wdconinc']

    version('master', branch='master', preferred=True)
    version('4.0.0', sha256='0e6a4d88e4dacd2e2f5b930d716d2f96353df57e44ec18603299172112252c91')
    version('3.6.0', sha256='2c843682a2a81667399254931b6222c98af3e65f24d0cc456a70de96be0c07bf')
    version('3.5.0', sha256='6730db099cd1b9f52b70417184bc348dce53de18e4d8f861038560e94de02d66')
    version('3.4.0', sha256='1cd35ec7aa92bdbeb85ab2d6b224272bc37d6bd8ce574b8ac7e60dd91d74f367')
    version('3.3.1', sha256='6e7b579a45d098befdb6b90f97cfeaaf2e7c05094a8b5c5095e9b3b1c9baa83e')
    version('3.3.0', sha256='717981df887273b1309bcc382796d8f8fc495250f0e385e58f1e0888a8d8d064')
    version('3.2.0', sha256='ce819299b407f2a008a0e6d2b8717fca7c8d55c8ae35d774c3bc5f965a36fdae')
    version('3.1.0', sha256='693e30c73d433b03bf450fa48c99dbfe5a036fcda0991b65f85a840899817cd6')
    version('3.0.0', sha256='dbee46ff5c34f33ad110f581192b7b3789f10706c05fde2cd50212d4d96bef6b')
    version('2.0.0', sha256='3f45c627a9ee08fbefca1fdbbf23adfa96665a62a350439176d39318daf2bb6d')
    version('1.8.0', sha256='b0259a0c59c6b46007d15c1d72a839006962b0720a5299b12ea11848b87bcf49')
    version('1.6.0', sha256='dca4f824a1c1d360b4bd795e6fb0353b8729318a3a0781a8ae0dcf745ae82f02')
    version('1.5.0', sha256='e2fe06730949766a32b08200101822fe8a145634fa46b09c6057cb321350cf57')

    depends_on('gaudi@36.0:', when='@master')
    depends_on('gaudi@36.0:36.99', when='@2.0.0:')
    depends_on('gaudi@33.0:34.99', when='@1.8.0:1.8.99')
    depends_on('acts@9: +identification +tgeo +dd4hep', when='@4:')
    depends_on('acts@:8 +identification +tgeo +dd4hep', when='@:3')
    depends_on('podio@0.11.0:')
    depends_on('npdet')
    depends_on('eicd')
    depends_on('root')
    depends_on('geant4')
    depends_on('genfit')
    depends_on('dd4hep +geant4')

