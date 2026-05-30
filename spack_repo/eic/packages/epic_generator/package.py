from spack.package import *

from spack_repo.builtin.packages.epic.package import Epic as BuiltinEpic


class EpicGenerator(BuiltinEpic):
    __doc__ = BuiltinEpic.__doc__

    tags = ["eic"]
