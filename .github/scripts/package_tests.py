#!/usr/bin/env spack-python
"""Helpers for the build-packages CI job.

Usage:
    package_tests.py supported <package>
        Print "true" if <package> can be built on the host platform, "false" if
        it declares an unconditional ``conflicts("platform=<host>")``.

    package_tests.py check <package>
        Verify that <package> has stand-alone tests that exercise it: the
        package class must define at least one ``test_*`` method, and for
        installed Python packages ``import_modules`` must not be empty (an
        empty list makes ``test_imports`` pass without importing anything).
        Exits non-zero, with GitHub Actions error annotations, otherwise.
"""
import sys

import spack.install_test
import spack.platforms
import spack.repo
import spack.spec
import spack.store


def supported(name):
    cls = spack.repo.PATH.get_pkg_class(name)
    platform = spack.platforms.host().name
    for when, conflicts in cls.conflicts.items():
        if when != spack.spec.Spec():
            continue
        for conflict, msg in conflicts:
            if conflict == spack.spec.Spec(f"platform={platform}"):
                print(f"{name} conflicts with platform={platform}: {msg}", file=sys.stderr)
                print("false")
                return 0
    print("true")
    return 0


def check(name):
    cls = spack.repo.PATH.get_pkg_class(name)
    errors = []

    tests = sorted({fn.__name__ for _, fn in spack.install_test.test_functions(cls)})
    if tests:
        print(f"{name}: stand-alone tests: {', '.join(tests)}")
    else:
        errors.append(f"{name} defines no stand-alone tests (test_* methods)")

    for spec in spack.store.STORE.db.query(name):
        pkg = spec.package
        if "test_imports" in tests and hasattr(pkg, "import_modules"):
            modules = pkg.import_modules
            print(f"{spec.short_spec}: import_modules: {' '.join(modules)}")
            if not modules:
                errors.append(f"{spec.short_spec}: test_imports would not import any module")

    for error in errors:
        print(f"::error::{error}")
    return 1 if errors else 0


if __name__ == "__main__":
    commands = {"supported": supported, "check": check}
    if len(sys.argv) != 3 or sys.argv[1] not in commands:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    sys.exit(commands[sys.argv[1]](sys.argv[2]))
