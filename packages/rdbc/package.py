# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install rdbc
#
# You can edit this file again by typing:
#
#     spack edit rdbc
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Rdbc(Package):
    """RDBC is a ROOT-ODBC interface for sPHENIX calibrations."""

    homepage = "http://github.com/eic/RDBC"
    url      = "http://github.com/eic/RDBC/archive/master.zip"
    git      = "http://github.com/eic/RDBC.git"

    version('master', branch='master')

    depends_on('libodbcpp')
    depends_on('root')

    def install(self, spec, prefix):
        autogen = Executable(join_path(self.stage.source_path,'autogen.sh'))
        args = []
        args.append('--prefix=%s' % self.spec.prefix)
        args.append('--with-odbc')
        autogen(*args)
        make()
        make('install')
