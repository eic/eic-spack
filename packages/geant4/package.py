from spack import *
from spack.pkg.builtin.geant4 import Geant4 as BuiltinGeant4


class Geant4(BuiltinGeant4):
    ## Versions with the eAST physics list
    version("11.2.1.east", git="https://github.com/eic/geant4", branch="east-v11.2.1")
    version("11.2.0.east", git="https://github.com/eic/geant4", branch="east-v11.2.0")
    version("11.1.3.east", git="https://github.com/eic/geant4", branch="east-v11.1.3")
    version("11.1.2.east", git="https://github.com/eic/geant4", branch="east-v11.1.2")
    version("11.1.1.east", git="https://github.com/eic/geant4", branch="east-v11.1.1")

    patch("G4LogicalSkinSurface.patch", when="@11.2")
