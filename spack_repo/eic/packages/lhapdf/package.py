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

from spack.package import *
from spack_repo.builtin.build_systems import autotools as _autotools
from spack_repo.builtin.packages.lhapdf.package import Lhapdf as _BuiltinLhapdf

from spack_repo.eic.build_systems.hwcaps import HwcapsAutotoolsMixin, add_hwcaps_variant


class Lhapdf(_BuiltinLhapdf):
    __doc__ = _BuiltinLhapdf.__doc__

    add_hwcaps_variant()

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


class AutotoolsBuilder(HwcapsAutotoolsMixin, _autotools.AutotoolsBuilder):
    """AutotoolsBuilder for lhapdf with optional glibc hwcaps multi-build."""
