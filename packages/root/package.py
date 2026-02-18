from spack.package import *

try:
    from spack_repo.builtin.packages.root.package import Root as BuiltinRoot
except ImportError:
    from spack.pkg.builtin.root import Root as BuiltinRoot

class Root(BuiltinRoot):
    version("6.32.14", sha256="dfb5193127ff80ebfa10e6a4dcdf56eeec0eface65fc3de347d853ae9653aeff")
    version("6.32.12", sha256="2e41968aeb0406ee31c30af9c046143099b251846e0839cb04f4e960c7893e19")
    version("6.32.10", sha256="5a896804ec153685e8561adaa4e546b708139c484280aa6713a0a178f5b7f98b")

    # [metacling] Add missing lock to TCling::Evaluate
    patch(
        "https://github.com/root-project/root/pull/18943.patch?full_index=1",
        sha256="8e822a875124f09c903d53766d5197c4f152463d223a47139d8e4e83b171f25e",
        when="@6.32:6.32.12,6.34:6.34.08,6.36.00",
    )
    # [cling] The LookupHelper routines need the ROOT lock
    patch(
        "https://github.com/root-project/root/pull/18548.patch?full_index=1",
        sha256="deced0c6c7ad8be44757366f8e2b222f0e1a19dc4deed78d07d5a4a672d40d62",
        when="@6.34:6.34.08",
    )
    patch(
        "https://github.com/root-project/root/pull/18830.patch?full_index=1",
        sha256="deced0c6c7ad8be44757366f8e2b222f0e1a19dc4deed78d07d5a4a672d40d62",
        when="@6.32:6.32.12",
    )
    # Apply TFile::k630forwardCompatibility when creating new file if set in rootrc
    patch(
        "https://github.com/root-project/root/pull/17542.patch?full_index=1",
        sha256="0a30cc6f342f38494d62a7aa8bcd7e9de820264aea44c09b1305aae89e61a680",
        when="@6.30:6.32.08,6.34:6.34.02",
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
