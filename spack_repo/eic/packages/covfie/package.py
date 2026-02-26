from spack.package import *
from spack_repo.builtin.build_systems.cmake import CMakePackage


class Covfie(CMakePackage):
    """covfie is a library for representing and accessing covariant fields,
    such as magnetic fields, in a flexible and efficient manner."""

    homepage = "https://github.com/acts-project/covfie"
    url = "https://github.com/acts-project/covfie/archive/refs/tags/v0.15.4.zip"
    list_url = "https://github.com/acts-project/covfie/tags"
    git = "https://github.com/acts-project/covfie.git"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("0.15.4", sha256="92fa0515d321bfafc820c1b0e9153416b4c61e16f464a08efcc2eed560c77f4f")
    version("0.15.3", sha256="ca4f9bd648d7334cdea48114aa0f3b585d0bf79f240d01bdbb72ce074db4698b")
    version("0.15.2", sha256="3bb95f8a5587cfc42eb4e774eac01d9e8ccb82ee3c5e82a8d7a5b494b8b399cd")
    version("0.15.1", sha256="d31234de93f6321807db38b7ec37a16d671d769a9ee9f5bdc0fcbebf14e0d63f")
    version("0.15.0", sha256="2a656791826c44cb869ffad6833962ed64d40bd101654ea484e77e38de5740a2")
    version("0.14.0", sha256="6caceb5ac281856579a8772ad39bfecd6ff692e7884d270e83c27e6a6d4474c2")
    version("0.13.0", sha256="a64ae5e03ba49a10db79ea50c3a1e02e5cb9409995ec3755248341e98afbd85d")
    version("0.12.0", sha256="ac4bbd8dc6d5e92458002a0676ca5493626001f633766d5c52dbd145b9b8a56d")
    version("0.11.0", sha256="02a7aa045061e02af152f1e88f618bea757bb1e1d50a1dcf69d6115362ecfae4")
    version("0.10.0", sha256="458bf41ca9230cd4f76e8f7660c2fc8e6c596d09e18a368e091c53c34cc0e7e7")

    depends_on("cxx", type="build")

    def cmake_args(self):
        return [
            self.define("COVFIE_BUILD_TESTS", False),
            self.define("COVFIE_BUILD_BENCHMARKS", False),
            self.define("COVFIE_BUILD_EXAMPLES", False),
        ]
