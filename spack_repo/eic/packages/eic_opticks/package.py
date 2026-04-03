# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage


class EicOpticks(CMakePackage, CudaPackage):
    """GPU-Accelerated Optical Photon Simulation using NVIDIA OptiX"""

    homepage = "https://github.com/bnlnpps/eic-opticks"
    git = "https://github.com/bnlnpps/eic-opticks.git"
    url = "https://github.com/BNLNPPS/eic-opticks/archive/refs/tags/0.1.0.tar.gz"

    license("Apache-2.0")

    maintainers("plexoos")

    version("main", branch="main")
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

    def setup_build_environment(self, env):
        # GLM 0.9.9+ requires this for experimental GTX headers such as
        # dual_quaternion, which are reached via string_cast in this codebase.
        if self.spec.satisfies("^glm@0.9.9:"):
            env.append_flags("CPPFLAGS", "-DGLM_ENABLE_EXPERIMENTAL")

    def _setup_optix_environment(self, env):
        # OptiX requires these NVIDIA container runtime capabilities to be
        # present whenever eic-opticks is loaded or consumed by another spec.
        env.set("NVIDIA_DRIVER_CAPABILITIES", "graphics,compute,utility")

    def setup_run_environment(self, env):
        super().setup_run_environment(env)
        self._setup_optix_environment(env)

    def setup_dependent_run_environment(self, env, dependent_spec):
        super().setup_dependent_run_environment(env, dependent_spec)
        self._setup_optix_environment(env)

    def setup_dependent_build_environment(self, env, dependent_spec):
        super().setup_dependent_build_environment(env, dependent_spec)
        self._setup_optix_environment(env)
