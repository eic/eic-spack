from spack.package import *


class East(CMakePackage):
    """Project eAST is a eA simulation toolkit."""

    homepage = "https://github.com/eic/east"
    url = "https://github.com/eic/east"
    list_url = "https://github.com/eic/east/releases"
    git = "https://github.com/eic/east.git"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("main", branch="main")

    depends_on("cxx", type="build")

    depends_on("geant4@10.7.0: +threads")
    depends_on("hepmc3")
