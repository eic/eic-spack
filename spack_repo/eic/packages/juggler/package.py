from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Juggler(CMakePackage):
    """Concurrent event processor for NP experiments, based on the Gaudi framework."""

    homepage = "https://github.com/eic/juggler"
    url = "https://github.com/eic/juggler/archive/refs/tags/v15.2.0.tar.gz"
    git = "https://github.com/eic/juggler.git"
    list_url = "https://github.com/eic/juggler/tags"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("main", branch="main")
    version("master", branch="master", deprecated=True)
    version("15.2.0", sha256="6452d97ee08df85acced4a56cd1d411a7451145b972480e4c095e8b8a09636cd")
    version("15.1.0", sha256="a26c31c55ac440130dbb6c8d1325a84317987887b8ade231c5edc649cd3a7e6a")
    version("15.0.5", sha256="94f03e10b655759cfaf69e82d39036b0e7b3a8028e879a22f94ed54bf6ede6ec")
    version("15.0.4", sha256="5eab7c25b1e33d2033d52c8524aa531c757f12cb0dd53252be3cc552a5b9b7d4")
    version("15.0.3", sha256="f1051e1ac8b5fb1d3e7f502d7baeeb06b6cdab49ff5596cf409961f8c716f908")
    version("15.0.2", sha256="26d6980686eb936132266fe042ce96e8bfcc6987746e49f6f332e1238081e544")
    version("15.0.1", sha256="0a3e0c80408c826bece94135b370282e8c148c1117dc414d43bf32de4fe83c5e")
    version("15.0.0", sha256="afcf9b7039103eddc76b1410118e2b57628c8a7eefe7da490653244667de343b")
    version("14.3.0", sha256="e4dbaeb06a192da716835ce77e85d84b07d5fef6f934c3b54a3346672d1560a3")
    version("14.2.2", sha256="bd49e48d6e2699cd18a925391247773bb4ce853c2240f0b39ed4c549d4264292")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("root")
    depends_on("geant4")
    depends_on("dd4hep +ddg4")

    depends_on("gaudi@36:")
    conflicts("^gaudi@37:38 ~gaudialg", when="@:14", msg="GaudiAlgLib required through v14")

    depends_on("acts +json +dd4hep", when="@15.0.4:")
    depends_on("acts +json +tgeo +dd4hep", when="@14.2:15.0.3")
    depends_on("acts", when="@main")
    depends_on("acts@30:")

    depends_on("podio@0.11.0:")
    conflicts("^podio@1.5:", when="@:15.0.2")

    depends_on("edm4hep")
    conflicts("^edm4hep@1:", when="@:15.1")
    conflicts("^edm4hep@0.99:", when="@:15.0.0")

    depends_on("edm4eic")

    depends_on("cppgsl")

    depends_on("k4fwcore")
    depends_on("k4actstracking")

    depends_on("algorithms")
    depends_on("eicrecon")

    def cmake_args(self):
        args = []
        args.append(self.define("CMAKE_CXX_STANDARD", "20"))
        return args
