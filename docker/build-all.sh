#!/bin/bash

dir=`dirname ${0}`
dir=`realpath ${dir}`

for os in `find ${dir} -mindepth 1 -type d` ; do
  docker build -f ${os}/Dockerfile .
done
