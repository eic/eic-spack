from spack import *


class AthenaIp6(CMakePackage):
    """The ATHENA Beamline at IP6 of the Electron-Ion Collider."""

    homepage = "https://athena-eic.org"
    url      = "https://eicweb.phy.anl.gov/EIC/detectors/ip6/-/archive/v0.4.0/ip6-v0.4.0.tar.gz"
    list_url = "https://eicweb.phy.anl.gov/EIC/detectors/ip6/-/tags"
    git      = "https://eicweb.phy.anl.gov/EIC/detectors/ip6"

    maintainers = ['wdconinc']

    tags = ['eic']

    version('master', branch='master')
    version('1.0.0', sha256='f387f049e8b4c25238dcaca29965c74445f83979ff56de44ef3b8df8d0893723')
    version('0.6.2', sha256='c5daf21952823356aacadc183a71a1888bda6734f48938c61a7c54ae73e40231')
    version('0.6.1', sha256='df111e1596f65f0d43555ea4d7a31e21199be34a68e481f884350a22792ab433')
    version('0.6.0', sha256='d44889f446aab78b28f9851d95e7ce1105f89c6034513b96c6cd7e3e50a03289')
    version('0.5.2', sha256='922ed7a54922cfc1db0295647b36a5d8e3cfbb5e01b2024d70a7ed9b7503a813')
    version('0.5.1', sha256='54c647df98a4a8e0926f75a03ac4e0914b92ba69d09f2a86be090cf972cc25b5')
    version('0.5.0', sha256='95d1b90cf00bb9eb62bd6f4569698b69621e9ed8bcbd51e572bc7d40db06e9f3')
    version('0.4.0', sha256='6612d23f885e891ffeb51bf5d1b18221f24ef76f061433fac23e91b030f97808')
    version('0.3.0', sha256='e584e8caf466c6686b379142e7379637c6fd410eaa0247ef41d79cc63a55667d')
    version('0.2.0', sha256='91d6838d67fce6ce2920409cb1b7b9ad817de4805e9a273b0340fcbe64cb5ae8')
    version('0.1.0', sha256='5b8300100be6ac9cbc797fa5d1a9532a16d1055ff4f39e94ec9613c9321b970c')

    depends_on('dd4hep +geant4')
    depends_on('acts +dd4hep +tgeo')
    depends_on('root +gdml')

    def setup_run_environment(self, env):
        env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib)
