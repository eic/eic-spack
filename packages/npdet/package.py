from spack import *


class Npdet(CMakePackage):
    """Nuclear Physics Detector library."""

    homepage = "https://eicweb.phy.anl.gov/EIC/NPDet"
    url      = "https://eicweb.phy.anl.gov/EIC/NPDet/-/archive/v0.5.0/NPDet-v0.5.0.tar.gz"
    git      = "https://eicweb.phy.anl.gov/EIC/NPDet"

    maintainers = ['wdconinc']

    version('master', branch='master')
    version('0.5.0', sha256='2ff4cd7992b7c18c25da64aa2d6223c210ea50c5ce90bcb007c0346cb4aee2c5')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    variant('geocad', default=False,
            description='Build the geocad interface')

    depends_on('fmt')
    depends_on('acts')
    depends_on('root +http', when='@:0.5.8')
    depends_on('podio')
    depends_on('dd4hep +geant4')
    depends_on('opencascade', when='+geocad')

    def cmake_args(self):
        args = [
            self.define_from_variant('USE_GEOCAD', 'geocad')
        ]
        args.append('-DCMAKE_CXX_STANDARD=17')
        return args

