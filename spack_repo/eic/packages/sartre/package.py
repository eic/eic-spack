# Copyright 2013-2026 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Sartre(CMakePackage):
    """Sartre is an event generator for exclusive and inclusive diffraction
    and ultra-peripheral collisions in ep and eA, based on the dipole model."""

    homepage = "https://github.com/tobiastoll/sartre"
    url = "https://github.com/tobiastoll/sartre/archive/refs/tags/2.20.1.tar.gz"
    list_url = "https://github.com/tobiastoll/sartre/releases"
    git = "https://github.com/tobiastoll/sartre.git"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    license("GPL-3.0-or-later")

    version("main", branch="main")
    version("2.20.1", sha256="e1395f58560b7c5044a51af36e7af1a6c843f0e7e5c033c2bbdfe1980b5ca0ba")

    variant(
        "inclusive",
        default=True,
        description="Build inclusive diffraction event generation (requires Pythia8)",
    )
    variant("multithreaded", default=True, description="Build in multithreaded mode")
    variant("openmp", default=False, description="Enable OpenMP in table generation")
    variant("tools", default=True, description="Build table command-line tools")

    # The bundled Cuba library is built with a nested `make` invocation
    generator("make")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.30:", type="build")
    depends_on("gmake", type="build")

    depends_on("root@6.20:")
    depends_on("gsl")
    depends_on("pythia8", when="+inclusive")
    depends_on("boost@1.70: +thread", when="+multithreaded")
    depends_on("python@3:", type="run")

    def cmake_args(self):
        args = [
            self.define_from_variant("ENABLE_INCLUSIVE_DIFFRACTION", "inclusive"),
            self.define_from_variant("MULTITHREADED", "multithreaded"),
            self.define_from_variant("ENABLE_OMP", "openmp"),
            self.define_from_variant("SARTRE_BUILD_TOOLS", "tools"),
        ]
        if self.spec.satisfies("+inclusive"):
            args.append(self.define("PYTHIA8_DIR", self.spec["pythia8"].prefix))
        return args

    @property
    def libs(self):
        return find_libraries(
            ["libsartre", "libgemini", "libcuba"], root=self.prefix.sartre.lib, shared=False
        )

    @property
    def headers(self):
        return find_headers("*", root=self.prefix.sartre.include)

    def _setup_sartre_environment(self, env):
        env.set("SARTRE_DIR", self.prefix.sartre)
        env.prepend_path("PATH", self.prefix.sartre.bin)

    def setup_run_environment(self, env):
        self._setup_sartre_environment(env)

    def setup_dependent_build_environment(self, env, dependent_spec):
        self._setup_sartre_environment(env)

    def setup_dependent_run_environment(self, env, dependent_spec):
        self._setup_sartre_environment(env)
