from spack.package import *
from spack.pkg.builtin.gaudi import Gaudi as BuiltinGaudi


class Gaudi(BuiltinGaudi):
    patch(
        "https://gitlab.cern.ch/gaudi/Gaudi/-/commit/03db151003d5207795ae8ec96aaf2f5f8a9ea008.diff",
        sha256="e73f45f10ea4a143a05c53a468233ceaad1a8ec22dee9877d178a3c9ee46c70f",
        when="@:36.5",
    )
