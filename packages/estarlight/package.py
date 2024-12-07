from spack.package import *


class Estarlight(CMakePackage):
    """Monte Carlo event generator for coherent vector meson photo- and electro-
    production in electron-ion collisions."""

    homepage = "https://github.com/eic/estarlight"
    url = "https://github.com/eic/estarlight/archive/refs/heads/master.zip"
    list_url = "https://github.com/eic/estarlight/releases"
    git = "https://github.com/eic/estarlight.git"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("master", branch="master")

    variant("hepmc3", default=True, description="Support HepMC3 writing")
    variant("doxygen", default=False, description="Build documentation")
    variant("pythia8", default=False, description="Use Pythia8 for parton showers")
    variant("pythia6", default=False, description="Use Pythia6 for parton showers")
    variant("dpmjet", default=False, description="Use dpmjet for jets")

    depends_on("cxx", type="build")

    depends_on("hepmc3", when="+hepmc3")
    depends_on("doxygen", when="+doxygen")
    depends_on("pythia8", when="+pythia8")
    depends_on("pythia6", when="+pythia6")
    depends_on("dpmjet", when="+dpmjet")

    def cmake_args(self):
        args = []
        return args
