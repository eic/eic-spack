#!/bin/bash

dir=`dirname ${0}`/..
dir=`realpath ${dir}`
echo "Assuming repository at ${dir} is part of spack."

for package in ${dir}/packages/*/package.py ; do
  package=`dirname ${package}`
  package=`basename ${package}`
  echo "Installing ${package}..."
  spack install ${package} $@
done
