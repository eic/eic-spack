#!/bin/bash

dir=`dirname ${0}`
dir=`realpath ${dir}`

mkdir -p ${dir}/mirror

os=$1
shift

for spec in $@ ; do
  docker run --rm \
             -v ${dir}/mirror:/spack/mirror \
             -it electronioncollider/spack-builder:${os} \
    bash -c " \
      spack install ${spec} && \
      spack buildcache create --rebuild-index -m local -a ${spec} \
    "
done
