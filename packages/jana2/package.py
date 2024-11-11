# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Jana2(CMakePackage, CudaPackage):
    """Multi-threaded HENP Event Reconstruction."""

    homepage = "https://jeffersonlab.github.io/JANA2/"
    url = "https://github.com/JeffersonLab/JANA2/archive/refs/tags/v2.0.3.tar.gz"
    list_url = "https://github.com/JeffersonLab/JANA2/tags"
    git = "https://github.com/JeffersonLab/JANA2.git"

    maintainer = ["wdconinc"]

    tags = ["eic"]

    version("master", branch="master")
    version("2.3.3", sha256="9cbb805e041ba54aea2c178f367ddf7b584b652cdbfa9f9be4d5ad7a22561861")
    version("2.3.2", sha256="26c5b521087cf526e9a498c9d1235531fdc28690f538221e422b79cc5fd0a87c")
    version("2.3.1", sha256="860e1f5019fbc9deed8768724e4d42956dc10ee55583852febde8dd7bf2b616e")
    version("2.3.0", sha256="7ebc914f1dafbd50d7296c92d67658b64f80e309e9812653413b525d84320b1d")
    version("2.2.1-rc1", sha256="7b65ce967d9c0690e22f4450733ead4acebf8fa510f792e0e4a6def14fb739b1")
    version("2.2.0", sha256="60940e182593dafddaa76d582d3270ac47694fa3f20257493e1017b34f624ba9")
    version("2.1.2", sha256="81b5b323289113d0fe666927afa3f81e76b3fcee0df7bff2c3fc1cb72fb240ce")
    version(
        "2.1.1",
        sha256="ea9926e0fb2fa1fa1f22acb6411d5bd521733f25031df114f118fa7fe2272a14",
    )
    version(
        "2.1.0",
        sha256="111f7a3c3a2357a4bbf54370740b22f641a99c83ec649d4ea9899c143371cf35",
    )
    version(
        "2.0.9",
        sha256="d8df3dc3390a239eae64eb58f6a5745608405b8aa91fb247965aaf2e321d269b",
        deprecated=True,
    )
    version(
        "2.0.8",
        sha256="b0c91a2780a66cd51cfeaf2ddbe44e2264afb4b2b2a91bc2d001802fb40c3a1b",
    )
    version(
        "2.0.7",
        sha256="56b4d1858d0f84e655b903eef07f5c6e23a9ed62219cd083ae279549dd051eb1",
    )
    version(
        "2.0.6",
        sha256="dc0bec6a63b6973171a714cb9eb2044b96c28f7aa5dd198e5be5858e5ec7ce7c",
    )
    version(
        "2.0.5",
        sha256="2e7297dfb0bd7f4a2f2fa3bca6b1c10b2553d321dec6060e48b0d75a5ed6717d",
    )
    version(
        "2.0.4",
        sha256="848adffcb881beb7835d01ce47a58991bb4f92664c9477196960ce8cfd94a3ca",
    )
    version(
        "2.0.3",
        sha256="fd34c40e2d6660ec08aca9208999dd9c8fe17de21c144ac68b6211070463e415",
    )
    version(
        "2.0.2",
        sha256="161d29c2b1efbfb36ec783734b45dff178b0c6bd77a2044d5a8829ba5b389b14",
    )
    version(
        "2.0.1",
        sha256="1471cc9c3f396dc242f8bd5b9c8828b68c3c0b72dbd7f0cfb52a95e7e9a8cf31",
    )

    variant(
        "podio", default=False, description="Build with PODIO support.", when="@2.1.0:"
    )
    variant("python", default=True, description="Build with Python bindings.")
    variant("root", default=False, description="Use ROOT for janarate.")
    variant("xerces", default=True, description="Build with XML support.")
    variant("zmq", default=False, description="Use zeroMQ for janacontrol.")

    depends_on("cmake@3.16:", type="build")
    depends_on("cppzmq", when="+zmq")
    depends_on("py-pybind11@2.6.1:", when="+python")
    depends_on("root", when="+root")
    depends_on("xerces-c")

    with when("+podio"):
        depends_on("podio@0.16.3:")
        depends_on("podio@:0.17.3", when="@:2.1.2")  # uses podio/EventStore.h
        depends_on("py-jinja2")
        depends_on("py-pyyaml")

    conflicts("+cuda", when="@:2.0", msg="CUDA support only available in 2.1 and later")

    # JFactoryPodioT.h: ClearData (https://github.com/JeffersonLab/JANA2/pull/243)
    patch(
        "https://github.com/JeffersonLab/JANA2/pull/243.patch?full_index=1",
        sha256="f1b89fe245ac44fec815b7cf97d40924acf1281cd2aeb31ee33ad76a13e0abd4",
        when="@2.1.1",
    )
    # JResourcePool.h: alignas (https://github.com/JeffersonLab/JANA2/pull/239)
    patch(
        "https://github.com/JeffersonLab/JANA2/pull/239.patch?full_index=1",
        sha256="a32220ba30f18f30c196a604c9ccf9ed01676a81aadfad0028214b42a4363e25",
        when="@2.0.6:2.1.1",
    )
    # JBacktrace.h: free after use (https://github.com/JeffersonLab/JANA2/pull/224)
    patch(
        "https://github.com/JeffersonLab/JANA2/pull/224.patch?full_index=1",
        sha256="cc3820e391caae8f4fe08d96f49fa2b38e454aaf37edde7dbd6fb4537a01af61",
        when="@2.0.2:2.1.0",
    )
    # Stop printing the component summary
    patch(
        "https://github.com/JeffersonLab/JANA2/commit/8ed069da7f307d12cafd6b075eae8401aec6f5aa.diff?full_index=1",
        sha256="65f4b71d5cbf40ca5ece32ebab20a2da651201cf8dc89a09ab656dec2075f1f3",
        when="@2.3.2",
    )

    def cmake_args(self):
        args = [
            self.define_from_variant("USE_CUDA", "cuda"),
            self.define_from_variant("USE_ROOT", "root"),
            self.define_from_variant("USE_ZEROMQ", "zmq"),
            self.define_from_variant("USE_PYTHON", "python"),
        ]

        # Podio
        if "+podio" in self.spec:
            args.append("-DUSE_PODIO=On")

        # ZeroMQ directory
        if "+zmq" in self.spec:
            args.append("-DZEROMQ_DIR=%s" % self.spec["cppzmq"].prefix)

        # C++ standard (defined by ROOT)
        if "+root" in self.spec:
            args.append(
                "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value
            )

        return args

    def setup_run_environment(self, env):
        env.append_path("JANA_PLUGIN_PATH", join_path(self.prefix, "plugins"))
        env.set("JANA_HOME", self.prefix)
