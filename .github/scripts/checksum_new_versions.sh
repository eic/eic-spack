#!/bin/bash
set -Eeuo pipefail
trap 's=$?; echo "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR
IFS=$'\n\t'

package_list=$(spack tags eic | sed 's/^[[:space:]]*//')

# prune duplicates (needed if package list is appended to)
#package_list=$(echo ${package_list} | tr ' ' '\n' | sort | uniq | tr '\n' ' ' | sed -e 's/[[:space:]]*$//')

for p in ${package_list}; do
  if [[ $p == "fluka" ]] ; then
    # skip all fluka versions due to licensing
    continue
  fi
  if [[ $p == "irt" ]] ; then
    # skip all newer irt since now packaged as irt2
    continue
  fi

  # Read one version per array element; drop pre/rc/alpha/beta
  mapfile -t versions < <((spack versions --new $p || true) \
    | grep -Ev '(rc|pre|alpha|beta)' \
    || true)

  if [[ ${#versions[@]} -gt 0 ]]; then
    spack checksum --add-to-package --batch $p "${versions[@]}"
  fi
done
