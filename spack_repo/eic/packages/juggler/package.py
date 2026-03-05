from spack.package import *
from spack_repo.builtin.build_systems.cmake import CMakePackage


class Juggler(CMakePackage):
    """Concurrent event processor for NP experiments, based on the Gaudi framework."""

    homepage = "https://eicweb.phy.anl.gov/EIC/juggler"
    url = (
        "https://eicweb.phy.anl.gov/EIC/juggler/-/archive/v1.8.0/juggler-v1.8.0.tar.gz"
    )
    git = "https://github.com/eic/juggler.git"
    list_url = "https://eicweb.phy.anl.gov/EIC/juggler/-/tags"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("main", branch="main")
    version("master", branch="master", deprecated=True)
    version("15.1.0", sha256="c5d6ac5e136cb95ba1288c724a0f53ba719af22a1c6f24ee315d4779e0d43665")
    version("15.0.5", sha256="b415c29f3f6d17a7c40a018a2f39b14fad2e3438f47ade21955f2a532ebb9830")
    version("15.0.4", sha256="64f7638235d1a84faf0451e2138ef7dac1b0e571965918d8e19413684fcb681e")
    version("15.0.3", sha256="44edeca4439483459e0617f445543eb7c49cfd66a845326a6610bf5369c8b637")
    version("15.0.2", sha256="0b31fa2d3a94b2448f53d46525f09e564dce36e1679fb3e798469875c5ede957")
    version("15.0.1", sha256="9754887d2bcee2549d6cdf824b03c6cf5ffc22265a69cc095ebcdb3bd4572478")
    version("15.0.0", sha256="b620175e706da931520367b9c010d728f73f86fa7ae8a37e79d7494e7a0fa490")
    version("14.3.0", sha256="46d19d69a951638c4bcdb3ad99def08eb21d4991894ff5b11e3d0d4479f52985")
    version("14.2.2", sha256="fab54810bee8437cf8c51c4991888be223956b206e0271668e641f363c403084")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("root")
    depends_on("geant4")
    depends_on("dd4hep +ddg4")

    depends_on("gaudi", when="@master")
    depends_on("gaudi@36:")

    depends_on("acts +json +dd4hep", when="@15.0.4:")
    depends_on("acts +json +tgeo +dd4hep", when="@14.2:15.0.3")
    depends_on("acts", when="@main")
    depends_on("acts@30:")

    depends_on("podio@0.11.0:")
    conflicts("^podio@1.5:", when="@:15.0.2")

    depends_on("edm4hep")
    conflicts("^edm4hep@0.99:", when="@:15.0.0")

    depends_on("edm4eic")

    depends_on("cppgsl")

    depends_on("k4fwcore")
    depends_on("k4actstracking")

    depends_on("algorithms")
    depends_on("eicrecon")

    def cmake_args(self):
        args = []
        args.append(self.define("CMAKE_CXX_STANDARD", "20"))
        return args
