from spack.package import *

try:
    from spack.pkg.k4.k4actstracking import K4actstracking as BuiltinK4actstracking

    class K4actstracking(BuiltinK4actstracking):
        def patch(self):
            filter_file(
                "m_obj.write(m_outputFileName)",
                "m_obj.write(m_outputFileName.value())",
                "k4ActsTracking/src/components/ActsGeoSvc.cpp",
                string=True,
            )

except:
    pass
