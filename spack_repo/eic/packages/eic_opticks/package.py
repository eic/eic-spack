# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class EicOpticks(CMakePackage, CudaPackage):
    """GPU-Accelerated Optical Photon Simulation using NVIDIA OptiX"""

    homepage = "https://github.com/bnlnpps/eic-opticks"
    git = "https://github.com/bnlnpps/eic-opticks.git"
    url = "https://github.com/BNLNPPS/eic-opticks/archive/refs/tags/0.1.0.tar.gz"

    license("Apache-2.0")

    maintainers("plexoos")

    version("main", branch="main")
    version("0.4.0", sha256="dd771bc9163cefe1f285d81b543929a4f998e2f0ad08abd91fefcbb57e22af42")
    version("0.3.0", sha256="611c84e782a8534f9cd9dd23d09b03f5612bd6632f009c0f746dbd08a70444c2")
    version("0.2.0", sha256="85022ee513020d13f5acf2e07fa3a9e73c24a51166507c8598b6fd86327b436b")
    version("0.1.0", sha256="b9b42254d3a2c57df9502e2920c7078aee3b7952d4de1d0299fd421d88a5950d")

    depends_on("cxx", type="build")
    depends_on("cmake@3.10:", type="build")

    depends_on("cuda")
    depends_on("geant4")
    depends_on("glew")
    depends_on("glfw")
    depends_on("glm")
    depends_on("glu")
    depends_on("nlohmann-json")
    depends_on("mesa")
    depends_on("optix-dev")
    depends_on("openssl")
    depends_on("plog")
    depends_on("python")

    conflicts("~cuda", msg="This package requires CUDA")

    def setup_build_environment(self, env):
        # GLM 0.9.9+ requires this for experimental GTX headers such as
        # dual_quaternion, which are reached via string_cast in this codebase.
        if self.spec.satisfies("^glm@0.9.9:"):
            env.append_flags("CPPFLAGS", "-DGLM_ENABLE_EXPERIMENTAL")

    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", self.spec.satisfies("@0.5:") and self.run_tests),
        ]
        return args
