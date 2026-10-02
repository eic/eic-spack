#!/usr/bin/env spack-python
"""Generate JSON data files for the GitHub Pages site.

Usage: generate_site_data.py <output_dir> [<environments_dir>]

Writes ``packages.json`` and ``environments.json`` into <output_dir>, describing
the packages of the ``eic`` Spack repository and the environments in the
repository's ``environments/`` directory.
"""
import datetime
import json
import os
import subprocess
import sys

import spack.repo
import spack.spec
import spack.util.spack_yaml as syaml


def first_line(doc):
    for line in (doc or "").strip().splitlines():
        if line.strip():
            return line.strip()
    return ""


def package_info(repo, name):
    cls = repo.get_pkg_class(name)
    versions = []
    for v, info in cls.versions.items():
        versions.append({"version": str(v), "deprecated": bool(info.get("deprecated", False))})
    variants = {}
    # cls.variants maps when-spec -> {variant name -> Variant}
    for by_name in cls.variants.values():
        for vname, variant in by_name.items():
            variants.setdefault(vname, {
                "default": str(variant.default),
                "description": variant.description or "",
            })
    deps = sorted({dep.name for by_when in cls.dependencies.values() for dep in by_when.values()}) \
        if isinstance(cls.dependencies, dict) else []
    bases = [b.__name__ for b in cls.__mro__[1:] if getattr(b, "__module__", "").startswith("spack_repo.builtin")]
    return {
        "name": name,
        "description": first_line(cls.__doc__),
        "homepage": getattr(cls, "homepage", None),
        "git": getattr(cls, "git", None),
        "maintainers": sorted(getattr(cls, "maintainers", []) or []),
        "tags": sorted(getattr(cls, "tags", []) or []),
        "versions": sorted(versions, key=lambda x: x["version"], reverse=True),
        "variants": variants,
        "dependencies": deps,
        "builtin_base": bases[0] if bases else None,
    }


def load_environments(env_dir):
    envs = []
    if not os.path.isdir(env_dir):
        return envs
    for name in sorted(os.listdir(env_dir)):
        path = os.path.join(env_dir, name, "spack.yaml")
        if not os.path.isfile(path):
            continue
        with open(path) as f:
            data = syaml.load(f)
        spack_cfg = data.get("spack", {})
        envs.append({
            "name": name,
            "specs": [str(s) for s in spack_cfg.get("specs", [])],
            "packages": json.loads(json.dumps(spack_cfg.get("packages", {}))),
        })
    return envs


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(f"Usage: {sys.argv[0]} <output_dir> [<environments_dir>]")
    out_dir = sys.argv[1]
    env_dir = sys.argv[2] if len(sys.argv) == 3 else "environments"
    os.makedirs(out_dir, exist_ok=True)

    repo = spack.repo.PATH.get_repo("eic")
    meta = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "commit": os.environ.get("GITHUB_SHA") or subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip(),
    }
    packages = []
    for name in sorted(repo.all_package_names()):
        try:
            packages.append(package_info(repo, name))
        except Exception as e:  # keep the site buildable if one package fails to load
            print(f"warning: could not load {name}: {e}", file=sys.stderr)
    with open(os.path.join(out_dir, "packages.json"), "w") as f:
        json.dump({**meta, "packages": packages}, f, indent=1)
    with open(os.path.join(out_dir, "environments.json"), "w") as f:
        json.dump({**meta, "environments": load_environments(env_dir)}, f, indent=1)
    print(f"Wrote {len(packages)} packages")


if __name__ == "__main__":
    main()
