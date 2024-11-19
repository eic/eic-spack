from spack import *


class AthenaEic(CMakePackage):
    """The ATHENA Detector at IP6 of the Electron-Ion Collider."""

    homepage = "https://athena-eic.org"
    url = "https://eicweb.phy.anl.gov/EIC/detectors/athena/-/archive/main/athena-main.tar.gz"
    list_url = "https://eicweb.phy.anl.gov/EIC/detectors/athena/-/tags"
    git = "https://eicweb.phy.anl.gov/EIC/detectors/athena"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("master", branch="master", preferred=True)
    version("acadia", branch="acadia")
    version("canyonlands", branch="canyonlands")
    version("deathvalley", branch="deathvalley")
    version(
        "0.2.0",
        sha256="188ed1e46196c7cb2474ec0e3a653e32bf781c464c68d6a15c26bddc51293999",
    )
    version(
        "0.1.0",
        sha256="34ab3c99e833ca6e674ae69d36c11b242413def06fb9a31735ffe43cac2989de",
    )

    variant("ip", default="6", values=("6"), description="Interaction point design")
    variant(
        "reconstruction",
        default=False,
        description="Depend on reconstruction libraries",
    )

    depends_on("cxx", type="build")

    depends_on("dd4hep +ddg4 +hepmc3")
    depends_on("acts +dd4hep +identification +tgeo")
    depends_on("fmt +shared")

    depends_on("eic-ip6", when="ip=6")
    depends_on("eic-ip6@master", when="@master ip=6")

    depends_on("juggler", when="+reconstruction")
    depends_on("juggler@master", when="@master +reconstruction")

    phases = ["cmake", "build", "install", "postinstall"]

    def postinstall(self, spec, prefix):
        ip = "ip" + spec.variants["ip"].value
        # Symlinks are not copied to view, so we have to make a full copy
        # Ref: https://github.com/spack/spack/issues/19531#issuecomment-793012461
        # symlink(join_path(self.spec['eic-' + ip].prefix, 'share', ip, ip),
        #        join_path(prefix, 'share/athena', ip))
        # FIXME: when issue above is resolved, go back to symlinking
        copy_tree(
            join_path(self.spec["eic-" + ip].prefix, "share", ip, ip),
            join_path(prefix, "share/athena", ip),
        )

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.set("DETECTOR_PATH", join_path(self.prefix.share, "athena"))
        env.set("JUGGLER_DETECTOR", "athena")
        env.set("DETECTOR_VERSION", str(self.spec.version))
