from spack import *
from spack.pkg.k4.k4fwcore import K4fwcore as BuiltinK4fwcore


class K4fwcore(BuiltinK4fwcore):
    # Allow podio@1: in CMakeLists.txt
    patch(
        "https://github.com/key4hep/k4FWCore/commit/d6e72d1fe24fe3e1c28d667a84e9f97e295d8976.patch?full_index=1",
        sha256="55c77a1eb7b57d14e0901f178bdd630311bebdd75eb971d659e37657a90e5738",
        when="@1.0pre17:1.0pre19",
    )
