from spack.package import *


class Edm4eic(CMakePackage):
    """A data model for EIC defined with podio and based on EDM4hep."""

    homepage = "https://github.com/eic/EDM4eic"
    url = "https://github.com/eic/EDM4eic/archive/refs/tags/v1.0.0.tar.gz"
    git = "https://github.com/eic/EDM4eic.git"
    list_url = "https://github.com/eic/EDM4eic/tags"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("main", branch="main")
    version("8.7.0", sha256="48287bbcfcd0aa4a15a7219fb30d17b2c93b9fd29626d54ccc1b906419773996")  # FIXME
    version("8.6.0", sha256="023fdc2f64812c612e7f173e662fecd45568dc43c5b84d2e3e986ed8e34b4939")
    version("8.5.0", sha256="35d6fe823c02cc0a85a27c086ac0b8ae08c557a5034f0355e9927eb9291a965c")
    version("8.4.0", sha256="fc2176d38978998dd10c40a8a6691e2d0e2fab381468d764ecde9e6dc4416bdf")
    version("8.3.0", sha256="744ebd8b265e47b3d281db77452f83e13bb924197c3e97bb546129be19595d97")
    version("8.2.0", sha256="c085a7df046d71b830ecfaf2fca2bfd44c52f22b480ab69cf01595140654f681")
    version("8.1.0", sha256="7b35bfa08cb6e5430c4d77ee4c3272faa6820834436370ef361315c2e403d8eb")
    version("8.0.1", sha256="6cc2c575b8ed94da91c4fed56658c922c7cebaf292a9da0b5522c4715bc3a6dc")
    version("8.0.0", sha256="91c483e1473fa015afe43040f7851b5d1ce7baa84aa2583c9de579401b466d13")
    version("7.0.0", sha256="48ff297dcdda285079bf63df9d7eb996072b41298ecc6c0a766d9f5aa48d85e8")
    version("6.0.1", sha256="5c159c61a284c6ad3bcba65532b21ed11fddc194129e84347d30c519d1ef8c77")
    version("6.0.0", sha256="9215b1477ddaaeff5bd0f9ff0990a4b54dc4780fb6c6ab36f0bd9bcc83e59928")
    version(
        "5.0.0",
        sha256="31ddc38b73909f2faf6a2ade5521104401b440fcbb6fccea4ed592427d7dcac2"
    )
    version(
        "4.0.0", 
        sha256="564d4ddff9a52c6358d72a99857d9e755af0fc8f782900dab471e65e6e34f0d3")
    version(
        "3.0.1",
        sha256="f5d3ed307c53a1197c71581b7095c40f9cd0afd624997a8720428d24bc0c0d60",
    )
    version(
        "3.0.0",
        sha256="dc7cc7f2af17bb90e0379487e651033e2694fa8926b6e9cb6555cc4b6a4ad255",
    )
    version(
        "2.1.0",
        sha256="eec896b8c4921904aefc0065c13d6a164d014029ead101a1bab5201400d1c482",
    )
    version(
        "2.0.0",
        sha256="bedce5fd3fd3a2d6ff3258e8857819a89cc467de0aa5871999265f9ec7e39015",
    )
    version(
        "1.2.2",
        sha256="a2b63689d05ee1c8836d9652ba8ccfe45f08558b6a89a75e4649654dd9a5073c",
    )
    version(
        "1.2.1",
        sha256="8349864f5c923e991d31462cc7987cd39c050910d4db8847575c8d4fd61967a5",
    )
    version(
        "1.2.0",
        sha256="e70ec6d2a93002237c1bfd0046e96f3838f9dab3f5326bdb17826999b5f42759",
    )
    version(
        "1.1.0",
        sha256="f50a6ef77d8247aa30da5b1e574bb24ab82c86c8706a8f3900ff151dafe9a754",
    )
    version(
        "1.0.1",
        sha256="683dcd463757f9e4ad47e493be1f5fb40a6c1aae7d249ff18a19367384a61070",
    )
    version(
        "1.0.0",
        sha256="700ae7453f16786db4d3ace1a146914e1f0b935a08039c9f1f6a5ebe4aa173ae",
    )

    variant(
        "cxxstd",
        default="17",
        values=("17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("cxx", type="build")
    depends_on("python", type="build")
    depends_on("cmake@3.3:", type="build")
    depends_on("py-jinja2", type="build")
    depends_on("py-pyyaml", type="build")

    depends_on("edm4hep@0.4.1:", when="@1:")
    depends_on("podio@0.15:", when="@1:")
    depends_on("cli11", when="@1.1:")
    depends_on("root@6.08:")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            self.define("CMAKE_CXX_STANDARD", self.spec.variants["cxxstd"].value)
        )
        return args
