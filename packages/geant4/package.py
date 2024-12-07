from spack.package import *
from spack.pkg.builtin.geant4 import Geant4 as BuiltinGeant4


class Geant4(BuiltinGeant4):
    ## Versions with the eAST physics list
    version("11.2.2.east", git="https://github.com/eic/geant4", branch="east-v11.2.2")
    version("11.2.1.east", git="https://github.com/eic/geant4", branch="east-v11.2.1")
    version("11.2.0.east", git="https://github.com/eic/geant4", branch="east-v11.2.0")
    version("11.1.3.east", git="https://github.com/eic/geant4", branch="east-v11.1.3")
    version("11.1.2.east", git="https://github.com/eic/geant4", branch="east-v11.1.2")
    version("11.1.1.east", git="https://github.com/eic/geant4", branch="east-v11.1.1")

    patch("G4LogicalSkinSurface.patch", when="@11.2:11.2.1")

    ## Fix commands in /particle/property/decay/
    patch("https://github.com/Geant4/geant4/commit/e32bc92498d87fb42829b08348d7fad89bc89404.diff?full_index=1",
          sha256="a63b098f3214eaf4b5f34b3e434603b1cdbd13c919456782e933cd7422a45d99")
