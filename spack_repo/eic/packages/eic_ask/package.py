# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class EicAsk(PythonPackage):
    """Command-line interface for the EIC documentation query API."""

    homepage = "https://eic.github.io"
    pypi = "eic_ask/eic_ask-0.1.0.tar.gz"
    git = "https://github.com/eic/eic-ask.git"

    tags = ["eic", "hep"]

    maintainers("wdconinc", "aprozo")

    license("LGPL-2.1-or-later", checked_by="wdconinc")

    version("0.2.3", sha256="f3c551e284e1b7ed17d9d5d904bbde37bd5ec8516e4bf65967e5fe540eff1edb")
    version("0.2.2", sha256="8fcfb904bb0db80a686b5d43e1f1ee12151a42ff846cd3e4aab6f29db3dfb322")
    version("0.1.0", sha256="a5e398941208cc5edcebc7ef3f7b7bae07657cc02e5fdd33d5dd0c35c0c6f208")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@68:")

    def setup_build_environment(self, env):
        # `--test root` runs the import test in this environment, set up before
        # the install; python-venv adds site-packages only once it exists
        venv = self.spec["python-venv"].package
        for d in {venv.platlib, venv.purelib}:
            env.prepend_path("PYTHONPATH", join_path(self.prefix, d))
