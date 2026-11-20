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

    version("2.3.0", sha256="c4457db2a425eb01162d9dd3ba50a2e1a8817ab9fed104ebdd4582e82d44582f")
    version("2.2.3a11", sha256="ad6ab7115c43ec1de563280edd945e3a865c288f58bce7fb345bbcddfeea6879")
    version("2.2.3a10", sha256="c7dbd97105d4bbd629b575cb7b3c9a1e757368ac60ae023565504a18b96496fe")
    version("2.2.3a9", sha256="65569fb1df3c86ac5f658a18d943c31211777dfcb020a3b2086252f01ae25dc5")
    version("2.2.3a8", sha256="db930a8c69e9a8da119bc0ffeab7d144d7af954301dd0f2e3e5bbca60b861c16")
    version("2.2.3a7", sha256="e89228b961583c22ef31651df57a8fa7788ff840f59d27e6a9cbfe003fff8dd2")
    version("2.2.3a6", sha256="928e85e7de4b6ce51d999ea088bb7c9cde556160bab7f5b03ed25389849f6963")
    version("2.2.3a5", sha256="3343f31a52954b986fb22ed77822dc6605c1ca5450e99185a8763aa72ed2a205")
    version("2.2.3a4", sha256="624c5746147416d675f0d6b94210257ef45934667052c078ed265fd10821b5e2")
    version("2.2.3a3", sha256="43d0136349732dfdc297de0d86b8c33e0a717579dc00a1968b4e9a71dd752566")
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
