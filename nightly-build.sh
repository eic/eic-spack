#!/bin/bash

# Test matrix
os="centos7"

# Determine calling directory
dir=`dirname $0`
dir=`realpath $dir`
echo "Using directory $dir for testing..."

# Fetch updates but do not apply to working copy
git fetch --all
branch=`git rev-parse --abbrev-ref HEAD`
packages=`git diff --name-only $branch origin/$branch | sed -n 's|packages/\([a-z0-9-]*\)/package.py|\1|p' | xargs`
git pull

# Mark updated packages dirty
echo "Updated packages: ${packages}"
for package in ${packages} ; do
  if [ -d ${dir}/packages/${package}/.success ] ; then
    rm -rf ${dir}/packages/${package}/.success/*
  fi
done

# Test dirty packages
for packagedir in ${dir}/packages/* ; do
  package=`basename ${packagedir}`
  versions=`sed -n 's|\s*version('\''\(.*\)'\'',.*$|\1|p' ${packagedir}/package.py | xargs`
  echo "Checking ${package} @ ${versions}..."
  for version in ${versions} ; do
    if [ ! -f ${package}/.success/ ] ; then
      export TINI_SUBREAPER=""
      ${dir}/docker/singularity-build.sh -r ${dir} ${package}@${version} \
          && mkdir -p ${package}/.success \
          && touch ${package}/.success/${version}
    fi
  done
done
