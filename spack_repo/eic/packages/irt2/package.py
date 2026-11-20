# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Irt2(CMakePackage):
    """Indirect Ray Tracing library for EPIC Cherenkov detector reconstruction."""

    homepage = "https://github.com/eic/irt"
    url = "https://github.com/eic/irt/archive/refs/tags/v2.1.0.zip"
    list_url = "https://github.com/eic/irt/tags"
    git = "https://github.com/eic/irt.git"

    maintainers = ["chchatte92", "veprbl"]
    tags = ["eic"]

    version("2.2.3", sha256="6b9d5a74491a12fe74e511f3041ec450da6cd3881a5df7b93993894f5307aac4")
    version("2.2.2", sha256="7781431843c57ca1de63dbb4ab3b66abd75e3526b46b1d77fba548adaa1c7807")
    version("2.2.1", sha256="3ec8e7438e1e44222b48579ba91318dd7e441ff813d2b06d20e54e0c829a8eae")
    version("2.2.0", sha256="30bd092583d41326582ec255d5a8b1c0ceabb1371211340d1afabb93b7c3ccdf")
    version("2.1.3", sha256="68ba8abdcaa3266ef0e61e442cf65c2c2b2cbc758502e11b2a56e10361c7cf55")
    version("2.1.2", sha256="93232b2c40f574410c4c3045c997c0f9c572280b6cfe2e30af589f36ea82106e")
    version("2.1.1", sha256="214ab5918b9fcf4a3bebc3f8fa5e06c0d0dc77ff7d2233d771c83967af5a634d")
    version("2.1.0", sha256="906a0cf7ec111bbf7e3f95d48daa8be6f0de592ffde2222aeec53f371abc2cb7")

    variant("root_io", default=False, description="Build dictionaries for ROOT IO")
    variant(
        "json",
        default=True,
        description="Import/export calibrations in JSON format (needed for QE setup)",
        when="@2.2:",
    )

    depends_on("cxx", type="build")

    depends_on("root@6: +root7")
    depends_on("nlohmann-json@3.11.2:", when="+json")

    def cmake_args(self):
        args = ["-DEVALUATION=OFF", "-DDELPHES=OFF"]
        args.append(self.define_from_variant("IRT_ROOT_IO", "root_io"))
        args.append(self.define_from_variant("JSON_IMPORT_EXPORT", "json"))
        return args

    def test_flat_surface(self):
        """compile and run a program that intersects a ray with an IRT2 surface"""
        source = join_path(self.test_suite.current_test_data_dir, "test_flat_surface.cpp")
        libs = find_libraries("libIRT2", root=self.prefix, shared=True, recursive=True)
        assert libs, "libIRT2 not found"
        root_config = which("root-config", path=self.spec["root"].prefix.bin, required=True)
        root_libdir = root_config("--libdir", output=str).strip()
        root_flags = root_config("--cflags", "--libs", output=str).split()
        # IRT2 exports DISABLE_ROOT_IO through its CMake target when built without dictionaries
        defs = [] if self.spec.satisfies("+root_io") else ["-DDISABLE_ROOT_IO"]
        # CXX is not set in the stand-alone test environment (compiler-wrapper is a build dep)
        cxx = Executable(self.spec["cxx"].package.cxx)
        cxx(
            *defs,
            f"-I{self.prefix.include.IRT2}",
            source,
            "-o",
            "test_flat_surface",
            *libs.ld_flags.split(),
            *root_flags,
            *[f"-Wl,-rpath,{d}" for d in libs.directories + [root_libdir]],
        )
        test_flat_surface = which("./test_flat_surface", required=True)
        out = test_flat_surface(output=str, error=str)
        assert "crossing: 1 z=10" in out
