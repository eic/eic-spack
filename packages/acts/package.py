from spack import *
from spack.pkg.builtin.acts import Acts as BuiltinActs


class Acts(BuiltinActs):
    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("Python_EXECUTABLE", self.spec["python"].command.path))
        return args
