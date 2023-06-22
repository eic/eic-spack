# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class TensorflowLite(CMakePackage):
    """TensorFlow Lite is TensorFlow's lightweight solution for mobile and
    embedded devices. It enables low-latency inference of on-device machine
    learning models with a small binary size and fast performance supporting
    hardware acceleration."""

    homepage = "https://www.tensorflow.org/lite/"
    url = "https://github.com/tensorflow/tensorflow/archive/refs/tags/v2.8.0.tar.gz"

    maintainers = ["wdconinc"]

    version("2.12.0", sha256="c030cb1905bff1d2446615992aad8d8d85cbe90c4fb625cee458c63bf466bc8e")
    version("2.11.1", sha256="624ed1cc170cdcc19e8a15d8cdde989a9a1c6b0534c90b38a6b2f06fb2963e5f")
    version("2.10.1", sha256="622a92e22e6f3f4300ea43b3025a0b6122f1cc0e2d9233235e4c628c331a94a3")
    version("2.9.3", sha256="59d09bd00eef6f07477eea2f50778582edd4b7b2850a396f1fd0c646b357a573")
    version(
        "2.9.1",
        sha256="6eaf86ead73e23988fe192da1db68f4d3828bcdd0f3a9dc195935e339c95dbdc",
    )
    version(
        "2.9.0",
        sha256="8087cb0c529f04a4bfe480e49925cd64a904ad16d8ec66b98e2aacdfd53c80ff",
    )
    version("2.8.4", sha256="c08a222792bdbff9da299c7885561ee27b95d414d1111c426efac4ccdce92cde")
    version(
        "2.8.2",
        sha256="b3f860c02c22a30e9787e2548ca252ab289a76b7778af6e9fa763d4aafd904c7",
    )
    version(
        "2.8.1",
        sha256="4b487a63d6f0c1ca46a2ac37ba4687eabdc3a260c222616fa414f6df73228cec",
    )
    version(
        "2.8.0",
        sha256="66b953ae7fba61fd78969a2e24e350b26ec116cf2e6a7eb93d02c63939c6f9f7",
    )

    variant("gpu", default=False, description="Enable GPU support")
    variant("metal", default=False, description="Enable Metal support")
    variant("xnnpack", default=True, description="Enable XNNPACK support")
    variant("shared", default=False, description="Build shared libraries")

    depends_on("cmake@3.16:", type="build")

    # TODO this package still overrides the upstream software with its own FetchContent
    depends_on("abseil-cpp")
    depends_on("eigen")
    depends_on("flatbuffers")
    depends_on("fp16")
    depends_on("gemmlowp")
    depends_on("psimd")
    depends_on("pthreadpool")
    depends_on("farmhash")
    # depends_on(fft2d REQUIRED)
    # depends_on(neon2sse REQUIRED)
    depends_on("cpuinfo")
    # depends_on(ruy REQUIRED)

    # GPU variant dependencies
    depends_on("opencl", when="gpu")
    # find_package(vulkan_headers REQUIRED)
    # find_package(fp16_headers REQUIRED)
    # find_package(opengl_headers REQUIRED)
    # find_package(egl_headers REQUIRED)

    # XNNPACK variant dependencies
    depends_on("xnnpack", when="xnnpack")

    root_cmakelists_dir = "tensorflow/lite"

    def patch(self):
        # Two utilities in subdirectory pull headers from outside lite
        filter_file(
            "^add_subdirectory", "#add_subdirectory", "tensorflow/lite/CMakeLists.txt"
        )

    def cmake_args(self):
        args = [
            self.define_from_variant("TFLITE_ENABLE_GPU", "gpu"),
            self.define_from_variant("TFLITE_ENABLE_METAL", "metal"),
            self.define_from_variant("TFLITE_ENABLE_XNNPACK", "xnnpack"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("TFLITE_KERNEL_TEST", self.run_tests),
        ]
        return args

    def install(self, spec, prefix):
        # Currently no install target is defined, but allowing for future
        super().install(spec, prefix)

        # Instal library
        mkdirp(self.prefix.lib)
        with working_dir(self.build_directory):
            for l in find(".", "libtensorflow-lite.*", recursive=False):
                install(l, self.prefix.lib)

        # Install headers for tensorflow itself
        mkdirp(self.prefix.include)
        for h in find(
            join_path(self.stage.source_path, "tensorflow/lite"), "*.h", recursive=True
        ):
            relpath = os.path.relpath(h)
            dirname = os.path.dirname(relpath)
            installdir = join_path(self.prefix.include, dirname)
            mkdirp(installdir)
            install(h, installdir)

        # Install headers for vendored dependencies
        for d in ["flatbuffers"]:
            install_tree(
                join_path(self.build_directory, d, "include"), self.prefix.include
            )
