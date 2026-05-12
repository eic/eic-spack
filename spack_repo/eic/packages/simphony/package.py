# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Simphony(CMakePackage, CudaPackage):
    """GPU-Accelerated Optical Photon Simulation using NVIDIA OptiX"""

    homepage = "https://github.com/bnlnpps/simphony"
    git = "https://github.com/bnlnpps/simphony.git"
    url = "https://github.com/BNLNPPS/simphony/archive/refs/tags/0.1.0.tar.gz"

    license("Apache-2.0")

    maintainers("plexoos")

    version("main", branch="main")
    version("0.5.0", sha256="383219ef86d67d6c2f3d9c00259f7a97ac007be39e889cfa95ada25ca0999ecc")
    version("0.4.0", sha256="15c776e79c1e8eb256886753e6f093e909e9ac69a4591a18b48a754b233856e7")
    version("0.3.0", sha256="6aebeb9b4c3dd6bdd300898d7e35ea51c550ec6005d7aa4b83066fc06771a456")
    version("0.2.0", sha256="94b97cd31d76ea6167b5db13cf05a9718bfb5ccda942dabd25ddbb9fde871211")
    version("0.1.0", sha256="e587eefa90febcb84de2de666170a3fd4a2b53912099bf1625b6a41298e5be9a")

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
        args = [self.define("BUILD_TESTING", self.spec.satisfies("@0.5:") and self.run_tests)]
        return args
