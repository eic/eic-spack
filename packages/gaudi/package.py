from spack import *
from spack.pkg.builtin.gaudi import Gaudi as BuiltinGaudi
class Gaudi(BuiltinGaudi):
    version("36.7", sha256="8dca43185ba11e1b33f5535d2e384542d84500407b0d1f8cb920be00f05c9716")
    version("36.6", sha256="8fc7be0ce32f99cc6b0be4ebbb246f4bb5008ffbf0c012cb39c0aff813dce6af")
    patch('https://gitlab.cern.ch/gaudi/Gaudi/-/commit/03db151003d5207795ae8ec96aaf2f5f8a9ea008.diff',
          sha256='e73f45f10ea4a143a05c53a468233ceaad1a8ec22dee9877d178a3c9ee46c70f',
          when='@:36.5')
