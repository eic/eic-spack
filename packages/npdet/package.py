from spack import *


class Npdet(CMakePackage):
    """Nuclear Physics Detector library."""

    homepage = "https://eicweb.phy.anl.gov/EIC/NPDet"
    url = "https://eicweb.phy.anl.gov/EIC/NPDet/-/archive/v0.5.0/NPDet-v0.5.0.tar.gz"
    list_url = "https://eicweb.phy.anl.gov/EIC/NPDet/-/tags"
    git = "https://eicweb.phy.anl.gov/EIC/NPDet"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("master", branch="master")
    version(
        "1.4.1",
        sha256="adc7a534da912aa0c037dcb2eea981990c3b1d3f59772a9dd08b8995c8df9f18",
    )
    version(
        "1.4.0",
        sha256="f10e6446fdc5f499bec3d59e0cebdbfc24dd63c5317974a589cc251475dfe0da",
    )
    version(
        "1.3.2",
        sha256="5b03cb266edf48806559ca29602038f841b4121aa875d1eb8341e387cb00d280",
    )
    version(
        "1.3.1",
        sha256="7c4bbc74d50bdfd21982456c1a95c5f3b7ef8acbf4d351c894736e46f5084aad",
    )
    version(
        "1.3.0",
        sha256="4280234bbad746ebcd2bb67085893d5c9caaab2505d7a8b5c8b7ad7fb0ab8ef2",
    )
    version(
        "1.2.4",
        sha256="5963d520f66242a49e9530eb60e20a309971a9eae2ff420fb9c639a0adbb649a",
    )
    version(
        "1.2.3",
        sha256="8736eedb8d43fdc0dfdf6b556a371fd47ad1192dd8a7c39f8f206bbdbeace591",
    )
    version(
        "1.2.2",
        sha256="96df677ec1b0e411bd20d22950bddc84622b9bab006b70ac545e32040df57dbd",
    )
    version(
        "1.2.1",
        sha256="814a601c0c05336ce1ebc44d514dd3b92c6b7fc3c21bbfa94352073e7b21da6b",
    )
    version(
        "1.2.0",
        sha256="117e307765e6554d4ad61c70d09991053ad4e88fc9d274264b40d512bd92ec04",
    )
    version(
        "1.1.0",
        sha256="0623684a153075c37ee4a2a66de89db12715e70c4a326ff4533eea67d2db6a95",
    )
    version(
        "1.0.0",
        sha256="e0522dd2a6c163367e8ad4bc12ba9ad5a58d99ea151192df3ab48228a754b490",
    )
    version(
        "0.9.0",
        sha256="0cb0e6e39956c6751b00d53e7d44007e71c41728ee97bc785664f2416fe051f4",
    )
    version(
        "0.8.0",
        sha256="89cec16c44e9ac3b009d2fbf3817b0df7dabafe1a34b0b0160183a6431a6fbed",
    )
    version(
        "0.7.0",
        sha256="d842d5571960316e76530849fa03296dc270d90da48d557bf4bd2c358538eefe",
    )
    version(
        "0.6.0",
        sha256="0b1adbb3aff5d8b8ef9c6e81ec63721bdf12f4c457465bfd584ddeba63161edd",
    )
    version(
        "0.5.0",
        sha256="2ff4cd7992b7c18c25da64aa2d6223c210ea50c5ce90bcb007c0346cb4aee2c5",
    )

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
