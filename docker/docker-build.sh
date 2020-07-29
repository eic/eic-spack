#!/bin/bash

dir=`dirname ${0}`
dir=`realpath ${dir}`

os="centos7"
repo=""
mirror="${dir}/mirror"
while getopts ":r:o:m:" opt; do
  case ${opt} in
    \? ) # process option h
      echo "Usage: `basename $0` [ -o os ] [ -r repo ] [ -m mirror ] spec"
      exit
      ;;
    o )
      os=$OPTARG
      echo "Using OS '${os}'"
      ;;
    r )
      repo=`realpath $OPTARG`
      echo "Using repo '${repo}'"
      ;;
    m )
      mirror=`realpath $OPTARG`
      echo "Using mirror '${mirror}'"
      ;;
    : )
      echo "Invalid Option: -$OPTARG requires an argument" 1>&2
      exit 1
      ;;
  esac
done
shift $((OPTIND -1))

mkdir -p ${mirror}

binds="-v ${mirror}:/spack/mirror"
if [ ! -z "${repo}" ] ; then
  binds="${binds} -v ${repo}:/spack/var/spack/repos/eic-spack"
fi

container="electronioncollider/spack-builder:${os}"

for spec in $@ ; do
  echo "Installing '${spec}'"
  docker run --rm ${binds} -it ${container} \
    bash -c " \
      spack spec -I ${spec} && \
      spack install --no-check-signature ${spec} && \
      spack buildcache create --force --rebuild-index -u -m local -r -a ${spec} \
    "
done
