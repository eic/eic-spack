#!/usr/bin/env spack-python
"""Verify version checksums for packages changed between two git refs.

This script replicates the functionality of ``spack ci verify-versions`` but
operates on the ``eic`` package repository instead of the built-in spack repo.
The built-in command hard-codes ``spack.repo.builtin_repo()`` for the git
diff, which causes it to run ``git ls-tree`` inside the spack-packages
checkout rather than the eic-spack checkout – making it fail whenever the
supplied commit SHAs are only present in the eic-spack repository.
"""
import os
import sys

import spack.ci as spack_ci
import spack.cmd.ci as ci_cmd
import spack.llnl.util.filesystem as fs
import spack.llnl.util.tty as tty
import spack.repo
import spack.spec


def main():
    if len(sys.argv) != 3:
        tty.die(f"Usage: {sys.argv[0]} <from_ref> <to_ref>")

    from_ref = sys.argv[1]
    to_ref = sys.argv[2]

    # Obtain the eic package repository so that git operations run inside the
    # eic-spack checkout (where the supplied commit SHAs are valid).
    try:
        eic_repo = spack.repo.PATH.get_repo("eic")
    except Exception:
        tty.die("Could not find the 'eic' repository. Make sure it has been added with 'spack repo add'.")

    # Discover packages that were changed or added between the two refs.
    pkgs = spack.repo.get_all_package_diffs("AC", eic_repo, from_ref, to_ref)

    if not pkgs:
        tty.msg(f"No packages changed between {from_ref[:12]} and {to_ref[:12]}")
        return

    success = True
    for pkg_name in pkgs:
        spec = spack.spec.Spec(pkg_name)
        pkg = eic_repo.get_pkg_class(spec.name)(spec)
        path = eic_repo.package_path(pkg_name)

        # Trust maintainers of packages that require manual download.
        if pkg.manual_download:
            tty.warn(f"Skipping manual-download package: {pkg_name}")
            continue

        url_version_to_checksum = {}
        git_version_to_checksum = {}
        for version in pkg.versions:
            vdata = pkg.versions[version]
            if "sha256" in vdata:
                url_version_to_checksum[version] = vdata["sha256"]
            elif "commit" in vdata:
                git_version_to_checksum[version] = vdata["commit"]

        def filter_added_versions(versions):
            added = spack_ci.filter_added_checksums(
                versions.values(), path, from_ref=from_ref, to_ref=to_ref
            )
            return [v for v, c in versions.items() if c in added]

        # Run git diff from the package directory so that filter_added_checksums
        # operates inside the eic-spack repository.
        with fs.working_dir(os.path.dirname(path)):
            new_url_versions = filter_added_versions(url_version_to_checksum)
            new_git_versions = filter_added_versions(git_version_to_checksum)

        if new_url_versions:
            success &= ci_cmd.validate_standard_versions(pkg, new_url_versions)

        if new_git_versions:
            success &= ci_cmd.validate_git_versions(pkg, new_git_versions)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
