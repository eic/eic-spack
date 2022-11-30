from spack import *


class EpicEic(CMakePackage):
    """The EPIC Detector at IP6 of the Electron-Ion Collider."""

    homepage = "https://epic-eic.org"
    url = "https://github.com/eic/epic/archive/refs/heads/main.zip"
    list_url = "https://github.com/eic/epic/tags"
    git = "https://github.com/eic/epic"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("main", branch="main", preferred=True)

    variant("ip", default="6", values=("6"), description="Interaction point design")
    variant(
        "reconstruction",
        default=False,
        description="Depend on reconstruction libraries",
    )

    depends_on("dd4hep +ddg4 +hepmc3")
    depends_on("acts +dd4hep +identification +tgeo")
    depends_on("fmt +shared")
    depends_on("py-pyyaml")
    depends_on("py-jinja2")

    depends_on("eic-ip6", when="ip=6")
    depends_on("eic-ip6@master", when="@main ip=6")

    depends_on("juggler", when="+reconstruction")
    depends_on("juggler@main", when="@main +reconstruction")

    phases = ["cmake", "build", "install", "postinstall"]

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
