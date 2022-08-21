from spack import *
from spack.pkg.builtin.acts import Acts as BuiltinActs


class Acts(BuiltinActs):
    version("20.0.0", commit="3740e6cdbfb1f75d8e481686acdfa5b16d3c41a3", submodules=True)
    version("19.7.0", commit="03cf7a3ae74b632b3f89416dc27cc993c9ae4628", submodules=True)
    version("19.6.0", commit="333082914e6a51b381abc1cf52856829e3eb7890", submodules=True)
    version("19.5.0", commit="bf9f0270eadd8e78d283557b7c9070b80dece4a7", submodules=True)
    version("19.4.0", commit="498af243755219486c26d32fb125b7ebf2557166", submodules=True)
    version("19.3.0", commit="747053f60254c5ad3aa1fe7b18ae89c19029f4a6", submodules=True)
    version("19.2.0", commit="adf079e0f7e278837093bf53988da73730804e22", submodules=True)
    version("19.1.0", commit="82f42a2cc80d4259db251275c09b84ee97a7bd22", submodules=True)

    depends_on("dd4hep @1.21: +dddetectors +ddrec", when="@20: +dd4hep")
