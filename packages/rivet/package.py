from spack.package import *
from spack.pkg.builtin.rivet import Rivet as BuiltinRivet


class Rivet(BuiltinRivet):
    with when("@4.1:"):
        variant("plugin-match", default="none", multi=True, description="List of Rivet analyses to be included")
        variant("plugin-unmatch", default="none", multi=True, description="List of Rivet analyses to be excluded")

    def cmake_args(self):
        args = super().cmake_args()

        if "plugin-match" in self.spec.variants:
            val = self.spec.variants["plugin-match"].value
            if "none" not in val:
                args += [f"--with-plugin-match={' '.join(val)}"]

        if "plugin-unmatch" in self.spec.variants:
            val = self.spec.variants["plugin-unmatch"].value
            if "none" not in val:
                args += [f"--with-plugin-unmatch={' '.join(val)}"]

        return args
