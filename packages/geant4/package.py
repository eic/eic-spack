from spack import *
from spack.pkg.builtin.geant4 import Geant4 as BuiltinGeant4


class Geant4(BuiltinGeant4):
    ## Add to the hardcoded GEANT4 Birk's constants
    patch('birks.patch', when='@10.7.0:')
