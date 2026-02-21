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

    license("Apache-2.0")

    maintainers("plexoos")

    version("main", branch="main")

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
