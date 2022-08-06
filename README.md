# EIC Spack Repository

[![Build Environments](https://github.com/eic/eic-spack/workflows/Build%20Environments/badge.svg)](https://github.com/eic/eic-spack/actions?query=workflow%3A%22Build+Environments%22)
[![Build Docker Images](https://github.com/eic/eic-spack-docker/workflows/Build%20Docker%20Images/badge.svg)](https://github.com/eic/eic-spack-docker/actions?query=workflow%3A%22Build+Docker+Images%22)
[![EIC CI against CVMFS Software Stack](https://github.com/eic/eic-spack-cvmfs-tests/workflows/EIC%20CI%20against%20CVMFS%20Software%20Stack/badge.svg)](https://github.com/eic/eic-spack-cvmfs-tests/actions?query=workflow%3A%22EIC+CI+against+CVMFS+Software+Stack%22)

This repository contains [Spack](https://spack.readthedocs.io/en/latest/index.html) packages for the EIC.

While we encourage the inclusion of Spack packages in the upstream repository, we realize that some packages may not be mature enough or have too small of a user base to be accepted there.

## Installing Spack

Installing Spack is outside the scope of this repository, but described in the Spack [Getting Started](https://spack.readthedocs.io/en/latest/getting_started.html) page.

The default `develop` branch of this package repository depends on builtin packages in the upstream Spack `develop` repository. For specific vesions of Spack (e.g. v0.18.1), please use the corresponding branch (e.g. v0.18) or the latest tag on that branch (e.g. v0.18.5).

## Adding the EIC Spack Repository

1. Clone this repository:
```sh
git clone https://github.com/eic/eic-spack.git
```

2. Add this repository to your Spack configuration:
```sh
spack repo add epic-eic
```

## Installing EIC Spack Packages

1. Find an EIC Spack package:
```sh
spack find epic-eic
```

2. Install an EIC Spack package:
```sh
spack install epic-eic
```
If this is the first package you install, it will also install all dependencies.

## Using EIC Spack Packages

1. Load the EIC Spack package:
```sh
spack load epic-eic
```

2. Unload the EIC Spack package:
```sh
spack unload epic-eic
```

3. Unload all Spack packages:
```sh
spack unload -a
```

## Using EIC Spack Packages in Environments

1. Create and activate a new Spack environment:
```sh
spack env create epic-eic-env
spack env activate epic-eic-env
```

2. Install an EIC Spack package:
```sh
spack install epic-eic
```
If you already installed this package earlier, this will go very quick.

3. Deactivate the Spack environment:
```sh
spack env deactivate
```
You can verify with `which root` inside and outside the environment that you did indeed use a different installation base.

## Containerizing a Spack Environment

Once you have a Spack environment setup, you can easily turn it into a Docker container recipe from any directory with an environment spack.yaml file:
```sh
cd $SPACK_ROOT/var/spack/environments/epic-eic-env/
spack containerize > Dockerfile
```
