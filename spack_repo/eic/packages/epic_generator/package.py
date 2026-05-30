from spack_repo.builtin.packages.epic.package import Epic as BuiltinEpic

from spack.package import *


class EpicGenerator(BuiltinEpic):
    __doc__ = BuiltinEpic.__doc__

    tags = ["eic"]
