# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Irt(CMakePackage):
    """Indirect Ray Tracing library for EPIC Cherenkov detector reconstruction."""

    homepage = "https://github.com/eic/irt"
    url = "https://github.com/eic/irt/archive/refs/tags/v1.0.0.zip"
    list_url = "https://github.com/eic/irt/tags"
    git = "https://github.com/eic/irt.git"

    maintainers = ["wdconinc", "c-dilks"]
    tags = ["eic"]

    version("1.0.5", sha256="b51006ae517a685e6a1004ec0f6cd538317801319ede51f8c806d23690c7648e")
    version("1.0.4", sha256="8e0bc2542c10d208e933418265a235922dc542026aa2cb0a58d5dc838677dfac")
    version("1.0.3", sha256="b28dea9880dcf84384ede6d672bf3b598446a229faa5197e86bcaa433a0186db")
    version("1.0.2_fixed", sha256="e97e57d043b88bfbce2e1a9534e0b9e98cb59e16f4f788587bf3d16e02154419")
    version("1.0.2", sha256="9e88df94a675bccbbd679c9fccb2e3d63d23edcfc9d487f6073b39b462e841f9")
    version("1.0.1", sha256="9e916f145a5a6045a1f9ad2130538e3c58e8c2342c77da831e5021aa752dc1c3")
    version("1.0.0", sha256="55746700a477ed4decbdadbc008b43f370071cdd699452b96d7daa1dbc4ee28d")

    patch(
        "https://patch-diff.githubusercontent.com/raw/eic/irt/pull/32.patch?full_index=1",
        sha256="66b53acc8a443e7f05bdb9de97a91c924092fbc92b7981b736c631b14173f3dd",
        when="@1.0.5",
    )

    depends_on("root@6: +root7")
