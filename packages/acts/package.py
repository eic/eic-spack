classspack.package import *
from spack.spec import Spec

try:
    from spack_repo.builtin.packages.acts.package import Acts as BuiltinActs
except:
    from spack.pkg.builtin.acts import Acts as BuiltinActs

class Acts(BuiltinActs):
    def __init__(self, spec):
        super(Acts, self).__init__(spec)
        # HACK Remove upstream limitations on podio@:0
        for _spec in ["@:35+edm4hep", "@:35+podio"]:
            if Spec(_spec) in Acts.dependencies:
                del Acts.dependencies[Spec(_spec)]

    # DD4hep layer builder fix
    variant("pr4620", default=False, description="Acts#4620: ensure DD4hep ProtoLayer understands local coordinate extent")
    patch(
        "https://github.com/acts-project/acts/compare/main...a9d1c8c99a3abcd8c697c9e95703352e757f81cf.diff?full_index=1",
        sha256="ccf241259fb50000aeb0580941880fd35c53e9b45877f9ad675bad25a00caf1d",
        when="@36:42 +pr4620",
    )
    conflicts("+pr4620", when="~pr4502")
    # Off-axis forward detector fixes
    variant("pr4502", default=False, description="Acts#4502: propagate transform to ProtoLayer in DD4hep builder")
    patch(
        "https://github.com/acts-project/acts/pull/4502.patch?full_index=1",
        sha256="d9bb4c9748233ac9f9e2bed3fc7d3aec9e5f5181729243be93b9c6eeee7db737",
        when="@36:42 +pr4502",
    )
    variant("pr4496", default=False, description="Acts#4496: enlarge cylinder volume rmax for layers with displaced center")
    patch(
        "https://github.com/acts-project/acts/pull/4496.patch?full_index=1",
        sha256="5aa1fee7437aaac8dc70bbac728c73fa42e59dd2e75ee4d2e7fbde1845889d08",
        when="@9:42 +pr4496",
    )

    # Core/src/Utilities/AxisDefinitions.cpp: parse correctly
    patch(
        "https://github.com/acts-project/acts/pull/4456.patch?full_index=1",
        sha256="d93a2792b40a82a412975ab183878e9f9d69a5018eef7a0a757ba650d31ab941",
        when="@39:",
    )

    # Plugins/Cuda/CMakeLists.txt: patch for c++20
    patch("Plugins_Cuda_CMakeLists.patch", when="@38:39.0")

    # Inline the ConstPodioTrackStateContainer copy constructor
    patch(
        "https://github.com/acts-project/acts/pull/4380.patch?full_index=1",
        sha256="85e7b52a21c9933d503e47a4d02e20fee61cb9d41fbe8c1471070d42a20d8ec8",
        when="@30.3.0:41",
    )

    # Remove unused G4Profiler.hh include
    patch(
        "https://github.com/acts-project/acts/commit/50dcda3890ce75b28b1485131b8da698603a73be.patch?full_index=1",
        sha256="4826f9718dba083cb67583ec7751550e9d39980649404272aa1b1c78247e4050",
        when="@35",
    )
    conflicts("^geant4@11.3:", when="@:34")

    # Plugins/Podio/edm.yml: add schema_version
    patch(
        "https://github.com/acts-project/acts/commit/8fce1a7b32aa39f967919adc4cabebbfde2a7a97.patch?full_index=1",
        sha256="78d4fac4235f7659c674a267f11e2d5bcad82af0d9df2036ef620d64997497d0",
        when="@30.3.0:34.0",
    )

    # CMakeLists.txt: fix ACTS_USE_SYSTEM_ACTSVG typo
    patch(
        "https://github.com/acts-project/acts/pull/3132.patch?full_index=1",
        sha256="e0c97940abc2b4eab50834f76dcfcf2e651b7bf961ad3dd6e124a56d4d5e1779",
        when="@30.3.0:34.0",
    )
    patch(
        "https://github.com/acts-project/acts/commit/3255dfc3dddf9c7a82aaddb041d4a6f095d19124.patch?full_index=1",
        sha256="60317f6a09a7d57721c1234fcf087ae85aeab27653976d1d3ac7a846c3b85a89",
        when="@20.1.0:26",
    )

    @when("@33:35")
    def patch(self):
        # HACK Remove upstream limitations on podio@:0
        filter_file("_acts_podio_version 0.16", "_acts_podio_version 1.0", "CMakeLists.txt")

    def cmake_args(self):
        args = super().cmake_args()
        if self.spec.satisfies("^python"):
            args.append(self.define("Python_EXECUTABLE", self.spec["python"].command.path))
        return args


# instantiate at least once
_acts = Acts(Spec("acts"))
