# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.build_systems.bundle import BundlePackage
except ImportError:
    from spack.build_systems.bundle import BundlePackage


class Eic(BundlePackage):
    """EIC Softare Consortium environment."""

    homepage = "https://gitlab.com/eic"

    maintainer = ["wdconinc"]

    tags = ["eic"]

    version("develop", preferred=True)
    depends_on("escalate")
    depends_on("eicroot")
    depends_on("eictoymodel")
