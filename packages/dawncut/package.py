# Copyright 203-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Dawncut(MakefilePackage):
    """DAWNCUT is a tool to generate a 3D scene data clipped with an arbitrary plane.
    It reads a source DAWN-format file and outputs a new DAWN-format data,
    describing a plane-clipped 3D scene.  The output DAWN-format data can be
    visualized with Fukui Renderer DAWN.
    """

    # dawn webpage not available anymore
    homepage = "https://geant4.kek.jp/~tanaka"
    url = "http://geant4.kek.jp/~tanaka/src/dawncut_1_54a.taz"
    maintainers = ["sly2j"]

    version(
        "1_54a",
        url="http://geant4.kek.jp/~tanaka/src/dawncut_1_54a.taz",
        sha256="531e1f0e2ed35de3e2b1803108c0efb732d83a0c676f14083bd41a71346b4fa9",
        expand=False,
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    phases = ["unpack", "repatch", "edit", "build", "install"]

    def unpack(self, spec, prefix):
        # Untar inner tar files
        def members(tf, tld):
            l = len(tld)
            for member in tf.getmembers():
                if member.path.startswith(tld):
                    member.path = member.path[l:]
                    yield member

        with working_dir(self.stage.source_path):
            import tarfile

            install_tar = tarfile.open("dawncut_1_54a.taz")
            install_tar.extractall(members=members(install_tar, "dawncut_1_54a/"))

    def repatch(self, spec, prefix):
        # Patch to add install directive to Makefile
        src = self.stage.source_path
        patches = self.package_dir
        which("patch")("-N", "-l", "-p1", "-i", join_path(patches, "install.patch"))

    def edit(self, spec, prefix):
        makefile = FileFilter("Makefile")
        makefile.filter("CC= .*", "CC = " + env["CC"])
        makefile.filter("CXX = .*", "CXX = " + env["CXX"])
        os.environ["INSTALL_DIR"] = "{}/bin".format(prefix)
