# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Overlay of the builtin lhapdf package that adds an ``hwcaps`` multi-valued
# variant.  When set, additional optimised shared-library builds are placed in
# ``lib/glibc-hwcaps/<level>/`` inside the install prefix.  Any binary whose
# RPATH already points at the prefix ``lib/`` directory gets automatic
# runtime CPU dispatch through the glibc dynamic-linker hwcaps mechanism —
# no changes to the consumer binary are needed.
#
# LHAPDF uses a GNU Autotools / libtool build.  The shared library is built
# in a ``src/.libs/`` subdirectory within the source tree (in-source build).
# The default HwcapsAutotoolsMixin behaviour (CXXFLAGS/CFLAGS override on the
# make command line + ``make -B`` + recursive copy) is sufficient; the
# recursive copy finds the rebuilt libraries in ``src/.libs/`` automatically.

from spack_repo.builtin.packages.lhapdf.package import Lhapdf as _BuiltinLhapdf
from spack_repo.eic.build_systems.hwcaps import HwcapsAutotoolsMixin, add_hwcaps_variant

from spack.package import *


class Lhapdf(_BuiltinLhapdf, HwcapsAutotoolsMixin):
    __doc__ = _BuiltinLhapdf.__doc__

    add_hwcaps_variant()

    # The hwcaps mixin is on the package class rather than on a custom
    # AutotoolsBuilder: with a builder class in this file, the builder's
    # setup_build_environment replaces the builtin package's, which adds
    # -L<gettext>/lib so that the python wrapper links with -lintl.

    # LHAPDF's installcheck runs example programs that require PDF sets to be
    # installed.  CI environments do not have any PDF sets, so suppress the
    # installcheck to avoid a spurious failure unrelated to our overlay.
    install_time_test_callbacks: list = []

    test_requires_compiler = True

    def test_lhapdf_config(self):
        """check the version reported by lhapdf-config"""
        lhapdf_config = which("lhapdf-config", path=self.prefix.bin, required=True)
        out = lhapdf_config("--version", output=str)
        assert out.strip() == str(self.spec.version), f"unexpected version: {out}"

    def test_version(self):
        """compile and run a program that calls LHAPDF::version()"""
        lhapdf_config = which("lhapdf-config", path=self.prefix.bin, required=True)
        flags = lhapdf_config("--cflags", "--libs", output=str).split()
        cxx = Executable(self.spec["cxx"].package.cxx)
        src = join_path(self.test_suite.current_test_data_dir, "test_lhapdf.cpp")
        cxx("-std=c++17", src, "-o", "test_lhapdf", *flags, f"-Wl,-rpath,{self.prefix.lib}")
        out = Executable("./test_lhapdf")(output=str)
        assert f"LHAPDF version: {self.spec.version}" in out, out

    def test_python(self):
        """import the lhapdf python module and check its version"""
        if not self.spec.satisfies("+python"):
            raise SkipTest("Package must be installed with +python")
        python = self.spec["python"].command
        out = python("-c", "import lhapdf; print(lhapdf.version())", output=str)
        assert out.strip() == str(self.spec.version), f"unexpected version: {out}"

    def patch(self):
        patch_fn = getattr(super(), "patch", None)
        if patch_fn is not None:
            patch_fn()
        # On systems where gettext does not install a standalone libintl.so
        # (e.g. Ubuntu 24.04, where glibc provides intl symbols natively),
        # Python's sysconfig.get_config_var("LIBS") still carries "-lintl".
        # That flag is appended verbatim to the compiler command in
        # wrappers/python/build.py.in, causing the link to fail with
        # "cannot find -lintl".  Strip -lintl from the sysconfig LIBS
        # substitution in build.py.in when no standalone libintl.so is present.
        if self.spec.satisfies("+python") and self.spec.satisfies("^gettext"):
            if "intl" not in self.spec["gettext"].libs.names:
                replacement = (
                    'pyargs += " " + '
                    '(sysconfig.get_config_var("LIBS") or "").replace("-lintl", "")'
                )
                filter_file(
                    r'pyargs \+= " " \+ sysconfig\.get_config_var\("LIBS"\)',
                    replacement,
                    "wrappers/python/build.py.in",
                )
