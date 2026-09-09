# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.elfutils.package import Elfutils as BuiltinElfutils

from spack.package import *

class Elfutils(BuiltinElfutils):
    __doc__ = BuiltinElfutils.__doc__

    # Allow debuginfod_find_source() to accept "./"-relative filenames, as
    # produced when Spack's compiler-wrapper -ffile-prefix-map targets a
    # relative ./build root rather than an absolute one. Upstream requires
    # filename[0] == '/'; without this, gdb's debuginfod client rejects
    # any "./"-prefixed DW_AT_name with EINVAL before contacting the
    # server at all. See debuginfod/debuginfod-client.c,
    # debuginfod_query_server_by_buildid().
    patch("elfutils-debuginfod-relative-source.patch", when="@0.181:+debuginfod")