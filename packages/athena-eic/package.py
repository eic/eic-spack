from spack import *


class AthenaEic(CMakePackage):
    """The ATHENA Detector at IP6 of the Electron-Ion Collider."""

    homepage = "https://athena-eic.org"
    url      = "https://eicweb.phy.anl.gov/EIC/detectors/athena/-/archive/v0.2.0/athena-v0.2.0.tar.gz"
    list_url = "https://eicweb.phy.anl.gov/EIC/detectors/athena/-/tags"
    git      = "https://eicweb.phy.anl.gov/EIC/detectors/athena"

    maintainers = ['wdconinc']

    version('master', branch='master', preferred=True)
    version('0.2.0', sha256='188ed1e46196c7cb2474ec0e3a653e32bf781c464c68d6a15c26bddc51293999')
    version('0.1.0', sha256='34ab3c99e833ca6e674ae69d36c11b242413def06fb9a31735ffe43cac2989de')

    variant('ip', default='6', values=('6'),
            description='Interaction point design')
    variant('reconstruction', default=False,
            description='Depend on reconstruction libraries')

    depends_on('dd4hep +geant4')
    depends_on('acts +dd4hep +identification +tgeo')
    depends_on('athena-ip6', when='ip=6')
    depends_on('juggler', when='reconstruction')
