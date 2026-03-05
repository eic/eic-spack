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
    version("14.2.1", sha256="4a2e1290b4d58f36df5c9c03c1c941e79f518c489648b4c1be067974f041eecf")
    version("14.2.0", sha256="b40e93e50d6ae57c8c73a5166ee4c1694bd2ef0018e545302d11369f4e89a0b6")
    version("14.1.0", sha256="c23cec2a77d9099f6574540116b8dc9c190537721b3fd1dfcce9d30e8b4ef410")
    version("14.0.3", sha256="2b163f5f1a8b087a3f0831f8074fe5a5831ad3d2f900c05ae097e1c7ec17d3aa")
    version("14.0.2", sha256="78825e34a2db2f99360c1c57a3e24d1fcad2c22b7b17e703c8b693944ebca5e2")
    version("14.0.1", sha256="55efe028ea9c70c2fbb4a33d83126f11f75b04396987c2e55a2b2fd055ca34c8")
    version("14.0.0", sha256="b5a6ec1960868464de530c3d508bee5378a2bfe23ef3afa0d38ad66ddf2bc977")
    version("13.0.0", sha256="5c967e5979b540ccdc64f94f371b9bb9056ff470c3691e8bda0f12b74702feb2")
    version("12.0.0", sha256="a1c85bc4fdfe894c6f3dfe3b55f4a02a1c45db0db085d5044a626034d5308f42")
    version("11.0.0", sha256="f3a4399387160796f23fb672714eb77f56063f8ebee56d16de9df38f7edc136e")

    variant(
        "cxxstd",
        default="20",
        values=(conditional("17", when="@:11"), "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("root")
    depends_on("geant4")
    depends_on("dd4hep +ddg4")

    depends_on("gaudi", when="@master")
    depends_on("gaudi@36:", when="@2:")
    conflicts("^gaudi@37:38 ~gaudialg", when="@:14", msg="GaudiAlgLib required through v14")

    depends_on("acts +json +dd4hep", when="@15.0.4:")
    depends_on("acts +json +tgeo +dd4hep", when="@14.2:15.0.3")
    depends_on("acts +json +tgeo +dd4hep", when="@:14.1")
    depends_on("acts", when="@main")
    depends_on("acts@30:", when="@11:")

    depends_on("podio@0.11.0:")
    conflicts("^podio@1.5:", when="@:15.0.2")
    conflicts("^podio@0.99:", when="@:14.0.1")

    depends_on("edm4hep")
    conflicts("^edm4hep@0.99:", when="@:15.0.0")

    depends_on("edm4eic", when="@8:")

    depends_on("cppgsl")

    depends_on("k4fwcore", when="@13:")
    depends_on("k4actstracking", when="@13:")

    depends_on("algorithms", when="@14:")
    depends_on("eicrecon", when="@14:")  # FIXME update to start at 15: when released

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            self.define("CMAKE_CXX_STANDARD", self.spec.variants["cxxstd"].value)
        )
        return args
