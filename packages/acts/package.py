from spack.package import *
from spack.pkg.builtin.acts import Acts as BuiltinActs


class Acts(BuiltinActs):
    def __init__(self, spec):
        super(Acts, self).__init__(spec)
        # HACK Remove upstream limitations on podio@:0
        for _spec in ["@:35+edm4hep", "@:35+podio"]:
            if spack.spec.Spec(_spec) in Acts.dependencies:
                del Acts.dependencies[spack.spec.Spec(_spec)]

    # Plugins/Podio/edm.yml: add schema_version
    patch(
        "https://github.com/acts-project/acts/commit/8fce1a7b32aa39f967919adc4cabebbfde2a7a97.patch?full_index=1",
        sha256="78d4fac4235f7659c674a267f11e2d5bcad82af0d9df2036ef620d64997497d0",
        when="@30.3.0:34.0",
    )

    # CMakeLists.txt: fix ACTS_USE_SYSTEM_ACTSVG typo
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
        args.append(self.define("Python_EXECUTABLE", self.spec["python"].command.path))
        return args


# instantiate at least once
_acts = Acts(spack.spec.Spec("acts"))
