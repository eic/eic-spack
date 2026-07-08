# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Jana2(CMakePackage, CudaPackage):
    """Multi-threaded HENP Event Reconstruction."""

    homepage = "https://jeffersonlab.github.io/JANA2/"
    url = "https://github.com/JeffersonLab/JANA2/archive/refs/tags/v2.0.3.tar.gz"
    list_url = "https://github.com/JeffersonLab/JANA2/tags"
    git = "https://github.com/JeffersonLab/JANA2.git"

    maintainer = ["wdconinc"]

    tags = ["eic"]

    version("master", branch="master")
    version(
        "2026.03.00", sha256="1e30333b457b61aaf812dfdc700a50bd5f17b9c580f4d2cd6ccd6fff3ab0b6af"
    )
    version(
        "2026.02.00", sha256="431a70d56019cf076fe80dc4317849ef5ad448173d4a0a7bf0325607aafba545"
    )
    # JANA2 2026.01 never worked with EICrecon, so it is not included here
    # version(
    #     "2026.01.01", sha256="2ccb1d6cc695df1ea9aa04667607534d89fb21c6f0692ebbf2ea9bf0e409621c"
    # )
    # version(
    #     "2026.01.00", sha256="575a202f5b7e153f9e25274fc6367c2a935aa23fb2ad3331c87d2fbfe08154ff"
    # )
    version("2.4.3", sha256="9d023f2225ad28d19c0e663de180d08e96900c4f76e3992faa946926cfa9cfcb")
    version("2.4.2", sha256="3536c2885745dd3e0ce3e068d09537a93850bee6e5a2ca8a559044ce1a7f985a")
    version("2.4.1", sha256="d3fabb532bbc6773fcd40fbdac714079b25bf69edd8f528395be0c7909bf8265")
    version("2.4.0", sha256="3b84fe3f86d8cc1ff79463e092c44d42c7d7a639319cb19bdfdfbcecd6f4ee7d")
    version("2.3.3", sha256="9cbb805e041ba54aea2c178f367ddf7b584b652cdbfa9f9be4d5ad7a22561861")
    version("2.3.2", sha256="26c5b521087cf526e9a498c9d1235531fdc28690f538221e422b79cc5fd0a87c")
    version("2.3.1", sha256="860e1f5019fbc9deed8768724e4d42956dc10ee55583852febde8dd7bf2b616e")
    version("2.3.0", sha256="7ebc914f1dafbd50d7296c92d67658b64f80e309e9812653413b525d84320b1d")
    version("2.2.1-rc1", sha256="7b65ce967d9c0690e22f4450733ead4acebf8fa510f792e0e4a6def14fb739b1")
    version("2.2.0", sha256="60940e182593dafddaa76d582d3270ac47694fa3f20257493e1017b34f624ba9")

    variant(
        "perfetto", default=False, description="Include Perfetto tracing.", when="@2026.03.00:"
    )
    variant("podio", default=False, description="Build with PODIO support.")
    variant("python", default=True, description="Build with Python bindings.")
    variant("root", default=False, description="Use ROOT for janarate.")
    variant("xerces", default=True, description="Build with XML support.")
    variant("zmq", default=False, description="Use zeroMQ for janacontrol.")

    depends_on("c", type="build")  # FIXME https://github.com/JeffersonLab/JANA2/pull/419
    depends_on("cxx", type="build")
    depends_on("cmake@3.16:", type="build")
    depends_on("cppzmq", when="+zmq")
    depends_on("py-pybind11@2.6.1:", when="+python")
    depends_on("root", when="+root")
    depends_on("xerces-c")

    with when("+podio"):
        depends_on("podio@0.16.3:")
        depends_on("podio@:1.4", when="@:2.4.2")  # uses operator-> on collections
        depends_on("py-jinja2")
        depends_on("py-pyyaml")

    # Add LinkDef.h for janaview and data model example add
    patch(
        "https://github.com/JeffersonLab/JANA2/commit/490fd69174a6241b5e532f346dbc1d05b830419f.patch?full_index=1",
        sha256="18b7d1fd8f855ebcb3c63661d312d892a70ba72765bd8b36ad45a6c42d2d97f7",
        when="@2026.02.00",
    )
    conflicts("^root@6.40:", when="@:2026.01", msg="ROOT 6.40 support only added in 2026.02")

    # Stop printing the component summary
    patch(
        "https://github.com/JeffersonLab/JANA2/commit/8ed069da7f307d12cafd6b075eae8401aec6f5aa.diff?full_index=1",
        sha256="65f4b71d5cbf40ca5ece32ebab20a2da651201cf8dc89a09ab656dec2075f1f3",
        when="@2.3.2",
    )

    # Bugfix: JFactoryPodioT template instantiation error with LinkCollections
    patch(
        "https://github.com/JeffersonLab/JANA2/commit/c439fdd14bad2da6cf237c6d442f2a2f6632b67a.patch?full_index=1",
        sha256="46c7beab1ff075ae2e8cd6de87e4c53a5c432675e31753f11ddcfb74a39c4659",
        when="@2.4:2.4.2",
    )

    # Bugfixes for EICrecon
    patch(
        "https://github.com/JeffersonLab/JANA2/pull/464.patch?full_index=1",
        sha256="a2590467a168a5771c02e4b361b1cc8f556a45e88683ec266169c1f0b3620d48",
        when="@2.4.3",
    )
    # Add BUILD_EXAMPLES and BUILD_TESTS CMake flags
    patch(
        "https://github.com/JeffersonLab/JANA2/pull/492.patch?full_index=1",
        sha256="dd30168e3968538cecbb1a4ff234e193c733956db2f4b8332df151cc297e8987",
        when="@2.4.3",
    )

    def cmake_args(self):
        args = [
            self.define_from_variant("USE_CUDA", "cuda"),
            self.define_from_variant("USE_ROOT", "root"),
            self.define_from_variant("USE_ZEROMQ", "zmq"),
            self.define_from_variant("USE_PERFETTO", "perfetto"),
            self.define_from_variant("USE_PYTHON", "python"),
            self.define("BUILD_EXAMPLES", self.run_tests),
            self.define("BUILD_TESTS", self.run_tests),
        ]

        # Podio
        if "+podio" in self.spec:
            args.append("-DUSE_PODIO=On")

        # ZeroMQ directory
        if "+zmq" in self.spec:
            args.append("-DZEROMQ_DIR=%s" % self.spec["cppzmq"].prefix)

        # C++ standard (defined by ROOT)
        if "+root" in self.spec:
            args.append("-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value)

        return args

    @when("@:2026.02.00")
    def check(self):
        pass

    def setup_run_environment(self, env):
        env.append_path("JANA_PLUGIN_PATH", self.prefix.lib.JANA.plugins)
        env.set("JANA_HOME", self.prefix)
