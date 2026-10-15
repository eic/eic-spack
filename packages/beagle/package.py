from spack import *


class Beagle(MakefilePackage):
    """BeAGLE, Benchmark eA Generator for LEptoproduction, is a Fortran
    program designed as a general purpose eA Monte-Carlo generator."""

    homepage = "https://gitlab.in2p3.fr/BeAGLE/BeAGLE"
    url      = "https://gitlab.in2p3.fr/BeAGLE/BeAGLE/-/archive/v1.01.00/BeAGLE-v1.01.00.tar.gz"

    maintainers = ["wdconinc"]

    license("UNKNOWN")

    version("1.03.02", sha256="02b2af1eeeb33e699e4c1ba5cc01b61ef5ca8f0f41fcc2905d4d8acc77e6fc79")
    version("1.03.01", sha256="0d918032fdbb56dd602dfc051f6cbe80597210dd3bdb92c98ab654549c4060bd")
    version("1.03.00", sha256="85e5ef8b153f1fba32a95c4059ded987a8daa81627db548f479dec48d1347283")
    version("1.02.00", sha256="64d54c96a1b3c9965b56dc965d13e767f885a48e8b88f007a9fce69ff78bbd53")
    version("1.01.04", sha256="a141e62912aed1f5b7369b82d64d835eb1e19ca7b3d7cedbec8437ee927c0853")
    version("1.01.03", sha256="adaefed4aaf619f587b44e0d4bb6d94ae47220d59ac88f54c1611536a64e9852")
    version("1.01.02", sha256="78c33504ebadc86e3d900f33faa23a98202737314108f3e0181cf53684b9cd85")
    version("1.01.01", sha256="c54c73e4ad58cb718354f6d355ea81915d3dc1711d36425ce93efa66c35ccf5b")
    version("1.01.00", sha256="d2ff1a691a6ba23ada442e8a303432ac9021f107b86bed621fd06c49cef3bb54")
    version("1.00.01", sha256="2fc5d42250971c0261a0426783231c42c0057b4b0136ddaf69f2f4308604b4ce")
    version("1.00.00", sha256="ae904d9e54f8f2d126a4ebc1da1b451c230ef3368cde26c570de3c33b3c3eb93")

    depends_on("fluka")
    depends_on("lhapdf5")
    depends_on("pythia6")
    depends_on("cernlib")

    def edit(self, spec, prefix):
        filter_file(r"^FLUKA = /.*",
                    r"FLUKA = $(FLUPRO)",
                    "Makefile")
        filter_file(r"^LIB1 = -L/cern64/pro/lib",
                    r"LIB1 = -L{}".format(self.spec["cernlib"].lib),
                    "Makefile")
        filter_file(r"^LIB3 = -L/afs/rhic/eic/lib",
                    r"LIB3 = -L{}".format(self.spec["lhapdf5"].lib),
                    "Makefile")

    def install(self, spec, prefix):
        make("all")
