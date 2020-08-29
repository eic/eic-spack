# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Sherpa(AutotoolsPackage):
    """Sherpa is a Monte Carlo event generator for the Simulation of
    High-Energy Reactions of PArticles in lepton-lepton, lepton-photon,
    photon-photon, lepton-hadron and hadron-hadron collisions."""

    homepage = "https://sherpa-team.gitlab.io"
    git      = "https://gitlab.com/sherpa-team/sherpa.git"

    maintainers = ['wdconinc']

    version('2.2.10', branch='rel-2-2-10')

    _cxxstd_values = ('11', '14', '17')
    variant('cxxstd',    default='11', values=_cxxstd_values, multi=False,
            description='Use the specified C++ standard when building')

    variant('mpi',        default=False, description='Enable MPI')
    variant('python',     default=False, description='Enable Python API')
    variant('ufo',        default=False, description='Enable UFO support')
    variant('hepmc2',     default=False, description='Enable HepMC (version 2.x) support')
    variant('hepmc3',     default=False, description='Enable HepMC (version 3.x) support')
    variant('hepmc3root', default=False, description='Enable HepMC (version 3.1+) ROOT support')
    variant('rivet',      default=False, description='Enable Rivet support')
    variant('fastjet',    default=False, description='Enable FASTJET')
    #variant('blackhat',   default=False, description='Enable BLACKHAT') # FIXME not available
    #variant('openloops',  default=False, description='Enable OpenLoops') # FIXME not available
    #variant('recola',     default=False, description='Enable Recola') # FIXME not available
    #variant('mcfm',       default=False, description='Enable MCFM') # FIXME not available
    #variant('lhole',      default=False, description='Enable Les Houches One-Loop Generator interface') # FIXME not available
    variant('root',       default=False, description='Enable ROOT support')
    variant('lhapdf',     default=False, description='Enable LHAPDF support')
    #variant('hztool',     default=False, description='Enable hztool for analysis') # FIXME not available
    variant('cernlib',    default=False, description='Enable cernlib')
    #variant('pgs',        default=False, description='Enable pgs') # FIXME not available
    # FIXME delphes integration is utterly broken https://sherpa.hepforge.org/trac/ticket/305
    #variant('delphes',    default=False, description='Enable delphes')
    variant('gzip',       default=False, description='Enable gzip support')
    variant('pythia',     default=False, description='Enable fragmentation/decay interface to Pythia')
    variant('sqlite3',    default=False, description='Use SQLite 3 library')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('mpi',       when='+mpi')
    depends_on('python',    when='+python')
    depends_on('ufo',       when='+ufo')
    depends_on('hepmc',     when='+hepmc2')
    depends_on('hepmc3',    when='+hepmc3')
    depends_on('hepmc3 +rootio', when='+hepmc3root')
    depends_on('rivet',     when='+rivet')
    depends_on('fastjet',   when='+fastjet')
    depends_on('blackhat',  when='+blackhat')
    depends_on('openloops', when='+openloops')
    depends_on('recola',    when='+recola')
    depends_on('mcfm',      when='+mcfm')
    depends_on('lhole',     when='+lhole')
    depends_on('root',      when='+root')
    depends_on('lhapdf',    when='+lhapdf')
    depends_on('hztool',    when='+hztool')
    depends_on('cernlib',   when='+cernlib')
    depends_on('pgs',       when='+pgs')
    depends_on('delphes',   when='+delphes')
    depends_on('gzip',      when='+gzip')
    depends_on('pythia6',   when='+pythia')
    depends_on('sqlite',    when='+sqlite3')

    for std in _cxxstd_values:
        depends_on('delphes cxxstd=' + std, when='+delphes cxxstd=' + std)
        depends_on('root cxxstd=' + std, when='+root cxxstd=' + std)

    def patch(self):
        filter_file(r'#include <sys/sysctl.h>',
                    '#ifdef ARCH_DARWIN\n#include <sys/sysctl.h>\n#endif',
                    'ATOOLS/Org/Run_Parameter.C')

    def configure_args(self):
        # Unused configure options:
        #  --enable-shared[=PKGS]  build shared libraries [default=yes]
        #  --enable-fast-install[=PKGS]
        #                          optimize for fast installation [default=yes]
        #  --disable-libtool-lock  avoid locking (might break parallel builds)
        #  --enable-versioning     Add version tag to executables and library/header
        #                          directories, such that multiple Sherpa versions can
        #                          live in the same prefix.
        #  --enable-hepevtsize=HEPEVT_SIZE
        #                          HEPEVT common block size [default=10000]
        #  --enable-binreloc       Enable binrelocing
        args = []
        if self.spec.satisfies('+mpi'):
            args.append('--enable-mpi')
        if self.spec.satisfies('+python'):
            args.append('--enable-pyext')
        if self.spec.satisfies('+ufo'):
            args.append('--enable-ufo')
        if self.spec.satisfies('+analysis'):
            args.append('--enable-analysis')
        if self.spec.satisfies('+lhole'):
            args.append('--enable-lhole')
        if self.spec.satisfies('+gzip'):
            args.append('--enable-gzip')
        if self.spec.satisfies('+pythia'):
            args.append('--enable-pythia')
        if self.spec.satisfies('+hepmc2'):
            args.append('--enable-hepmc2=' + self.spec['hepmc'].prefix)
        if self.spec.satisfies('+hepmc3'):
            args.append('--enable-hepmc3=' + self.spec['hepmc3'].prefix)
        if self.spec.satisfies('+rivet'):
            args.append('--enable-rivet=' + self.spec['rivet'].prefix)
        if self.spec.satisfies('+fastjet'):
            args.append('--enable-fastjet=' + self.spec['fastjet'].prefix)
        if self.spec.satisfies('+blackhat'):
            args.append('--enable-blackhat=' + self.spec['blackhat'].prefix)
        if self.spec.satisfies('+openloops'):
            args.append('--enable-openloops=' + self.spec['openloops'].prefix)
        if self.spec.satisfies('+recola'):
            args.append('--enable-recola=' + self.spec['recola'].prefix)
        if self.spec.satisfies('+mcfm'):
            args.append('--enable-mcfm=' + self.spec['mcfm'].prefix)
        if self.spec.satisfies('+root'):
            args.append('--enable-root=' + self.spec['root'].prefix)
        if self.spec.satisfies('+lhapdf'):
            args.append('--enable-lhapdf=' + self.spec['lhapdf'].prefix)
        if self.spec.satisfies('+hztool'):
            args.append('--enable-hztool=' + self.spec['hztool'].prefix)
        if self.spec.satisfies('+cernlib'):
            args.append('--enable-cernlib=' + self.spec['cernlib'].prefix)
        if self.spec.satisfies('+pgs'):
            args.append('--enable-pgs=' + self.spec['pgs'].prefix)
        if self.spec.satisfies('+delphes'):
            args.append('--enable-delphes=' + self.spec['delphes'].prefix)
        if self.spec.satisfies('+sqlite3'):
            args.append('--with-sqlite3=' + self.spec['sqlite'].prefix)
        return args
