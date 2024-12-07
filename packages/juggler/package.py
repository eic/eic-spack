from spack.package import *


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
    version("10.1.0", sha256="d31d80db3829dea46f5909e7978e7be72968f8d38c847b0f4c59abc2953efcde")
    version("10.0.1", sha256="2ce73fb46191a457c4f0fcaf1c8d84f9686665ab94654946d53fa8616c73195a")
    version("10.0.0", sha256="8436aa9c083e50ea2cb18e64d5c1821607b9251e16115ee799c64925f7c9756d")
    version("9.4.0", sha256="f1e76f2bd8799a0555352de472cf58c55c2ba27388ad5a8522889169b8341263")
    version(
        "9.3.0",
        sha256="2ce7c36b38a1041c1a80c2e0f16d12759881a0337eac1fcd78277093151b2b94",
    )
    version(
        "9.2.0",
        sha256="265917ace308fa08a2158ca93fe308a7af15008780f81abc443e7cbea90c4f39",
    )
    version(
        "9.1.0",
        sha256="76545542032b723ccfda31f5f293c41b9dda89c0cd86431c69f6ce15b5dd8733",
    )
    version(
        "9.0.0",
        sha256="59e4e0871303e25fdba058742854a6a99d62f847becd03d1141c64c05746498d",
    )
    version(
        "8.0.2",
        sha256="cac26f6e9658dc94cce59b11cc4bef6b71c1575ccda3eaf798f8cab03da877bb",
    )
    version(
        "8.0.1",
        sha256="c85f633ca17f9690aed9a30592efbadd0b2223d8064d9dd01de29988402812ea",
    )
    version(
        "8.0.0",
        sha256="498734a4e776e2ab9b6adafa827ca2f09895e64dbf6685281d4b894ed123566b",
    )
    version(
        "7.0.0",
        sha256="c30cf91d7424340f2b36093a3538d25c700f2191cd0da0d3dccfa83bdc996826",
    )
    version(
        "6.1.0",
        sha256="1ab310910f7e8f6178edc994b66305bf4b3cb4a6eaa93833b662155008e2b119",
    )
    version(
        "6.0.0",
        sha256="645fc7a45fa73f154b7919d292d9d5b8a864df488a8526c054edb18b90c1fd99",
    )
    version(
        "5.0.0",
        sha256="326f36cf1421dc1bbfa8bbe485b0741037c3da5228f75dd75fa56e84b233003b",
    )
    version(
        "4.4.0",
        sha256="da901f786b570db25aa52071ff942118db958b2c13bf1c41a236905e2022c49a",
    )
    version(
        "4.3.0",
        sha256="d10bb8179514245f358a05efb4ddad0ea6b4bf8d9f20b50b0ac14165d4d95449",
    )
    version(
        "4.2.0",
        sha256="e3277ff67e726127c92233d7f7989af54b9f12bf1621bc4e7d571100394f3f02",
    )
    version(
        "4.1.0",
        sha256="90aec3cfff6b01a7937c421037ff8ec9cc30c7c7ad7739f646776c997f0a8e57",
    )
    version(
        "4.0.0",
        sha256="0e6a4d88e4dacd2e2f5b930d716d2f96353df57e44ec18603299172112252c91",
    )
    version(
        "3.6.0",
        sha256="2c843682a2a81667399254931b6222c98af3e65f24d0cc456a70de96be0c07bf",
    )
    version(
        "3.5.0",
        sha256="6730db099cd1b9f52b70417184bc348dce53de18e4d8f861038560e94de02d66",
    )
    version(
        "3.4.0",
        sha256="1cd35ec7aa92bdbeb85ab2d6b224272bc37d6bd8ce574b8ac7e60dd91d74f367",
    )
    version(
        "3.3.1",
        sha256="6e7b579a45d098befdb6b90f97cfeaaf2e7c05094a8b5c5095e9b3b1c9baa83e",
    )
    version(
        "3.3.0",
        sha256="717981df887273b1309bcc382796d8f8fc495250f0e385e58f1e0888a8d8d064",
    )
    version(
        "3.2.0",
        sha256="ce819299b407f2a008a0e6d2b8717fca7c8d55c8ae35d774c3bc5f965a36fdae",
    )
    version(
        "3.1.0",
        sha256="693e30c73d433b03bf450fa48c99dbfe5a036fcda0991b65f85a840899817cd6",
    )
    version(
        "3.0.0",
        sha256="dbee46ff5c34f33ad110f581192b7b3789f10706c05fde2cd50212d4d96bef6b",
    )
    version(
        "2.0.0",
        sha256="3f45c627a9ee08fbefca1fdbbf23adfa96665a62a350439176d39318daf2bb6d",
    )
    version(
        "1.8.0",
        sha256="b0259a0c59c6b46007d15c1d72a839006962b0720a5299b12ea11848b87bcf49",
    )
    version(
        "1.6.0",
        sha256="dca4f824a1c1d360b4bd795e6fb0353b8729318a3a0781a8ae0dcf745ae82f02",
    )
    version(
        "1.5.0",
        sha256="e2fe06730949766a32b08200101822fe8a145634fa46b09c6057cb321350cf57",
    )

    variant(
        "cxxstd",
        default="20",
        values=(conditional("17", when="@:11"), "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("cxx", type="build")

    depends_on("root")
    depends_on("geant4")
    depends_on("genfit", when="@:8")
    depends_on("dd4hep +ddg4")

    depends_on("gaudi", when="@master")
    depends_on("gaudi@36:", when="@2:")
    depends_on("gaudi@33:34", when="@:1.8")

    depends_on("acts +json +tgeo +dd4hep", when="@14.2:")
    depends_on("acts +identification +json +tgeo +dd4hep", when="@:14.1")
    depends_on("acts", when="@main")
    depends_on("acts@30:", when="@11:")
    depends_on("acts@20.2:21", when="@9.1:10")
    depends_on("acts@19.9:19", when="@9.0")
    depends_on("acts@19:19.8", when="@7:8")
    depends_on("acts@15.1:19", when="@5:6")
    depends_on("acts@9:14", when="@4")
    depends_on("acts@8", when="@3")

    depends_on("podio@0.11.0:")
    conflicts("podio@0.99:", when="@:14.0.1")

    depends_on("edm4hep")

    depends_on("eicd", when="@:7")
    depends_on("eicd@2:", when="@6:7")

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
