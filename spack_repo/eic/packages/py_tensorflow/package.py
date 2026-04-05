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

    # tensorflow/dtensor/mlir/shape_utils.cc uses unqualified cast<mlir::OpResult>,
    # which is ambiguous with Eigen::internal::cast under GCC. Qualify it explicitly.
    @run_before("install")
    def patch_gcc_cast_ambiguity(self):
        if self.spec.satisfies("@2.20: %gcc"):
            filter_file(
                r"return ExtractGlobalOutputShape\(cast<mlir::OpResult>",
                "return ExtractGlobalOutputShape(llvm::cast<mlir::OpResult>",
                "tensorflow/dtensor/mlir/shape_utils.cc",
            )
