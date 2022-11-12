from spack import *


class Edm4eic(CMakePackage):
    """A data model for EIC defined with podio and based on EDM4hep."""

    homepage = "https://github.com/eic/EDM4eic"
    url      = "https://github.com/eic/EDM4eic/archive/refs/tags/v1.0.0.tar.gz"
    git      = "https://github.com/eic/EDM4eic.git"
    list_url = "https://github.com/eic/EDM4eic/tags"

    maintainers = ['wdconinc']

    tags = ['eic']

    version('main', branch='main')
    version("1.2.1", sha256="8349864f5c923e991d31462cc7987cd39c050910d4db8847575c8d4fd61967a5")
    version("1.2.0", sha256="e70ec6d2a93002237c1bfd0046e96f3838f9dab3f5326bdb17826999b5f42759")
    version("1.1.0", sha256="f50a6ef77d8247aa30da5b1e574bb24ab82c86c8706a8f3900ff151dafe9a754")
    version("1.0.1", sha256="683dcd463757f9e4ad47e493be1f5fb40a6c1aae7d249ff18a19367384a61070")
    version("1.0.0", sha256="700ae7453f16786db4d3ace1a146914e1f0b935a08039c9f1f6a5ebe4aa173ae")

    variant('cxxstd',
            default='17',
            values=('17', '20'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('python', type='build')
    depends_on('cmake@3.3:', type='build')
    depends_on('py-jinja2', type='build')
    depends_on('py-pyyaml', type='build')

    depends_on('edm4hep@0.4.1:', when='@1:')
    depends_on('podio@0.15:', when='@1:')
    depends_on('root@6.08:')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(self.define('CMAKE_CXX_STANDARD',
                    self.spec.variants['cxxstd'].value))
        return args
