from spack import *
from spack.pkg.builtin.hepmc3 import Hepmc3 as BuiltinHepmc3
class Hepmc3(BuiltinHepmc3):
    version("3.2.5", sha256="cd0f75c80f75549c59cc2a829ece7601c77de97cb2a5ab75790cac8e1d585032")
    patch('https://gitlab.cern.ch/hepmc/HepMC3/-/merge_requests/188.diff',
          sha256='775f312a72cc900751290f5a474ddccd9b8bf5bc37b6ac5c11da8dc2d9e1c561',
          when='@3.2.5')
