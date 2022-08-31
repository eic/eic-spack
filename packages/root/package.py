from spack import *
from spack.pkg.builtin.root import Root as BuiltinRoot


class Root(BuiltinRoot):
    version("6.26.06", sha256="b1f73c976a580a5c56c8c8a0152582a1dfc560b4dd80e1b7545237b65e6c89cb")
    version("6.26.04", sha256="a271cf82782d6ed2c87ea5eef6681803f2e69e17b3036df9d863636e9358421e")

    # 6.26.00:6.26.06 fails for recent libc versions when ROOT7 is enabled
    patch(
        "https://github.com/root-project/root/pull/11111.patch?full_index=1",
        sha256="3115be912bd948979c9c2a3d89ffe6437fe17bd3b81396958c6cb6f51f64ae62",
        when="@6.26:6.26.06 +root7",
    )
    # 6.26.00:6.26.06 fails for recent nlohmann-json single headers versions
    patch(
        "https://github.com/root-project/root/pull/11225.patch?full_index=1",
        sha256="397f2de7db95a445afdb311fc91c40725fcfad485d58b4d72e6c3cdd0d0c5de7",
        when="@6.26:6.26.06 +root7 ^nlohmann-json@3.11:",
    )
