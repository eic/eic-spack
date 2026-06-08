# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyEicRucioPolicyPackage(PythonPackage):
    """Rucio policy package for the EIC collaborations."""

    homepage = "https://github.com/eic/eic_rucio_policy_package"
    pypi = "eic_rucio_policy_package/eic_rucio_policy_package-0.0.4.tar.gz"
    git = "https://github.com/eic/eic_rucio_policy_package.git"

    maintainers("panta-123")

    tags = ["eic"]

    license("Apache-2.0", checked_by="wdconinc")
    version("0.1.1", sha256="dfeff8571d76f6998a6e2ff3f3c989236c0d61ec707c4b6efbf254e117daf426")
    version("0.0.9", sha256="63caf566e8d72a7ca01970b9f6e8e2a837dfbd2ae507bdd49b092ae3f368dd92")
    version("0.0.8", sha256="a3d1a067762c4b895a5d72754c9590bc796da7c4c712b603ab3132ba31a2c43c")
    version("0.0.7", sha256="d24e4cc602a3bf035f5788efec18cc369f55aa60be7d441f2e81105ab0b2c12d")
    version("0.0.6", sha256="b734b846c2a568c93b29e9ac6d8ff018ff8f0a4bf1f02bc5f1520cba3eabfdd4")
    version("0.0.5", sha256="55b0e4bdfa7e8df575315989ef2998101f61be69941a068be3e8d343cd2e2916")
    version("0.0.4", sha256="f66b860a45b43ec70b91d369024eea0cb08cd996c3c17da8bb21932d6ee72834")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")

    depends_on("py-jsonschema", type=("build", "run"))
    depends_on("py-rucio-clients", type=("build", "run"))
    depends_on("py-rucio-clients@37.0.0:", type=("build", "run"), when="@0.1.1:")
    depends_on("py-sqlalchemy", type=("build", "run"))
