# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Jpacphoto(CMakePackage):
    """jpacPhoto is a framework for amplitude analysis involving single
    meson production via quasi-elastic scattering of a real photon on a
    nucleon target."""

    homepage = "https://eicweb.phy.anl.gov/monte_carlo/jpacPhoto"
    url = "https://eicweb.phy.anl.gov/monte_carlo/jpacPhoto/-/archive/v1.0.1/jpacPhoto-v1.0.1.tar.gz"
    git = "https://eicweb.phy.anl.gov/monte_carlo/jpacPhoto.git"

    tags = ["hep", "eic"]

    maintainers("wdconinc", "sly2j")

    license("MIT", checked_by="wdconinc")

    version("1.0.1", sha256="80e52c5330f330cf2bf2cd785e11938d56c59e58aedb655c0daa02decfc17838")

    depends_on("cxx", type="build")
    depends_on("cmake@3.8:", type="build")

    depends_on("root +math")
