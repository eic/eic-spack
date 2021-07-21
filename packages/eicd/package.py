from spack import *


class Eicd(CMakePackage):
    """A podio based data model for the EIC."""

    homepage = "https://eicweb.phy.anl.gov/EIC/eicd"
    url      = "https://eicweb.phy.anl.gov/EIC/eicd/-/archive/v0.2.0/eicd-v0.2.0.tar.gz"
    git      = "https://eicweb.phy.anl.gov/EIC/eicd.git"

    maintainers = ['wdconinc']

    version('master', branch='master')
    version('0.2.0', sha256='3e52e19bdfbda67454786080db678107a00b932b4cf26bfd95bbf764cc1f7fc9')

    depends_on('podio@0.11.0:')
    depends_on('root')
