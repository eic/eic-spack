# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""Shared infrastructure for glibc hwcaps multi-arch shared library builds.

This module provides:

* Pure utility functions (``add_hwcaps_variant``, ``install_hwcaps_variants``,
  ``copy_so_files``, ``copy_so_files_recursive``, …) used by overlay packages.

* **Builder mixins** that package Builder classes can inherit to gain hwcaps
  support with minimal boilerplate:

  - :class:`HwcapsMixin` — base mixin; adds the ``@run_after("install")`` hook
    and declares an abstract :meth:`build_for_hwcaps` that subclasses must
    implement.

  - :class:`HwcapsCMakeMixin` — default CMake implementation: prepends the
    hwcaps ``-march=`` flag to ``SPACK_CXXFLAGS`` / ``SPACK_CFLAGS`` so the
    Spack compiler wrappers inject it transparently, then runs ``make -B``
    (no cmake re-configure needed for a pure -march change), and copies all
    rebuilt ``lib*.so*`` files recursively.  Override :meth:`build_for_hwcaps`
    when the package needs a cmake re-configure (e.g. VecGeom's
    ``VECGEOM_VECTOR``).

  - :class:`HwcapsAutotoolsMixin` — default Autotools implementation: passes
    ``CXXFLAGS`` and ``CFLAGS`` overrides on the make command line (highest
    priority for GNU make) and copies rebuilt libraries recursively.

Typical usage in a CMake overlay::

    from spack_repo.eic.build_systems.hwcaps import HwcapsCMakeMixin, add_hwcaps_variant
    from spack_repo.builtin.build_systems import cmake as _cmake
    from spack_repo.builtin.packages.mypkg.package import MyPkg as _BuiltinMyPkg
    from spack.package import *

    class MyPkg(_BuiltinMyPkg):
        add_hwcaps_variant()

    class CMakeBuilder(HwcapsCMakeMixin, _cmake.CMakeBuilder):
        pass  # default build_for_hwcaps handles the rebuild + copy

Background
----------
glibc's dynamic linker transparently prefers libraries in
``<prefix>/lib/glibc-hwcaps/<level>/`` over those in ``<prefix>/lib/`` when
running on a CPU that satisfies *level*.  Installing a baseline-optimised
library in ``lib/`` and a higher-level rebuild in
``lib/glibc-hwcaps/x86-64-v3/`` therefore gives zero-overhead CPU dispatch
with no changes to consumer binaries.

The glibc hwcaps subdirectory names (``x86-64-v2``, ``x86-64-v3``, …) are
defined by glibc itself and happen to coincide with the GCC ``-march=`` flag
names for the generic x86-64 baseline levels.  This module derives the
mapping automatically from the vendored archspec CPU database: for each
generic target whose modern-GCC ``-march`` name matches the pattern
``^x86-64-v[2-9]$``, the target name and march name are recorded.  New
x86_64_v* levels added to archspec are therefore picked up without any code
change here.

Compiler wrapper injection
--------------------------
Spack's compiler wrappers (``spack_cc``, ``spack_cxx``) read the environment
variables ``SPACK_CFLAGS`` and ``SPACK_CXXFLAGS`` and prepend their contents
to every compilation command.  During ``@run_after("install")`` the wrappers
are still active, so temporarily setting these variables before calling
``make -B`` injects the hwcaps ``-march=`` flag without touching the build
system's own flag configuration (Makefiles, CMake cache).  For CMake this
means we can skip the cmake re-configure entirely for a pure ``-march``
change; the wrappers handle flag injection at compile time.

