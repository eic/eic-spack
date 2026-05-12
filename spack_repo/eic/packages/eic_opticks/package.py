# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.eic.packages.simphony.package import Simphony

from spack.package import *


class EicOpticks(Simphony):
    __doc__ = Simphony.__doc__