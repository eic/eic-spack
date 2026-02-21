from spack.package import *

try:
    from spack_repo.builtin.packages.py_tensorflow.package import PyTensorflow as BuiltinPyTensorflow
except ImportError:
    from spack.pkg.builtin.py_tensorflow import PyTensorflow as BuiltinPyTensorflow

class PyTensorflow(BuiltinPyTensorflow):
    patch(
        "https://github.com/tensorflow/tensorflow/pull/90579.diff?full_index=1",
        sha256="f623d5d833ba0185c9b6ef4a98b90069a73bea84e45381995a3db8150280c896",
        when="@2.15:2.19",
    )