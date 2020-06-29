#!/bin/bash

dir=`dirname ${0}`/..
dir=`realpath ${dir}`
if [ -z "`spack repo list | grep ${dir}`" ] ; then
  echo "Directory ${dir} is not listed as spack repo:"
  spack repo list
  echo "Assuming repository at ${dir} is part of spack."
fi

for package in ${dir}/packages/*/package.py ; do
  package=`dirname ${package}`
  package=`basename ${package}`
  echo "Installing ${package}..."
  spack install ${package} $@
done
