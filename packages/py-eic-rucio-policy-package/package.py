# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEicRucioPolicyPackage(PythonPackage):
    """Rucio policy package for the EIC collaborations."""

    homepage = "https://github.com/eic/eic_rucio_policy_package"
    pypi = "eic_rucio_policy_package/eic_rucio_policy_package-0.0.4.tar.gz"
    git = "https://github.com/eic/eic_rucio_policy_package.git"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("0.0.4", sha256="f66b860a45b43ec70b91d369024eea0cb08cd996c3c17da8bb21932d6ee72834")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")

    depends_on("py-jsonschema", type=("build", "run"))
    depends_on("py-rucio-clients", type=("build", "run"))
    depends_on("py-sqlalchemy", type=("build", "run"))
