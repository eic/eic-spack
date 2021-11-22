#!/bin/bash

package_list=$(spack tags eic)

# prune duplicates (needed if package list is appended to)
#package_list=$(echo ${package_list} | tr ' ' '\n' | sort | uniq | tr '\n' ' ' | sed -e 's/[[:space:]]*$//')

for p in ${package_list}; do
  v=$(spack versions --new $p)
  # ignore pre and rc versions (for all packages)
  v=$(echo $v | sed 's/\S*\(rc\|pre\|alpha\)\S*//g')
  # using `echo $v` instead of "$v" will handle v=" " correctly
  if [[ ! -z `echo $v` ]]; then
    echo "- [ ] \`$p\`: \`$v\` " >> gh-new-version.log
  fi
done
