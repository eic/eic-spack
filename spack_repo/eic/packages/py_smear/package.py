# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySmear(PythonPackage):
    """Simple command line interface to eic-smear and jleic-smear
    particle smearing engines."""

    homepage = "https://gitlab.com/eic/escalate/smear"
    url = "https://files.pythonhosted.org/packages/81/b9/be65c5adaf171392e87a3d5d50004a9b5d7f1412a0c6011145508e90f28c/smear-0.1.6.tar.gz"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version(
        "0.1.6",
        sha256="29bf782a318657198e26a22fe1b7fd65b2784458e724eed6b664eade85db70e6",
    )

    depends_on("py-setuptools", type="build")
