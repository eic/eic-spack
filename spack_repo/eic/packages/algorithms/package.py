# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Algorithms(CMakePackage):
    """Collection of Reconstruction Algorithms using DD4hep and EDM4hep."""

    homepage = "https://eic.github.io/algorithms"
    url = "https://github.com/eic/algorithms/archive/refs/tags/v1.1.0.tar.gz"
    git = "https://github.com/eic/algorithms.git"

    maintainers = ["wdconinc", "sly2j"]

    tags = ["eic"]

    test_requires_compiler = True

    version("main", branch="main")
    version("master", branch="master", deprecated=True)
    version("2.0.0", sha256="2904f321aa6875c2b1bde458723cf9a1ba029f2949ffc799ede39449da09fb18")
    version("1.3.0", sha256="1a134c86c899223d20de5d2eaf50f63423c8751ac6098c9c5a24db7e7125e3fb")
    version("1.2.0", sha256="893da7948baf9aa778b1716b3ce7331cd14befa7e43f3cce810c6b49235c73fd")
    version(
        "1.1.0",
        sha256="f7fef07ee4217b1d224bbe3f87e21e155e1e205356ad5a19b7d09558e7c5c024",
        deprecated=True,
    )  # exposes log() function
    version("1.0.0", sha256="b36598ba539938c0f8e5d75170f770e5701a1ad81dbee929ccc36df15233a99d")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("dd4hep +ddrec")
    depends_on("edm4hep")
    depends_on("edm4eic")
    depends_on("cppgsl")
    depends_on("fmt")

    def test_random_service(self):
        """compile and run a program that uses the algorithms random service"""
        with open("test_random.cpp", "w") as f:
            f.write(
                """#include <algorithms/logger.h>
#include <algorithms/random.h>

#include <cstdlib>
#include <iostream>

int main() {
  auto& serviceSvc = algorithms::ServiceSvc::instance();
  auto& randomSvc  = algorithms::RandomSvc::instance();
  randomSvc.setProperty("seed", std::size_t{42});
  serviceSvc.init();
  if (!serviceSvc.ready()) {
    std::cerr << "services not ready" << std::endl;
    return EXIT_FAILURE;
  }
  const auto generator = randomSvc.generator();
  double sum           = 0;
  for (int i = 0; i < 10000; ++i) {
    const double x = generator.uniform_double(2.0, 3.0);
    if (x < 2.0 || x >= 3.0) {
      std::cerr << "uniform_double out of range: " << x << std::endl;
      return EXIT_FAILURE;
    }
    sum += x;
  }
  const double mean = sum / 10000;
  std::cout << "algorithms::RandomSvc mean: " << mean << std::endl;
  return (mean > 2.45 && mean < 2.55) ? EXIT_SUCCESS : EXIT_FAILURE;
}
"""
            )
        fmt = self.spec["fmt"]
        # CXX is not set in the stand-alone test environment (compiler-wrapper is a build dep)
        cxx = Executable(self.spec["cxx"].package.cxx)
        cxx(
            "-std=c++20",
            f"-I{self.prefix.include}",
            f"-I{fmt.prefix.include}",
            f"-I{self.spec['cppgsl'].prefix.include}",
            "test_random.cpp",
            "-o",
            "test_random",
            *fmt.libs.ld_flags.split(),
            *[f"-Wl,-rpath,{d}" for d in fmt.libs.directories],
        )
        test_random = which("./test_random", required=True)
        out = test_random(output=str, error=str)
        assert "algorithms::RandomSvc mean:" in out
