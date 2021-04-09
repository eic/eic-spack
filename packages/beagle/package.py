from spack import *


class Beagle(MakefilePackage):
    """BeAGLE, Benchmark eA Generator for LEptoproduction, is a Fortran
    program designed as a general purpose eA Monte-Carlo generator."""

    homepage = "https://gitlab.in2p3.fr/BeAGLE/BeAGLE"
    url      = "https://gitlab.in2p3.fr/BeAGLE/BeAGLE/-/archive/v1.01.00/BeAGLE-v1.01.00.tar.gz"

    maintainers = ['wdconinc']

    version('1.01.00', sha256='d2ff1a691a6ba23ada442e8a303432ac9021f107b86bed621fd06c49cef3bb54')
    version('1.00.01', sha256='2fc5d42250971c0261a0426783231c42c0057b4b0136ddaf69f2f4308604b4ce')
    version('1.00.00', sha256='ae904d9e54f8f2d126a4ebc1da1b451c230ef3368cde26c570de3c33b3c3eb93')

    depends_on('fluka')
    depends_on('lhapdf5')
    depends_on('cernlib')

    def edit(self, spec, prefix):
        filter_file(r'^FLUKA = /.*',
                    r'FLUKA = $(FLUPRO)',
                    'Makefile')
        filter_file(r'^LIB1 = -L/cern64/pro/lib',
                    r'LIB1 = -L{}'.format(self.spec['cernlib'].lib),
                    'Makefile')
        filter_file(r'^LIB3 = -L/afs/rhic/eic/lib',
                    r'LIB3 = -L{}'.format(self.spec['lhapdf5'].lib),
                    'Makefile')

    def install(self, spec, prefix):
        make('all')
