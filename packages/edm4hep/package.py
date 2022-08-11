from spack import *
from spack.pkg.builtin.edm4hep import Edm4hep as BuiltinEdm4hep


class Edm4hep(BuiltinEdm4hep):
    version("0.6", sha256="625a5a939cb8d7a0a6ab5874a3e076d7dd5338446be3921b0cbc09de4d96b315")
    version("0.5", sha256="aae4f001412d57585751d858999fe78e004755aa0303a503d503a325ef97d7e0")
    version("0.4.2", sha256="5f2ff3a14729cbd4da370c7c768c2a09eb9f68f814d61690b1cc99c4248994f4")
    depends_on("podio@0.15:", when="@0.6:")

