from spack import *


class EpicEic(CMakePackage):
    """The EPIC Detector at IP6 of the Electron-Ion Collider."""

    homepage = "https://epic-eic.org"
    url = "https://github.com/eic/epic/archive/refs/tags/22.10.0.zip"
    list_url = "https://github.com/eic/epic/tags"
    git = "https://github.com/eic/epic"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("main", branch="main")
    version(
        "23.03.0",
        sha256="16badb2418531250a81931f920e145c4be9ef93411f091d93202c23e36e91129",
    )
    version(
        "23.01.0",
        sha256="56e1d9a9ca3d81e64127f4d14fd45733dad07f6ffdec8387e6cae5e729525399",
    )
    version(
        "22.12.0",
        sha256="9de036b47ab8d0c97ab32fc788dd8300132014413013a1b19c2a3f8f3883a7ae",
    )
    version(
        "22.11.3",
        sha256="5cea46de7edf4868a361c5a75749f6c0f3d3ee941a33b956b2507581aa638232",
    )
    version(
        "22.11.2",
        sha256="f53aa7a4d992ddfb7549abedd4d6b87d61569b9530691b99640c6a635f2545c2",
    )
    version(
        "22.11.1",
        sha256="c8aded71dc707185a06557a76060661c57f24ed5eeb4a39b0ebcc63c9fc0a4fe",
    )
    version(
        "22.11.0",
        sha256="f683ed9e26b303ea428dc513d6e841efeeaa584cec44121f6a28116693d13065",
    )
    version(
        "22.10.1",
        sha256="dbd70d2d5ab42f3979ba4e7cda87cbb8cc48b37c4d13a887bbf96c3b32c347e9",
    )
    version(
        "22.10.0",
        sha256="f683ed9e26b303ea428dc513d6e841efeeaa584cec44121f6a28116693d13065",
    )

    variant(
        "ip",
        default="6",
        values=("6"),
        when="@:22.11",
        description="Interaction point design",
    )

    depends_on("dd4hep@1.21: +ddg4 +ddrec", when="@:23.03.0")
    depends_on("dd4hep@1.21: +ddrec", when="@23.05.0:")

    depends_on("acts-dd4hep", when=@:23.01.0")
    
    depends_on("fmt +shared")
    depends_on("py-pyyaml")
    depends_on("py-jinja2")

    depends_on("eic-ip6", when="@:22.11 ip=6")

    with when("@:22.11"):
        phases = ["cmake", "build", "install", "postinstall"]
    with when("@22.12:"):
        phases = ["cmake", "build", "install"]

    @when("@:22.11")
    def postinstall(self, spec, prefix):
        ip = "ip" + spec.variants["ip"].value
        # Symlinks are not copied to view, so we have to make a full copy
        # Ref: https://github.com/spack/spack/issues/19531#issuecomment-793012461
        # symlink(join_path(self.spec['eic-' + ip].prefix, 'share', ip, ip),
        #        join_path(prefix, 'share/epic', ip))
        # FIXME: when issue above is resolved, go back to symlinking
        copy_tree(
            join_path(self.spec["eic-" + ip].prefix, "share", ip, ip),
            join_path(prefix, "share/epic", ip),
        )

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.set("JUGGLER_DETECTOR_PATH", join_path(self.prefix.share, "epic"))
        env.set("JUGGLER_DETECTOR", "epic")
        env.set("JUGGLER_DETECTOR_CONFIG", "epic")
        env.set("JUGGLER_DETECTOR_VERSION", str(self.spec.version))
        env.set("DETECTOR_PATH", join_path(self.prefix.share, "epic"))
        env.set("DETECTOR", "epic")
        env.set("DETECTOR_CONFIG", "epic")
        env.set("DETECTOR_VERSION", str(self.spec.version))
