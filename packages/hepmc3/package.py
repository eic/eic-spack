from spack import *
from spack.pkg.builtin.hepmc3 import Hepmc3 as BuiltinHepmc3
class Hepmc3(BuiltinHepmc3):
    version("3.2.5", sha256="cd0f75c80f75549c59cc2a829ece7601c77de97cb2a5ab75790cac8e1d585032")
    patch('ReaderPlugin.patch',
          sha256='66354530bea9f68a1eb5a1fcceb829e5df6844ee0e0ea67aec2af55d5e4cfa78',
          when='@3.2.5')

    # copy over cmake_args to resolve https://github.com/spack/spack/issues/31648
    def cmake_args(self):
        spec = self.spec
        args = [
            "-DHEPMC3_ENABLE_PYTHON={0}".format(spec.satisfies("+python")),
            "-DHEPMC3_ENABLE_ROOTIO={0}".format(spec.satisfies("+rootio")),
            "-DHEPMC3_INSTALL_INTERFACES={0}".format(spec.satisfies("+interfaces")),
        ]

        if self.spec.satisfies("+python"):
            py_ver = spec["python"].version.up_to(2)
            args.extend(
                [
                    "-DHEPMC3_PYTHON_VERSIONS={0}".format(py_ver),
                    "-DHEPMC3_Python_SITEARCH{0}={1}".format(py_ver.joined, python_platlib),
                ]
            )

        if self.spec.satisfies("+rootio"):
            args.append("-DROOT_DIR={0}".format(self.spec["root"].prefix))
        args.append("-DHEPMC3_ENABLE_TEST={0}".format(self.run_tests))
        return args

