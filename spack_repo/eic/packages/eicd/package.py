from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Eicd(CMakePackage):
    """A podio based data model for the EIC."""

    homepage = "https://github.com/eic/eicd"
    url = "https://github.com/eic/eicd/archive/refs/tags/v0.2.0.tar.gz"
    git = "https://github.com/eic/eicd.git"
    list_url = "https://github.com/eic/eicd/tags"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("master", branch="master")
    version("2.0.0", sha256="06ac51559382b982a4f3556befd569db95927ff14058df0ae988944eff86de16")

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
    depends_on("podio@0.14.1:0", when="@2:")
    depends_on("root@6.08:")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(self.define("CMAKE_CXX_STANDARD", self.spec.variants["cxxstd"].value))
        return args
