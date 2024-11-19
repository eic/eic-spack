from spack import *


class Eicd(CMakePackage):
    """A podio based data model for the EIC."""

    homepage = "https://github.com/eic/eicd"
    url = "https://github.com/eic/eicd/archive/refs/tags/v0.2.0.tar.gz"
    git = "https://github.com/eic/eicd.git"
    list_url = "https://github.com/eic/eicd/tags"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("master", branch="master")
    version(
        "2.0.0",
        sha256="06ac51559382b982a4f3556befd569db95927ff14058df0ae988944eff86de16",
    )
    version(
        "1.1.0",
        sha256="9a2f335ef292e1bff41a794fb8c953a75db5f45fef9b12628e4d35307251fb1d",
    )
    version(
        "1.0.0",
        sha256="40657274c3b486d0305ce88bb6fead139029bd14fe4bb1fdb663bca017c25126",
    )
    version(
        "0.9.0",
        sha256="80306b2fe41e7b49a465fdfd040faf957f508d90c243945751a72cae4fb7777d",
    )
    version(
        "0.8.0",
        sha256="f29f8db627064efeef5fa80b1ef628ca874a0aa94f7c2c97451870fd7439c101",
    )
    version(
        "0.7.0",
        sha256="2e378f2440d029e8f7e45165e3c7ec1063595b24b2de1e207bf09ce5b9531277",
    )
    version(
        "0.6.0",
        sha256="09d9d143bd242092ac2d5fa6f3918387c7f24d4b18230ef80eecff7861ce0929",
    )
    version(
        "0.5.0",
        sha256="b5a30166f036bb4519d546f16f32fd45e6574031190935705d24412ef259169e",
    )
    version(
        "0.2.0",
        sha256="7b59d6fb5df82ef495d5afe462958ddd7366fc0396dad3e9bf9dc276d7ec9b95",
    )
    version(
        "0.1.0",
        sha256="c82c771a384c8a252ed45562042f916807708e0f887e0d51be06f908c6003712",
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

    depends_on("edm4hep@0.4.1:", when="@2:")
    depends_on("edm4hep@:0.4", when="@:1")
    depends_on("podio@0.14.1:", when="@2:")
    depends_on("podio@0.11.0:0.14.0", when="@:1")
    depends_on("root@6.08:")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            self.define("CMAKE_CXX_STANDARD", self.spec.variants["cxxstd"].value)
        )
        return args
