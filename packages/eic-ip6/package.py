from spack.package import *


class EicIp6(CMakePackage):
    """The Beamline at IP6 of the Electron-Ion Collider."""

    homepage = "https://github.com/eic/ip6"
    url = "https://github.com/eic/ip6/archive/refs/tags/v0.4.0.tar.gz"
    list_url = "https://github.com/eic/ip6/tags"
    git = "https://github.com/eic/ip6"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("master", branch="master")
    version(
        "1.1.0",
        sha256="117da7f69acfcc94ae2c1b9dc196bee9577cc022a713b5893ad4329c0b787163",
    )
    version(
        "1.0.1",
        sha256="0605f577afaebe20a10292226eb1bbe2230fb6d12118a4553a8b0f3a3897d6d7",
    )
    version(
        "1.0.0",
        sha256="b3b2e9e4d389a59ba22b0131b81081f2255a5721a3447e71ab56103fc85c9bb4",
    )
    version(
        "0.6.2",
        sha256="00cd864e7a345500a1c026668282d469f3db148bb630a2e590e4d7ee22286258",
    )
    version(
        "0.6.1",
        sha256="058cc15c1813ea02e92af2c7cfaeb1fd5e7fc315a56d58d108ac3c5587d9ec1a",
    )
    version(
        "0.6.0",
        sha256="d081565b0376ee7a7bd2d20d60f3e7c045cd3e482a8d39040143653e8b362c27",
    )
    version(
        "0.5.2",
        sha256="d1a95ec0c1d432f3cd158e7c1c2baefe86438203292767304adf3467d4b54444",
    )
    version(
        "0.5.1",
        sha256="68ad5d44fff21d1e75c0c66ab26f7347dc7d5a227ca83ddbd30655861a49f18d",
    )
    version(
        "0.5.0",
        sha256="eab4ee7756532ee2991dbe3fbd4aa591f3dd506cd0b9a9c1d85581f9b04f3d2f",
    )
    version(
        "0.4.0",
        sha256="b59b99cbc1c772d1d3fe281bc424b8a59afb7a999467da7b554d479b6c5092be",
    )

    depends_on("cxx", type="build")

    depends_on("dd4hep +ddg4")
    depends_on("acts +dd4hep +tgeo")
    depends_on("root +gdml")
    depends_on("fmt")

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.set("BEAMLINE_PATH", join_path(self.prefix.share, "ip6"))
        env.set("BEAMLINE", "ip6")
        env.set("BEAMLINE_VERSION", str(self.spec.version))
        env.set("BEAMLINE_CONFIG", "ip6")
        env.set("BEAMLINE_CONFIG_VERSION", str(self.spec.version))