Upstream path
-------------
This module lives in ``spack_repo/eic/build_systems/`` in the eic-spack
overlay.  To upstream to ``spack/spack-packages``, move it to
``spack_repo/builtin/build_systems/hwcaps.py`` and update import paths from
``spack_repo.eic.build_systems.hwcaps`` to
``spack_repo.builtin.build_systems.hwcaps``.  No spack-core changes are
required.
"""

import glob as _glob
import os as _os
import re as _re

import spack.vendor.archspec.cpu as _cpu

from spack.error import InstallError
from spack.llnl.util.filesystem import install as _install
from spack.package import conflicts as _conflicts
from spack.package import find, join_path, mkdirp, run_after, variant, working_dir
from spack.util.executable import Executable as _Executable

# ---------------------------------------------------------------------------
# Mapping: archspec target name → glibc hwcaps subdirectory name
# ---------------------------------------------------------------------------

_GLIBC_HWCAPS_PATTERN = _re.compile(r"^x86-64-v[2-9]$")


def _build_hwcaps_subdirs():
    result = {}
    for _name, _target in sorted(_cpu.TARGETS.items()):
        if _target.vendor != "generic":
            continue
        _gcc_entries = _target.compilers.get("gcc", [])
        if not _gcc_entries:
            continue
        # First entry has the most-recent (highest minimum) compiler version,
        # i.e. the canonical modern -march name for this target.
        _march_name = _gcc_entries[0].get("name", _name)
        if _GLIBC_HWCAPS_PATTERN.match(_march_name):
            result[_name] = _march_name
    return result


#: Mapping from archspec target name to the glibc hwcaps subdirectory name.
#: Derived at import time from the vendored archspec CPU database.
GLIBC_HWCAPS_SUBDIRS = _build_hwcaps_subdirs()


def valid_hwcaps_values():
    """Return a sorted tuple of valid archspec target names for the hwcaps variant."""
    return tuple(sorted(GLIBC_HWCAPS_SUBDIRS.keys()))


def hwcaps_march(target_name):
    """Return the ``-march=<subdir>`` flag for *target_name*, or an empty string."""
    subdir = GLIBC_HWCAPS_SUBDIRS.get(target_name)
    return f"-march={subdir}" if subdir else ""


_DEFAULT_HWCAPS_DESCRIPTION = (
    "Build additional optimised shared libraries for the listed glibc hwcaps "
    "levels and install them to lib/glibc-hwcaps/<level>/.  The hwcaps level "
    "must be strictly greater than the spec's baseline target in archspec "
    "ordering (enforced at concretize time)."
)


def add_hwcaps_variant(
    description: str = _DEFAULT_HWCAPS_DESCRIPTION, conflicts: str = "", conflicts_msg: str = ""
) -> None:
    """Declare the ``hwcaps`` variant and all archspec-ordering conflicts.

    Call this inside a package class body.  It is equivalent to::

        variant("hwcaps", values=("none",) + valid_hwcaps_values(),
                default="none", multi=True, description=...)
        # plus, for every (hwcaps_val, baseline_val) pair where hwcaps_val
        # is NOT strictly greater than baseline_val in archspec ordering:
        conflicts("hwcaps=<hwcaps_val>", when="target=<baseline_val>", msg=...)

    Because :func:`variant` and :func:`conflicts` are Spack directives that
    queue their work in a global list flushed at class-creation time, calling
    them from a helper function that is itself called during the class body
    works identically to calling them directly in the class body.

    Parameters
    ----------
    description:
        Variant description string.
    conflicts:
        If provided, add ``conflicts(<conflicts>, when="hwcaps=<val>", ...)``
        for every hwcaps value.  Useful for packages that only support hwcaps
        together with a specific other variant setting, e.g.
        ``conflicts="libs=static"``.
    conflicts_msg:
        Optional custom message for the extra conflicts entries.  Defaults to
        ``"hwcaps conflicts with <conflicts>"``.
    """
    hwcaps_vals = valid_hwcaps_values()

    variant(
        "hwcaps",
        values=("none",) + hwcaps_vals,
        default="none",
        multi=True,
        description=description,
    )

    for hwcaps_val in hwcaps_vals:
        t_hwcaps = _cpu.TARGETS[hwcaps_val]
        for baseline_val in hwcaps_vals:
            t_baseline = _cpu.TARGETS[baseline_val]
            if not (t_hwcaps > t_baseline):
                _conflicts(
                    f"hwcaps={hwcaps_val}",
                    when=f"target={baseline_val}",
                    msg=(
                        f"hwcaps={hwcaps_val} requires the baseline target to be "
                        f"strictly below {hwcaps_val} in archspec ordering; "
                        f"target={baseline_val} does not satisfy this"
                    ),
                )

        if conflicts:
            _conflicts(
                conflicts,
                when=f"hwcaps={hwcaps_val}",
                msg=conflicts_msg or f"hwcaps conflicts with {conflicts}",
            )


def copy_so_files(src_dir, hwcaps_dir):
    """Copy ``*.so*`` files (ELFs and SONAME/ldconfig symlinks) into *hwcaps_dir*.

    Symlinks are re-created as symlinks; regular files are copied with spack's
    ``install()`` (which preserves permissions).  Existing destinations are
    silently replaced.
    """
    for src in sorted(_glob.glob(join_path(src_dir, "*.so*"))):
        dst = join_path(hwcaps_dir, _os.path.basename(src))
        if _os.path.islink(src):
            link_target = _os.readlink(src)
            if _os.path.lexists(dst):
                _os.unlink(dst)
            _os.symlink(link_target, dst)
        else:
            if _os.path.lexists(dst):
                _os.unlink(dst)
            _install(src, dst)


def copy_so_files_recursive(src_root, hwcaps_dir):
    """Recursively search *src_root* for ``lib*.so*`` files and copy them into *hwcaps_dir*.

    Useful for CMake packages that scatter shared libraries across multiple
    subdirectories of the build tree (e.g. FastJet, VecGeom).  Only
    ``lib*.so*`` files are matched to avoid picking up Python extension modules
    or other unrelated shared objects.  Symlinks are re-created as symlinks;
    regular files are copied with ``install()``.  Existing destinations are
    silently replaced.
    """
    for src in sorted(find(src_root, "lib*.so*")):
        dst = join_path(hwcaps_dir, _os.path.basename(src))
        if _os.path.islink(src):
            link_target = _os.readlink(src)
            if _os.path.lexists(dst):
                _os.unlink(dst)
            _os.symlink(link_target, dst)
        else:
            if _os.path.lexists(dst):
                _os.unlink(dst)
            _install(src, dst)


def install_hwcaps_variants(builder, build_fn):
    """Iterate over the ``hwcaps`` variant values and call *build_fn* for each.

    Parameters
    ----------
    builder:
        The spack Builder instance (provides ``spec``, ``spec.prefix``, etc.).
    build_fn:
        Callable ``(target_name: str, march_flag: str, hwcaps_dir: str) -> None``
        that performs the package-specific rebuild.  It is responsible for
        placing the rebuilt shared libraries in *hwcaps_dir* (typically by
        calling :func:`copy_so_files` or :func:`copy_so_files_recursive`).
    """
    if "hwcaps" not in builder.spec.variants:
        return
    hwcaps_targets = builder.spec.variants["hwcaps"].value
    if not hwcaps_targets or set(hwcaps_targets) == {"none"}:
        return

    baseline_str = str(builder.spec.architecture.target)
    try:
        t_baseline = _cpu.TARGETS[baseline_str]
    except KeyError:
        raise InstallError(f"hwcaps: unrecognised baseline target {baseline_str!r}")

    for target_name in hwcaps_targets:
        if target_name == "none":
            continue

        subdir = GLIBC_HWCAPS_SUBDIRS.get(target_name)
        if not subdir:
            raise InstallError(
                f"hwcaps: {target_name!r} has no known glibc hwcaps subdirectory; "
                f"valid values: {valid_hwcaps_values()!r}"
            )

        try:
            t_hwcaps = _cpu.TARGETS[target_name]
        except KeyError:
            raise InstallError(f"hwcaps: unrecognised archspec target {target_name!r}")

        if not (t_hwcaps > t_baseline):
            raise InstallError(
                f"hwcaps target {target_name!r} is not strictly greater than "
                f"baseline target {baseline_str!r} in archspec ordering"
            )

        march_flag = hwcaps_march(target_name)
        hwcaps_dir = join_path(builder.spec.prefix, "lib", "glibc-hwcaps", subdir)
        mkdirp(hwcaps_dir)
        build_fn(target_name, march_flag, hwcaps_dir)


# ---------------------------------------------------------------------------
# Builder mixins
# ---------------------------------------------------------------------------


def _set_spack_flags(march_flag):
    """Context helper: prepend *march_flag* to SPACK_CXXFLAGS and SPACK_CFLAGS.

    Returns a dict of the original values (or None if unset) for restoration.
    """
    saved = {}
    for var in ("SPACK_CXXFLAGS", "SPACK_CFLAGS"):
        saved[var] = _os.environ.get(var)
        new_val = f"{march_flag} {saved[var]}".strip() if saved[var] else march_flag
        _os.environ[var] = new_val
    return saved


def _restore_spack_flags(saved):
    """Restore SPACK_CXXFLAGS / SPACK_CFLAGS from a dict returned by :func:`_set_spack_flags`."""
    for var, old_val in saved.items():
        if old_val is not None:
            _os.environ[var] = old_val
        else:
            _os.environ.pop(var, None)


class HwcapsMixin:
    """Base builder mixin: adds ``@run_after("install")`` hwcaps hook.

    Subclasses **must** implement :meth:`build_for_hwcaps`.  Prefer the
    concrete subclasses :class:`HwcapsCMakeMixin` or
    :class:`HwcapsAutotoolsMixin` for standard build systems.
    """

    @run_after("install")
    def _install_hwcaps_variants(self):
        install_hwcaps_variants(self, self.build_for_hwcaps)

    def build_for_hwcaps(self, target_name: str, march_flag: str, hwcaps_dir: str) -> None:
        raise NotImplementedError(
            f"{type(self).__name__} must implement "
            "build_for_hwcaps(target_name, march_flag, hwcaps_dir)"
        )


class HwcapsCMakeMixin(HwcapsMixin):
    """CMake builder mixin with default hwcaps rebuild via compiler wrapper injection.

    Injects the hwcaps ``-march=`` flag through ``SPACK_CXXFLAGS`` /
    ``SPACK_CFLAGS`` so the Spack compiler wrappers forward it to every
    compilation, then runs ``make -B`` (forced full rebuild).  All rebuilt
    ``lib*.so*`` files in the build tree are copied recursively to *hwcaps_dir*.

    If the package class defines a method
    ``hwcaps_cmake_extra_args(target_name: str) -> list[str]``, the returned
    arguments are passed to a cmake re-configure step *before* ``make -B``.
    This allows packages like VecGeom to update CMake cache variables that
    control SIMD selection (e.g. ``-DVECGEOM_VECTOR=avx2``) without needing
    to override :meth:`build_for_hwcaps` entirely.
    """

    def build_for_hwcaps(self, target_name: str, march_flag: str, hwcaps_dir: str) -> None:
        extra_cmake_args = []
        hwcaps_cmake_extra_args = getattr(self.pkg, "hwcaps_cmake_extra_args", None)
        if hwcaps_cmake_extra_args is not None:
            extra_cmake_args = hwcaps_cmake_extra_args(target_name)
        saved = _set_spack_flags(march_flag)
        try:
            with working_dir(self.build_directory):
                if extra_cmake_args:
                    cmake = _Executable("cmake")
                    cmake(*extra_cmake_args, ".")
                make = _Executable("make")
                make("-B")
        finally:
            _restore_spack_flags(saved)
        copy_so_files_recursive(self.build_directory, hwcaps_dir)


class HwcapsAutotoolsMixin(HwcapsMixin):
    """Autotools builder mixin with default hwcaps rebuild via make flag override.

    Passes ``CXXFLAGS`` and ``CFLAGS`` as GNU make command-line variable
    overrides (highest priority, propagated to libtool and sub-makes), then
    runs ``make -B``.  All rebuilt ``lib*.so*`` files in the build tree are
    copied recursively to *hwcaps_dir*.

    Override :meth:`build_for_hwcaps` for packages with non-standard build
    trees or that require additional flags beyond ``-march=``.
    """

    def build_for_hwcaps(self, target_name: str, march_flag: str, hwcaps_dir: str) -> None:
        make = _Executable("make")
        with working_dir(self.build_directory):
            make("-B", f"CXXFLAGS=-O3 {march_flag}", f"CFLAGS=-O3 {march_flag}")
        copy_so_files_recursive(self.build_directory, hwcaps_dir)


class HwcapsMakefileMixin(HwcapsMixin):
    """Makefile builder mixin for packages that use ``CFLAGS`` env-var injection.

    Unlike :class:`HwcapsCMakeMixin`, this mixin overrides the ``CFLAGS``
    environment variable directly (not ``SPACK_CFLAGS``) so that the hwcaps
    ``-march=`` flag appears *after* ``SPACK_TARGET_ARGS`` on the compiler
    command line (GCC uses the last ``-march`` flag, so this overrides the
    baseline).  Useful for packages like lz4 whose Makefiles expand ``CFLAGS``
    from the environment.

    The package class may define:

    ``hwcaps_make_args``:
        Extra arguments appended to ``make -B``, e.g. ``["-C", "lib"]``.
        Default: ``[]``.

    ``hwcaps_lib_subdir``:
        Subdirectory of the build directory where rebuilt ``*.so*`` files land,
        e.g. ``"lib"``.  When non-empty, :func:`copy_so_files` is used on
        that specific directory; otherwise the full build tree is searched
        recursively.  Default: ``""``.
    """

    def build_for_hwcaps(self, target_name: str, march_flag: str, hwcaps_dir: str) -> None:
        pic = self.pkg.compiler.cc_pic_flag
        # Add -O3 because many Makefiles prepend -O3 to USERCFLAGS; repeating
        # it is harmless and ensures it is always present.
        new_cflags = f"{pic} -O3 {march_flag}"
        extra_make_args = list(getattr(self.pkg, "hwcaps_make_args", []))
        lib_subdir = getattr(self.pkg, "hwcaps_lib_subdir", "")

        old_cflags = _os.environ.get("CFLAGS")
        _os.environ["CFLAGS"] = new_cflags
        try:
            with working_dir(self.build_directory):
                make = _Executable("make")
                make("-B", *extra_make_args)
        finally:
            if old_cflags is not None:
                _os.environ["CFLAGS"] = old_cflags
            else:
                _os.environ.pop("CFLAGS", None)

        if lib_subdir:
            copy_so_files(join_path(self.build_directory, lib_subdir), hwcaps_dir)
        else:
            copy_so_files_recursive(self.build_directory, hwcaps_dir)
