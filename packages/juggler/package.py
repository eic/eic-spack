from spack import *


class Juggler(CMakePackage):
    """Concurrent event processor for NP experiments, based on the Gaudi framework."""

    homepage = "https://eicweb.phy.anl.gov/EIC/juggler"
    url      = "https://eicweb.phy.anl.gov/EIC/juggler/-/archive/v1.8.0/juggler-v1.8.0.tar.gz"
    git      = "https://eicweb.phy.anl.gov/EIC/juggler.git"
    list_url = "https://eicweb.phy.anl.gov/EIC/juggler/-/tags"

    maintainers = ['wdconinc']

    tags = ['eic']

    version('master', branch='master')
    version('7.0.0', sha256='c30cf91d7424340f2b36093a3538d25c700f2191cd0da0d3dccfa83bdc996826')
    version('6.1.0', sha256='1ab310910f7e8f6178edc994b66305bf4b3cb4a6eaa93833b662155008e2b119')
    version('6.0.0', sha256='645fc7a45fa73f154b7919d292d9d5b8a864df488a8526c054edb18b90c1fd99')
    version('5.0.0', sha256='326f36cf1421dc1bbfa8bbe485b0741037c3da5228f75dd75fa56e84b233003b')
    version('4.4.0', sha256='da901f786b570db25aa52071ff942118db958b2c13bf1c41a236905e2022c49a')
    version('4.3.0', sha256='d10bb8179514245f358a05efb4ddad0ea6b4bf8d9f20b50b0ac14165d4d95449')
    version('4.2.0', sha256='e3277ff67e726127c92233d7f7989af54b9f12bf1621bc4e7d571100394f3f02')
    version('4.1.0', sha256='90aec3cfff6b01a7937c421037ff8ec9cc30c7c7ad7739f646776c997f0a8e57')
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

    variant('cxxstd',
            default='17',
            values=('17', '20'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('root')
    depends_on('geant4')
    depends_on('genfit')
    depends_on('dd4hep +ddg4')
    depends_on('tensorflow-lite')

    depends_on('gaudi', when='@master')
    depends_on('gaudi@36', when='@2:')
    depends_on('gaudi@33:34', when='@:1.8')
    
    depends_on('acts +identification +json +tgeo +dd4hep')
    depends_on('acts@15.1:19', when='@master')
    depends_on('acts@15.1:19', when='@5')
    depends_on('acts@9:14', when='@4')
    depends_on('acts@8', when='@3')
    
    depends_on('podio@0.11.0:')

    depends_on('edm4hep')

    depends_on('eicd')
    depends_on('eicd@master', when='@master')
    depends_on('eicd@2:', when='@6:')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(self.define('CMAKE_CXX_STANDARD',
                    self.spec.variants['cxxstd'].value))
        return args
