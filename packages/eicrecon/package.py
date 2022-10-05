# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Eicrecon(CMakePackage):
    """EIC Reconstruction - JANA based."""

    homepage = "https://github.com/eic/eicrecon"
    url      = "https://github.com/eic/EICrecon/archive/refs/tags/v0.1.0.zip"
    git      = "https://github.com/eic/eicrecon.git"
    list_url = "https://github.com/eic/EICrecon/releases"

    maintainers = ['wdconinc']

    version('main', branch='main')
    version("0.1.0", sha256="dcc8b60530a627c825413c07472659ba155600339ef8b8e742e3c997bcc504ae")

    depends_on('cmake@3.8:', type='build')
    depends_on('jana2')
    depends_on('dd4hep')
    depends_on('edm4hep')
    depends_on('eic-ip6')
    depends_on('epic-eic')
    depends_on('fmt')

    def setup_build_environment(self, env):
        env.set('EDM4HEP_ROOT', self.spec['edm4hep'].prefix)

    def cmake_args(self):
        args = [
            self.define('DETECTOR_LIBS_IP6',
                self.spec['eic-ip6'].prefix),
            self.define('DETECTOR_LIBS_EPIC',
                self.spec['epic-eic'].prefix),
        ]
        return args
