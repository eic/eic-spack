from spack.package import *

try:
    from spack_repo.builtin.packages.epic.package import Epic as BuiltinEpic
except ImportError:
    from spack.pkg.builtin.epic import Epic as BuiltinEpic


class EpicGenerator(BuiltinEpic):
    __doc__ = BuiltinEpic.__doc__
