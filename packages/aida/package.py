from spack import *
import os
import glob

class Aida(Package):
    """Abstract Interfaces for Data Analysis"""
    homepage = "http://aida.freehep.org"
    url      = "ftp://ftp.slac.stanford.edu/software/freehep/AIDA/v3.2.1/aida-3.2.1-src.tar.gz"

    version('3.2.1', 'c35073da04abfdd96ac9f4801f3da473')

    def install(self, spec, prefix):
        mkdirp(prefix.include)
        cp = which('cp')
        cp('-r', 'src/cpp/AIDA', prefix + '/include')
