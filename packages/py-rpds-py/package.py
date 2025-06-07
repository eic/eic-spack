from spack.package import *
from spack.pkg.builtin.acts import PyRpdsPy as BuiltinPyRpdsPy
from spack.spec import Spec


class PyRpdsPy(BuiltiPyRpdsPy):
    depends_on("rust@1.76:", type="build", when="@0.19:")

    def __init__(self, spec):
        super(PyRpdsPy, self).__init__(spec)
        # HACK Remove rust as a runtime dependency
        for _spec in ["@0.19:"]:
            if Spec(_spec) in PyRpdsPy.dependencies:
                del PyRpdsPy.dependencies[Spec(_spec)]

# instantiate at least once
_pyrpdspy = PyRpdsPy(Spec("py-rpds-py"))
