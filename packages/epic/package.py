import os
from spack import *


class Epic(CMakePackage):
    """The ePIC Detector at IP6 of the Electron-Ion Collider."""

    homepage = "https://epic-eic.org"
    url = "https://github.com/eic/epic/archive/refs/tags/22.10.0.zip"
    list_url = "https://github.com/eic/epic/tags"
    git = "https://github.com/eic/epic"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("main", branch="main")
    version("24.12.0", sha256="e7003a27bcb3f21763157ba12c9298113052249a4ccb49b5ba8a71a2f8612a12")
    version("24.11.2", sha256="0c734bec463103149acea641ce085c9653bc3b451a18f22c7c34aa632467f26f")
    version("24.11.1", sha256="781f848dc5032fc15699d57bcc911736d5fc22ac4b728a84da19fe7ee579a29f")
    version("24.11.0", sha256="3039d22bc654643046b27fc840543ec0faf35708c045f40f8f2c1064d1c6126d")
    version("24.10.1", sha256="9b5d161851d7acbe1986e7673bf8a268a9b74e1256fa3cb7e51a76e952990dcd")
    version("24.10.0", sha256="aeef27935f2664b96c1e0558b65dd2817ae53143c72de3451c24a9c65652c786")
    version("24.09.0", sha256="a0ab3ac4f5268aa2e5f7da0ab2e9c3c06180019bee088e1f72111e491fb8ae07")
    version("24.08.1", sha256="56f71b3136ade19a62ee6307f22a41a0cfade702519b0074799aee2aeecec8c8")
    version("24.08.0", sha256="288064ec68eb61a443a6b5ab5b8ec0b12b541ae1ad1550f4d68831390246dbb7")
    version("24.07.0", sha256="86f9a3f052e7a3699bba4e8f9f2600948073357bec820369a236dfe1339cf6f2")
    version("24.06.0", sha256="1aa075223704269905c6ac166ded074679387cbfda0297cfd4ec799e5b38a764")
    version("24.05.2", sha256="4e25154ca7c499eb360f370e0afac5c2d780cd2f682e0ad178875beb7db77040")
    version("24.05.1", sha256="2e0e7390fea6c091ee230835eac2354ac8b5f506f9508b4e6f8fd46d9573c2a5")
    version("24.05.0", sha256="647eff542ec5b77f73c2d9623d90abcca7a9ef30baaa21809b59f3c77e080385")
    version("24.04.0", sha256="9de5a71c3af9bf7d99ffcb10c5000d9ed2b5ffdbfc45a1a2e8b60cb73b480eea")
    version("24.03.1", sha256="58eb4fe340ba9e1b2d23bad805619b095ff0dc59d0187e831b576b1dbfb5cb24")
    version("24.03.0", sha256="d9943955a8135108df02ed4916c7493f246290c9379f912401efb3eecc297d4b")
    version("24.02.1", sha256="5c8bb108c00c807913da8508aa6a36d370079918e93f7cf6c8eae98fa41f43e7")
    version("24.02.0", sha256="04eb6e498eb6a9eafc2d29a5a34e6bbbedac26289ec98c5ce99cb5cfc3455d0e")
    version("23.12.0", sha256="04e94abf111d2746315dfa912f86c81c0f11011dff2a65434e00c87ba2de7b4a")
    version("23.11.0", sha256="24d856f718369d4336c56e191b5cb305bae60bcb06d00485154f5145d9acf597")
    version(
        "23.10.0",
        sha256="abf833eea328afb749c1eabbc83072c1382f02fc547ce7e9291e0616db552a0e",
    )
    version(
        "23.09.1",
        sha256="1fc30d36461e5acc3a54f475e9c01132aca12e74cc2fbec78fb3073fa83782b5",
    )
    version(
        "23.09.0",
        sha256="6f2ced07ead619ad4096246966383f7362d34fb140f8c0f3f60e775401deb303",
    )
    version(
        "23.08.0",
        sha256="1a8f82ef75d19dfad7228fcb437736622fc984caf0cf06466209124a8559d968",
    )
    version(
        "23.07.2",
        sha256="e80c31a338e41766aecc76441ac7aed7d53ddf401c7ca8773b0124536096ef2d",
    )
    version(
        "23.07.1",
        sha256="7e5908b3a64941ca2ff81195d62b3da6c8a20c4431f903a3c1bdda30bd39fac3",
    )
    version(
        "23.07.0",
        sha256="3b2fd83ee1664cb6bb47e45098c0357649d33526bac1e8637118bec4cd88295e",
    )
    version(
        "23.06.1",
        sha256="c78a756f84f34c6bb7b39e2bb104ffa7bcb2c7d0dcbdaa7905fe44f81e7b17aa",
    )
    version(
        "23.06.0",
        sha256="3e9825457920b97cab1bc73f44b8cfc45130f66a5d00c4acde4f8b9079a661b1",
    )
    version(
        "23.05.2",
        sha256="afb31d076a7859bd4cd94d9eed237f402a5cc56100c53c933ed4a024c8ef997b",
    )
    version(
        "23.05.1",
        sha256="4cac31b2619b3aafaaa9cc6a43923a97d04d74b753eb580990d569d1ef94c94d",
    )
    version(
        "23.05.0",
        sha256="a72774ffc3176178b128a4069d2a7bebfebde91192d971d0ccd3ab3392ff7977",
    )
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

    def cmake_flags(self):
        return [f"-DVERSION={self.version}"]

    # dd4hep::CartesianField renamed type to field_type
    patch(
        "https://github.com/eic/epic/pull/449.patch?full_index=1",
        sha256="df951c3e8a6dd519b48ae7b6248dc70e9709e3931f129cba66cafed2466837f4",
        when="@:23.06 ^dd4hep@1.26:",
    )
    # ensure file download command is constexpr since required in C++20
    patch(
        "https://github.com/eic/epic/pull/520.patch?full_index=1",
        sha256="b76a5830404c4e25efc95f359dc661c29de417b1961525ac3cfd76f954ee3957",
        when="@:23.09",
    )

    variant(
        "artifacts",
        default="none",
        description="Initialize configuration with artifacts",
    )
    variant(
        "ip",
        default="6",
        values=("6"),
        when="@:22.11",
        description="Interaction point design",
    )

    depends_on("cxx", type="build")

    depends_on("dd4hep@1.21: +ddg4 +ddrec", when="@:23.03.0")
    depends_on("dd4hep@1.21: +ddrec", when="@23.05.0:")

    depends_on("acts-dd4hep", when="@:23.01.0")

    depends_on("fmt +shared")
    depends_on("py-pyyaml")
    depends_on("py-jinja2")

    depends_on("eic-ip6", when="@:22.11 ip=6")

    phases = ["cmake", "build", "install", "postinstall"]

    def postinstall(self, spec, prefix):
        if spec.satisfies("@:22.11"):
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

        if not spec.satisfies("artifacts=none"):
            detector_path = join_path(self.prefix.share, "epic")
            with working_dir(detector_path):
                os.environ["LD_LIBRARY_PATH"] += os.pathsep + self.prefix.lib
                if spec.satisfies("@:24.03"):  # no rpath linking until 24.04
                    os.environ["LD_LIBRARY_PATH"] += os.pathsep + self.spec["root"].prefix.lib.root
                    os.environ["LD_LIBRARY_PATH"] += os.pathsep + self.spec["fmt"].prefix.lib
                os.environ["DETECTOR_PATH"] = detector_path
                checkGeometry = Executable(join_path(spec['dd4hep'].prefix.bin, 'checkGeometry'))
                checkGeometry('-c', join_path(detector_path, spec.variants["artifacts"].value + ".xml"))

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.set("DETECTOR_PATH", join_path(self.prefix.share, "epic"))
        env.set("DETECTOR", "epic")
        env.set("DETECTOR_CONFIG", "epic")
