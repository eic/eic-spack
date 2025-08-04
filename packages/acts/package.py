from spack.package import *
from spack.pkg.builtin.acts import Acts as BuiltinActs
from spack.spec import Spec


class Acts(BuiltinActs):
    def __init__(self, spec):
        super(Acts, self).__init__(spec)
        # HACK Remove upstream limitations on podio@:0
        for _spec in ["@:35+edm4hep", "@:35+podio"]:
            if Spec(_spec) in Acts.dependencies:
                del Acts.dependencies[Spec(_spec)]

    # Off-axis forward detector fixes
    patch(
        "https://github.com/acts-project/acts/commit/05eb9c9ca448e56cef79ae8678e50e8b0895cb1f.patch?full_index=1",
        sha256="7f985f9d2a0e32c1df7252ae0b7216f8577c767e6126ad8de2e9cf94c5288d1a",
        when="@36:42",
    )
    patch(
        "https://github.com/acts-project/acts/commit/f812fb17537712f5d31df803ef6c052fea9a90b8.patch?full_index=1",
        sha256="0e54a524b8e21c4fcf62b56606de0816c9f65f1c095b299578a7a3831683fc29",
        when="@9:42",
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
