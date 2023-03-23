from spack import *
from spack.pkg.builtin.root import Root as BuiltinRoot


class Root(BuiltinRoot):
    version("6.28.02", sha256="6643c07710e68972b00227c68b20b1016fec16f3fba5f44a571fa1ce5bb42faa")
    patch(
        "https://github.com/root-project/root/pull/11788.patch?full_index=1",
        sha256="89294c428c679d4850f999df89f83c26a86b2dd410fb0cd3941bda0bca07dc32",
        when="@6.06.00:6.26.10",
    )
