#!/bin/bash

# Setup script error handling see https://disconnected.systems/blog/another-bash-strict-mode for details
set -uo pipefail
trap 's=$?; echo "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR
IFS=$'\n\t'

# Go to directory
dir=`dirname $0`/../..
dir=`realpath ${dir}`
cd ${dir}

# Create log file
log=`basename $0 .sh`
tag=`date +%Y-%m-%d-%H%M`
mkdir -p log
log=log/${log}-${tag}.log

# Update repository
git pull   | tee -a ${log}
git status | tee -a ${log}

# Concretize all environments
for env in environments/* ; do

  env=`basename ${env}`

  # Concretize existing environment (allow failure when container exists)
  spack env create ${env} environments/${env}/spack.yaml || true
  spack env activate ${env}
  spack concretize -f
  spack install
  spack find -c -l
  for hash in `spack find -l --no-groups | grep \@ | gawk '{print$1}'` ; do
    spack buildcache create --rebuild-index -u -m jlab-public -r -a /${hash}
  done | tee -a ${log}
  spack env deactivate
  spack env remove -y ${env}

done | tee -a ${log}
