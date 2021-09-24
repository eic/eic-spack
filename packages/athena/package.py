from spack import *


class Athena(CMakePackage):
    """The ATHENA Detector at IP6 of the Electron-Ion Collider."""

    homepage = "https://athena-eic.org"
    url      = "https://eicweb.phy.anl.gov/EIC/detectors/athena"
    git      = "https://eicweb.phy.anl.gov/EIC/detectors/athena"

    maintainers = ['wdconinc']

    version('master', branch='master')

    depends_on('dd4hep +geant4')
    depends_on('acts +dd4hep +identification +tgeo')
