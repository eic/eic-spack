from spack import *
from spack.pkg.builtin.harfbuzz import Harfbuzz as BuiltinHarfbuzz


class Harfbuzz(BuiltinHarfbuzz):
    version("5.3.1", sha256="4a6ce097b75a8121facc4ba83b5b083bfec657f45b003cd5a3424f2ae6b4434d")

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path("XDG_DATA_DIRS", self.prefix.share)
        env.prepend_path("GI_TYPELIB_PATH", join_path(self.prefix.lib, "girepository-1.0"))

