# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class EicSmear(CMakePackage):
    """Monte Carlo analysis package originally
    developed by the BNL EIC task force."""

    homepage = "https://wiki.bnl.gov/eic/index.php/Monte_Carlo_and_Smearing"
    url = "https://github.com/eic/eic-smear/archive/1.0.4.tar.gz"
    list_url = "https://github.com/eic/eic-smear/releases"
    git = "https://github.com/eic/eic-smear.git"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    variant("pythia6", default=False, description="Include Pythia6 support")

    version("master", branch="master")
    version(
        "1.1.12", sha256="9f95bbdd8bfffc2082ead67d17d240f0c057559e8727607bd42fef72257fa85c",
    )
    version(
        "1.1.11", sha256="0cffcecd139af3a2604a756ded2f9ccdefecfbe045a07766cf3c62c455de30b0",
    )
    version(
        "1.1.10",
        sha256="2a5866166299f216528bf1e9a7177faa0fca849cb8b20b64e08107c828059c3b",
    )
    version(
        "1.1.9",
        sha256="a469455f44d8fc9abd7475cbf5ca2bad7f235b09d81f1fe41485d7fcca177080",
    )
    version(
        "1.1.8",
        sha256="93c991dcd5fda8490901cb6c75badfa0198d0b7e05c8637d9832f352e4b285c0",
    )
    version(
        "1.1.7",
        sha256="a026002303148f00374f8597cd99274371030697dee81d910331d3bb8074bb80",
    )
    version(
        "1.1.4",
        sha256="bfa9304301b83b2f1c3e355ad1bce50036f0bc93289f1510665cc4cb31a48601",
    )
    version(
        "1.1.3",
        sha256="61561da2483775b9aba22bfea8b99bdd073f3fa222bdf4297ca9bab6c44e29d9",
    )
    version(
        "1.1.2",
        sha256="bc5eabec74786be3bebf9d61bb2ee3e56dcafe9b457b00c9a85bc89f1d1f9cd0",
    )
    version(
        "1.1.1",
        sha256="9c0f1162229e42f6f98213e49326d6279e42318726560989b05335db002a5854",
    )
    version(
        "1.1.0",
        sha256="9d2c37e389c588208c16c93aac0e6f5f36a141f4dbab07d2ced1c71e19378ef3",
    )
    version(
        "1.0.4-fix1",
        sha256="ae312f4440b7ec5eeda75631bea209d733186199eaa3cd76c757ba1337679392",
    )
    version(
        "1.0.4",
        sha256="7d12a1d8b1c490502cd73737e1ce264880b04e74c16ee3b27cabad371c5b9e73",
    )
    version(
        "1.0.3",
        sha256="74b0e7a690b8fe81eb2e2ea78f96cb75aadca1c8b08450e89a7ebf8963a4d44c",
    )
    version(
        "1.0.2",
        sha256="5f33b8ba75120918023be458d9fb0f138e1d41dd37ca7107d3aa6e0ab51b691c",
    )
    version(
        "1.0.1",
        sha256="60b4222e41c6cf5c9cbb30c85e388ce06f1e585c5a970d34ef4d1394c058ccdc",
    )
    version(
        "1.0.0",
        sha256="be994c94b5b665f3802723a51e5983a0d9221ca3b13138146d68ba48eb0b2d93",
    )

    depends_on("cxx", type="build")
    depends_on("cmake", type="build")

    depends_on("root +pythia6", when="+pythia6")
    depends_on("root", when="-pythia6")
    depends_on("zlib")
    depends_on("hepmc3")
    depends_on("pythia6", when="+pythia6")

    conflicts(
        "-pythia6",
        when="@1.1.0-rc1",
        msg="eic-smear@1.1.0-rc1 cannot be built without pythia6.",
    )

    def cmake_args(self):
        args = []

        args.append(
            "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value
        )
        if "+pythia6" in self.spec.variants:
            args.append("-DPYTHIA6_LIBDIR={0}".format(self.spec["pythia6"].prefix.lib))

        return args
