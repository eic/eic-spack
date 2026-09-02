# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class EicAsk(PythonPackage):
    """Command-line interface for the EIC documentation query API."""

    homepage = "https://eic.github.io"
    pypi = "eic_ask/eic_ask-0.1.0.tar.gz"

    tags = ["eic", "hep"]

    maintainers("wdconinc", "aprozo")

    license("LGPL-2.1", checked_by="wdconinc")

    version("0.1.0", sha256="a5e398941208cc5edcebc7ef3f7b7bae07657cc02e5fdd33d5dd0c35c0c6f208")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@68:")
