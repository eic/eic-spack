from spack_repo.builtin.packages.podio.package import Podio as BuiltinPodio

from spack.package import *


class Podio(BuiltinPodio):
    __doc__ = BuiltinPodio.__doc__

    depends_on("py-graphviz", type=("run", "test"))

    patch(
        "https://github.com/AIDASoft/podio/pull/1071.patch?full_index=1",
        sha256="9447f23170e0689d27892dac0c95198426f92cfce44e816cdf1167216b292016",
        when="@1.9",
    )
    patch(
        "https://github.com/AIDASoft/podio/pull/423.patch?full_index=1",
        sha256="a88278b99a579fa1e8b8027f5ce8baad85d5870f648620d19dd40cf35880aa9d",
        when="@0.16.4:0.16.5",
    )
    patch(
        "https://github.com/AIDASoft/podio/commit/9f9c5fc8d40bc3e037b0846d5133d9a0e4d15c36.patch?full_index=1",
        sha256="36b2f363c06103af276d490e7292a8688d0879f04995d28c46c37c3d6dd35bc4",
        when="@0.16.4:0.16.5",
    )
    patch(
        "https://github.com/AIDASoft/podio/pull/452.patch?full_index=1",
        sha256="47692dd40c30a76a565a20750e494b34d57fbd96bbae2d867cccbbbd9ff09636",
        when="@0.16.4:0.16.5",
    )

    # The pyunittest test of the build-time test suite fails on macOS, see
    # https://github.com/eic/eic-spack/issues/1097. Skip it through CTestCustom.cmake
    # before the builtin build_test callback runs `ninja test` / `make test`.
    @run_after("install", when="platform=darwin")
    def skip_pyunittest(self):
        if not self.run_tests:
            return
        with working_dir(self.build_directory):
            with open("CTestCustom.cmake", "a") as f:
                f.write("set(CTEST_CUSTOM_TESTS_IGNORE ${CTEST_CUSTOM_TESTS_IGNORE} pyunittest)\n")

    def test_podio_dump_help(self):
        """check that podio-dump parses its command line options"""
        podio_dump = which("podio-dump", path=self.prefix.bin, required=True)
        out = podio_dump("--help", output=str, error=str)
        assert "Dump contents of a podio file" in out

    def test_podio_vis_help(self):
        """check that podio-vis parses its command line options"""
        if not self.spec.satisfies("@0.17:"):
            raise SkipTest("podio-vis was introduced in podio 0.17")
        podio_vis = which("podio-vis", path=self.prefix.bin, required=True)
        out = podio_vis("--help", output=str, error=str)
        assert "Given a description yaml file" in out
