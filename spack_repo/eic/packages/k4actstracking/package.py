from spack.package import *

try:
    import spack.llnl.util.tty as tty
except ImportError:
    import llnl.util.tty as tty

try:
    from spack.pkg.k4.k4actstracking import K4actstracking as BuiltinK4actstracking
except ImportError:
    tty.warn("k4actstracking requires the key4hep-spack repository")
    from spack.package import Package as BuiltinK4actstracking


class K4actstracking(BuiltinK4actstracking):
    def patch(self):
        filter_file(
            "m_obj.write(m_outputFileName)",
            "m_obj.write(m_outputFileName.value())",
            "k4ActsTracking/src/components/ActsGeoSvc.cpp",
            string=True,
        )
