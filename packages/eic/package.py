# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Eic(BundlePackage):
    """EIC Softare Consortium environment."""

    homepage = "https://gitlab.com/eic"

    maintainer = ["wdconinc"]

    tags = ["eic"]

    version("develop", preferred=True)
    depends_on("escalate")
    depends_on("eicroot")
    depends_on("eictoymodel")
