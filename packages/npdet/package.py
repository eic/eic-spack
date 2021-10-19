from spack import *


class Npdet(CMakePackage):
    """Nuclear Physics Detector library."""

    homepage = "https://eicweb.phy.anl.gov/EIC/NPDet"
    url      = "https://eicweb.phy.anl.gov/EIC/NPDet/-/archive/v0.5.0/NPDet-v0.5.0.tar.gz"
    list_url = "https://eicweb.phy.anl.gov/EIC/NPDet/-/tags"
    git      = "https://eicweb.phy.anl.gov/EIC/NPDet"

    maintainers = ['wdconinc']

    tags = ['eic']

    version('master', branch='master', preferred=True)
    version('1.0.0', sha256='e0522dd2a6c163367e8ad4bc12ba9ad5a58d99ea151192df3ab48228a754b490')
    version('0.9.0', sha256='0cb0e6e39956c6751b00d53e7d44007e71c41728ee97bc785664f2416fe051f4')
    version('0.8.0', sha256='89cec16c44e9ac3b009d2fbf3817b0df7dabafe1a34b0b0160183a6431a6fbed')
    version('0.7.0', sha256='d842d5571960316e76530849fa03296dc270d90da48d557bf4bd2c358538eefe')
    version('0.6.0', sha256='0b1adbb3aff5d8b8ef9c6e81ec63721bdf12f4c457465bfd584ddeba63161edd')
    version('0.5.0', sha256='2ff4cd7992b7c18c25da64aa2d6223c210ea50c5ce90bcb007c0346cb4aee2c5')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    variant('geocad', default=False,
            description='Build the geocad interface')

    depends_on('fmt')
    depends_on('acts')
    depends_on('eigen')
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
