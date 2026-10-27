# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

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

    tags = ["eic"]

    version("main", branch="main")
    version("0.9.0", sha256="7f2afd0bcfa4c3dfaf1e291571fb1b9590e0ce48939e93251647136a315291fa")
    version("0.8.0", sha256="36a15510b02fcab86b2c2b229e2d1362d016b96871e66c713fe3480a3ea87f6f")
    version("0.7.0", sha256="60bb96928f7217befae175d6c4f8c8143535ad526de50f44fb1d41e8ab4fea9a")
    version("0.6.0", sha256="839d866f80563a6e39de9ba30c6f1d3913452e808336e6483d69b02dd0673436")
    version("0.5.0", sha256="383219ef86d67d6c2f3d9c00259f7a97ac007be39e889cfa95ada25ca0999ecc")
    version("0.4.0", sha256="15c776e79c1e8eb256886753e6f093e909e9ac69a4591a18b48a754b233856e7")
    version("0.3.0", sha256="6aebeb9b4c3dd6bdd300898d7e35ea51c550ec6005d7aa4b83066fc06771a456")
    version("0.2.0", sha256="94b97cd31d76ea6167b5db13cf05a9718bfb5ccda942dabd25ddbb9fde871211")
    version("0.1.0", sha256="e587eefa90febcb84de2de666170a3fd4a2b53912099bf1625b6a41298e5be9a")

    depends_on("cxx", type="build")
    depends_on("cmake@3.10:", type="build")

    depends_on("cuda")
    depends_on("dd4hep", when="@0.6.0:")
    depends_on("geant4")
    depends_on("glew")
    depends_on("glfw")
    depends_on("glm")
    depends_on("glu")
    depends_on("libglx")
    depends_on("nlohmann-json")
    depends_on("optix-dev")
    depends_on("openssl")
    depends_on("plog")
    depends_on("python")

    conflicts("~cuda", msg="This package requires CUDA")
    conflicts("platform=darwin", msg="CUDA and OptiX are not available on macOS")

    # SPM.cu uses std::cerr without including <iostream>; newer CUDA (13.x)
    # no longer provides it transitively through the thrust headers
    patch("simphony-spm-include-iostream.patch", when="@:0.9")

    # Build-time tests that need a CUDA device; they fail on hosts without an
    # NVIDIA GPU (e.g. CI runners) and are skipped there. Setup.SimphonyInputPhotons
    # only provides input photons to the QEvt_Lifecycle_Test GPU tests.
    gpu_tests = [
        r"SysRapTest\.SUTest\.presized",
        r"CSGTest\.(CSGPrimImpTest|CUTest)",
        r"Setup\.SimphonyInputPhotons",
        r"QUDARapTest\.(QRngTest|QSimCreateTest|QUTest|QTexMakerTest|QTexLookupTest)",
        r"QUDARapTest\.QEvt_Lifecycle_Test\..*",
        r"CSGOptiXTest\.CSGOptiXHelpersTest",
        r"Integration\.simg4ox\.(raindrop|dune_mock_wls_detector_box|opticks_two_spheres)",
        r"Integration\.simg4ox\.(8x8SiPM_w_CSI_optial_grease|sibling_pair|preinit_macro)",
        r"Integration\.simg4ox\.(drich_.*|zero_genstep_profile)",
        r"Integration\.simg4ox_(multievent|multithread)",
        r"Integration\.simg4ox_rng_rebuild\.(on|off|counts_match|hits_match)",
    ]

    def setup_build_environment(self, env):
        # GLM 0.9.9+ requires this for experimental GTX headers such as
        # dual_quaternion, which are reached via string_cast in this codebase.
        if self.spec.satisfies("^glm@0.9.9:"):
            env.append_flags("CPPFLAGS", "-DGLM_ENABLE_EXPERIMENTAL")

    def cmake_args(self):
        args = [self.define("BUILD_TESTING", self.spec.satisfies("@0.6:") and self.run_tests)]
        return args

    def setup_run_environment(self, env):
        if self.spec.satisfies("@0.6.0:"):
            env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)

    def _has_cuda_device(self):
        nvidia_smi = which("nvidia-smi")
        if nvidia_smi is None:
            return False
        out = nvidia_smi("-L", output=str, error=str, fail_on_error=False)
        return nvidia_smi.returncode == 0 and "GPU " in out

    @run_after("cmake", when="@0.6:")
    def skip_gpu_tests(self):
        if not self.run_tests or self._has_cuda_device():
            return
        with working_dir(self.build_directory):
            ctest = Executable(join_path(self.spec["cmake"].prefix.bin, "ctest"))
            tests = re.findall(r"Test\s+#\d+: (\S+)", ctest("-N", output=str))
            gpu_tests = [t for t in tests if any(re.fullmatch(p, t) for p in self.gpu_tests)]
            with open("CTestCustom.cmake", "a") as f:
                f.write(
                    "set(CTEST_CUSTOM_TESTS_IGNORE ${CTEST_CUSTOM_TESTS_IGNORE} "
                    + " ".join(gpu_tests)
                    + ")\n"
                )

    test_gdml = join_path("tests", "geom", "raindrop.gdml")

    @run_after("install", when="@0.6:")
    def copy_test_files(self):
        cache_extra_test_sources(self, [self.test_gdml])

    def test_consgeo(self):
        """convert a GDML geometry into a CSG geometry (no GPU needed)"""
        if not self.spec.satisfies("@0.6:"):
            raise SkipTest("Test requires simphony 0.6.0 or later")
        gdml = join_path(self.test_suite.current_test_cache_dir, self.test_gdml)
        consgeo = which("consgeo", path=self.prefix.bin, required=True)
        consgeo("-g", gdml, "-o", "csg")
        csg = join_path("csg", "raindrop", "CSGFoundry")
        for f in ["solid.npy", "prim.npy", "node.npy"]:
            assert os.path.isfile(join_path(csg, f)), f"consgeo did not write {f}"
