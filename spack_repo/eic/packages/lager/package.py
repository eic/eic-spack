# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Lager(CMakePackage):
    """lAger is the Argonne generic l/A-event generator, a flexible MC generator
    system to simulate electro- and photo-production off nucleons and nuclei."""

    homepage = "https://eicweb.phy.anl.gov/monte_carlo/lager"
    url = "https://eicweb.phy.anl.gov/monte_carlo/lager/-/archive/3.7.0/lager-3.7.0.tar.gz"
    git = "https://eicweb.phy.anl.gov/monte_carlo/lager.git"

    tags = ["hep", "eic"]

    maintainers("wdconinc", "sly2j")

    license("GPL-3.0-or-later", checked_by="wdconinc")

    version("3.7.0", sha256="3ba025b744caae17e7109d8f8a19edd3e2ffdd79d07ff692373f15e92310f2f5")

    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.8:", type="build")

    depends_on("root +math")
    depends_on("boost +program_options +filesystem +system")
    depends_on("gsl")
    depends_on("hepmc")
    depends_on("hepmc3")
    depends_on("photos +hepmc +hepmc3")
    depends_on("jpacphoto")
    depends_on("fmt")

    conflicts("^boost@1.89:1.90", msg="Boost 1.89 and 1.90 do not ship a CMake config for system")

    def cmake_args(self):
        args = []
        # Add Find*.cmake modules to module path
        args.append(f"-DCMAKE_MODULE_PATH={self.package_dir}")
        # Set HepMC directory for FindHepMC.cmake
        args.append(f"-DHEPMC_DIR={self.spec['hepmc'].prefix}")
        # Set PHOTOS++ directory for Findphotospp.cmake
        args.append(f"-DPHOTOSPP_DIR={self.spec['photos'].prefix}")
        return args
