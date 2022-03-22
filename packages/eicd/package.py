from spack import *


class Eicd(CMakePackage):
    """A podio based data model for the EIC."""

    homepage = "https://eicweb.phy.anl.gov/EIC/eicd"
    url      = "https://eicweb.phy.anl.gov/EIC/eicd/-/archive/v0.2.0/eicd-v0.2.0.tar.gz"
    git      = "https://eicweb.phy.anl.gov/EIC/eicd.git"
    list_url = "https://eicweb.phy.anl.gov/EIC/eicd/-/tags"

    maintainers = ['wdconinc']

    tags = ['eic']

    version('master', branch='master')
    version('2.0.0', sha256='2f74e82e2877e267405f9a0f518166e666c3901ed5d65f0b35cdb98629bab682')
    version('1.1.0', sha256='67595efcbf44044c71b7774ee579efae7122066eb4137cdc2549508cdcea7adf')
    version('1.0.0', sha256='32d800e6ed6cf869b3cf2c26a57ee9571ca1a1533e81ae44e5bfb46f95c45fea')
    version('0.9.0', sha256='f9ec441fe9e3d1a7bedb96a75e97a3ee32fb72f94c26114f2c252618d36009f3')
    version('0.8.0', sha256='140b191c7bb64d5fc7c039b646ade9ecfeb00509ad19eb04917cd6f2ace3b1d1')
    version('0.7.0', sha256='12458ed06d3f7d3f17852637d8b7f6c406e8ffb24b487d690be81d342a0c0e75')
    version('0.6.0', sha256='e44a7535ce0e94bfa4df0676ffc3af90b9ed90626cb4b524860576848bfc9ed7')
    version('0.5.0', sha256='597b22a7d8b1ba9d1f3c0facee8f8df95cc4d4baa9d9c7f1a624dfa13b48751b')
    version('0.2.0', sha256='3e52e19bdfbda67454786080db678107a00b932b4cf26bfd95bbf764cc1f7fc9')
    version('0.1.0', sha256='814eec1b6c27e46fdedfd3f42d846366c6170c3b1c7b5225c28465d0861b612c')

    depends_on('python', type='build')
    depends_on('cmake@3.3:', type='build')
    depends_on('py-jinja2', type='build')
    depends_on('py-pyyaml', type='build')

    depends_on('edm4hep@0.4.1:', when='@2:')
    depends_on('edm4hep@:0.4', when='@:1')
    depends_on('podio@0.14.1:', when='@2:')
    depends_on('podio@0.11.0:0.14.0', when='@:1')
    depends_on('root@6.08:')
