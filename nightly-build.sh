#!/bin/bash

# Test matrix
oslist="centos7"
cclist="gcc@9.2.0 gcc@9.3.0"

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
  if [ -d ${dir}/packages/${package}/.nightly ] ; then
    rm -rf ${dir}/packages/${package}/.nightly/*
  fi
done

# Test dirty packages
for packagedir in ${dir}/packages/* ; do

  # Skip non-package directories (left over package.pyc from branches)
  if [ ! -f ${packagedir}/package.py ] ; then continue ; fi

  # Determine package name and versions
  package=`basename ${packagedir}`
  versions=`sed -n 's|\s*version('\''\(.*\)'\'',.*$|\1|p' ${packagedir}/package.py | xargs`

  # Loop over all packages and versions
  echo "Checking ${package} @ ${versions}..."
  for version in ${versions} ; do
    for os in ${oslist} ; do
      for cc in ${cclist} ; do

    tag="${os}-${cc}-${package}-${version}"
    log="${packagedir}/.nightly/${tag}.log"
    success="${packagedir}/.nightly/${tag}.success"
    mkdir -p ${packagedir}/.nightly
    if [ ! -f ${success} ] ; then
      ${dir}/docker/singularity-build.sh -o ${os} -r ${dir} -c ${cc} ${package}@${version}%${cc} \
        2>&1 | tee ${log} && touch ${success}

      # Pause for keyboard interrupt
      sleep 1
    fi

      done
    done
  done
done
