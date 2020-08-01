#!/bin/bash

dir=`dirname ${0}`
dir=`realpath ${dir}`

os="centos7"
repo=""
mirror="${dir}/mirror"
cc="gcc"
while getopts ":c:r:o:m:" opt; do
  case ${opt} in
    \? ) # process option h
      echo "Usage: `basename $0` [ -o os ] [ -r repo ] [ -m mirror ] spec"
      exit
      ;;
    c )
      cc=$OPTARG
      echo "Using cc '${cc}'"
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

binds="-B ${mirror}:/spack/mirror"
if [ ! -z "${repo}" ] ; then
  binds="${binds} -B ${repo}:/spack/var/spack/repos/eic-spack"
fi

container="docker://electronioncollider/spack-builder:${os}"

spec=$@
echo "Installing '${spec}'"
if [ ! -f ${os}.img ] ; then
  dd if=/dev/zero of=${os}.img bs=1M count=8000
  mkfs.ext3 ${os}.img
fi
export TINI_SUBREAPER=""
singularity run --overlay ${os}.img --no-home ${binds} ${container} \
  bash -c " \
    spack install ${cc} && \
    spack buildcache create --force --rebuild-index -u -m local -r -a ${cc} && \
    spack load ${cc} && \
    spack compiler find && \
    spack spec -I ${spec} && \
    spack install --no-check-signature ${spec} && \
    spack buildcache create --force --rebuild-index -u -m local -r -a ${spec} \
  "
