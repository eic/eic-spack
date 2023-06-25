from spack import *
from spack.pkg.builtin.acts import Acts as BuiltinActs


class Acts(BuiltinActs):
    patch(
        "https://github.com/acts-project/acts/commit/3255dfc3dddf9c7a82aaddb041d4a6f095d19124.patch?full_index=1",
        sha256="60317f6a09a7d57721c1234fcf087ae85aeab27653976d1d3ac7a846c3b85a89",
        when="@20.1.0:26",
    )
    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("Python_EXECUTABLE", self.spec["python"].command.path))
        return args
