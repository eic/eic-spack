from spack import *
from spack.pkg.builtin.root import Root as BuiltinRoot


class Root(BuiltinRoot):
    patch(
        "hist-cmake.patch",
        when="@6.28.04",
    )
    patch(
        "https://github.com/root-project/root/pull/11788.patch?full_index=1",
        sha256="89294c428c679d4850f999df89f83c26a86b2dd410fb0cd3941bda0bca07dc32",
        when="@6.06.00:6.26.10",
    )
