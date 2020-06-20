# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ejana(CMakePackage):
    """Implementation of EIC reconstruction in JANA."""

    homepage = "http://gitlab.com/eic/escalate/ejana/"
    url      = "http://gitlab.com/eic/escalate/ejana/-/archive/v1.2.1/ejana-v1.2.1.tar.gz"
    git      = "http://gitlab.com/eic/escalate/ejana.git"
    list_url = "https://gitlab.com/eic/escalate/ejana/-/tags"

    version('master', branch='master')
    version('1.2.2', sha256='d6e906591159014cbfa9a2a4ebc0354fdd8948436dddb8c3edc0bdf5d9544b69')
    version('1.2.1', sha256='80c1c16f7e350747c7980526c6c863db44c9b5dca9aadfe8e1be40e8ba352acd')
    version('1.2.0', sha256='9390facfcf77702efb102d3fda7711e2da025c7637b23f45ee055507fabda71a')

    variant('acts', default=False, description='Use ACTS')
    variant('genfit', default=False, description='Use genfit')

    depends_on('cmake@3.9:', type='build')
    depends_on('jana2')
    depends_on('hepmc3')
    depends_on('root@6.00.00:')
    depends_on('acts', when='+acts')
    depends_on('genfit', when='+genfit')

    # FIXME acts should be variant only
    depends_on('acts +identification +tgeo')

    # FIXME genfit should be variant only
    depends_on('genfit')

    def cmake_args(self):
        args = []

        args.append('-DROOT_DIR={0}'.format(
            self.spec['root'].prefix))
        args.append('-DJANA_DIR={0}'.format(
            self.spec['jana2'].prefix))
        args.append('-DHepMC3_DIR={0}'.format(
            self.spec['hepmc3'].prefix))
        # FIXME acts should be variant only
        args.append('-DActs_DIR={0}'.format(
            self.spec['acts'].prefix))
        if '+acts' in self.spec:
            args.append('-DActs_DIR={0}'.format(
                self.spec['acts'].prefix))
        # FIXME genfit should be variant only
        args.append('-DGENFIT_DIR={0}'.format(
            self.spec['genfit'].prefix))
        if '+genfit' in self.spec:
            args.append('-DGENFIT_DIR={0}'.format(
                self.spec['genfit'].prefix))

        return args

