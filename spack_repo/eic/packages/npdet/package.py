from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Npdet(CMakePackage):
    """Nuclear Physics Detector library."""

    homepage = "https://eicweb.phy.anl.gov/EIC/NPDet"
    url = "https://eicweb.phy.anl.gov/EIC/NPDet/-/archive/v0.5.0/NPDet-v0.5.0.tar.gz"
    list_url = "https://eicweb.phy.anl.gov/EIC/NPDet/-/tags"
    git = "https://eicweb.phy.anl.gov/EIC/NPDet"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("master", branch="master")
    version("1.4.1", sha256="adc7a534da912aa0c037dcb2eea981990c3b1d3f59772a9dd08b8995c8df9f18")
    version("1.4.0", sha256="f10e6446fdc5f499bec3d59e0cebdbfc24dd63c5317974a589cc251475dfe0da")
    version("1.3.2", sha256="cae9987bf08829c564da3739a344b6e077f2710908c79d1582d27943b6de8e79")
    version("1.3.1", sha256="dcdebb3ec3b9c90be63270585eb415cca1b5c54829d098847789fc7b1d9fdade")
    version("1.3.0", sha256="0e563ed94906a8f92e9802ff0ca5d824e7ea744f8aaf569dbe1549ef2816d702")
    version("1.2.4", sha256="7925d511cc337831f4c5d07d2f35c5616bf03be4ece663237a556a25851b9149")
    version("1.2.3", sha256="dd7443b13492c93298b6e33701cf733851af334312d8a904b5cfff8c61e95244")
    version("1.2.2", sha256="733334e642899f17bf79f0859af16fed5a86fe51508c6159944a2cb01b4d460b")
    version("1.2.1", sha256="1a9e37d89e22902716501f560937b2737d42ee943a85f52650b57e4bb41e97e6")
    version("1.2.0", sha256="6c39c5704f0069053f4882d83e8c526c1c40f05a161c79e5b2321cc4b54ea565")
    version("1.1.0", sha256="d7d01174f511a649cec4b4132caef17f3df0104d56095ce41b29e67068fc90c7")
    version("1.0.0", sha256="3c54266182d65cc5a25a76449eaeb9302bfb330d2ebcd4df0c385e59489b7e52")
    version("0.9.0", sha256="87e04b674b6e55ee79cc7da1e00b62992fe54fc0354b7b1faaf04dae8393de0e")
    version("0.8.0", sha256="d8ec998c8f5d5e1e63f856fa7acb32e4bf73caa07db183f349645b35227a038f")
    version("0.7.0", sha256="53aebda38492712ef87b7093ec0da2eea6b96eb10eb3f3fc3fd1932aa3501fb8")
    version("0.6.0", sha256="c9af46404465b4311cf6d312c52e633883dee8c7fde2ac445bd8d5d13ff40992")
    version("0.5.0", sha256="09833b35ecaa9d11c3479e8bc07bc61e8ce4d8efaab0f29aabb1f3481079359a")

    variant("http", default=False, description="Build web display services")
    variant("geocad", default=False, description="Build the geocad interface")

    depends_on("cxx", type="build")

    depends_on("fmt +shared")
    depends_on("acts")
    depends_on("eigen")
    depends_on("root")
    depends_on("podio")
    depends_on("py-pyyaml", type="build")
    depends_on("py-jinja2", type="build")
    depends_on("spdlog")
    depends_on("root +http", when="+http")
    depends_on("dd4hep +ddg4")
    depends_on("dd4hep@1.18:", when="@1.2.2:")
    depends_on("opencascade", when="+geocad")
    depends_on("py-six")

    conflicts("-http", when="@:0.5.8", msg="NPDet pre-0.5.8 requires http")

    def cmake_args(self):
        args = [self.define_from_variant("USE_GEOCAD", "geocad")]
        args.append("-DCMAKE_CXX_STANDARD=17")
        return args
