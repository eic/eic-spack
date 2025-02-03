from spack.package import *
from spack.pkg.builtin.root import Root as BuiltinRoot


class Root(BuiltinRoot):
    # Apply TFile::k630forwardCompatibility when creating new file if set in rootrc
    patch(
        "https://github.com/root-project/root/pull/17542.patch?full_index=1",
        sha256="0a30cc6f342f38494d62a7aa8bcd7e9de820264aea44c09b1305aae89e61a680",
        when="@6.30:6.34.02",
    )
    # Fix surface area calculation for TGeoTessellated facets
    patch(
        "https://github.com/wdconinc/root/commit/06db88c70f602c08c97c401b81afcf6adc2eb25e.diff?full_index=1",
        sha256="991905b17d246fb7584309fdeb5720d29a083a1313920562de1de1edb11675a6",
        when="@6.32",
    )
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
