from spack import *
from spack.pkg.builtin.geant4 import Geant4 as BuiltinGeant4


class Geant4(BuiltinGeant4):
    version("11.0.3", sha256="1e6560b802aa84e17255b83987dfc98a1457154fb603d0f340fae978238de3e7")

    ## Add to the hardcoded GEANT4 Birk's constants
    patch('birks.patch', when='@10.7.0:')
