from spack.package import *
from spack.pkg.builtin.root import Root as BuiltinRoot


class Root(BuiltinRoot):
    # Skip overlap checking if a partner is a tessellated shape
    patch(
        "https://github.com/root-project/root/pull/11788.patch?full_index=1",
        sha256="89294c428c679d4850f999df89f83c26a86b2dd410fb0cd3941bda0bca07dc32",
        when="@6.06.00:6.26.10",
    )
    # Allow producing forward compatible file for fBits value
    patch(
        "https://github.com/root-project/root/pull/15006.patch?full_index=1",
        sha256="93673f697bd4c7def71c3e8420b930d59546bc709e9fe6ed23a6dddd82fc104b",
        when="@6.30:6.30.4",
    )
