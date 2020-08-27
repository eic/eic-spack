# EIC Spack Repository

[![Build Status](https://travis-ci.org/eic/eic-spack.svg?branch=master)](https://travis-ci.org/eic/eic-spack)

This repository contains [Spack](https://spack.readthedocs.io/en/latest/index.html) packages for the EIC.

While we encourage the inclusion of Spack packages in the upstream repository, we realize that some packages may not be mature enough or have too small of a user base to be accepted there.

## Installing Spack

Installing Spack is outside the scope of this repository, but described in the Spack [Getting Started](https://spack.readthedocs.io/en/latest/getting_started.html) page.

## Adding the EIC Spack Repository

1. Clone this repository:
```sh
git clone https://github.com/eic/eic-spack.git
```

2. Add this repository to your Spack configuration:
```sh
spack repo add eic-spack
```

## Installing EIC Spack Packages

1. Find an EIC Spack package:
```sh
spack find eic-smear
```

2. Install an EIC Spack package:
```sh
spack install eic-smear
```
If this is the first package you install, it will also install all dependencies.

## Using EIC Spack Packages

1. Load the EIC Spack package:
```sh
spack load eic-smear
```

2. Unload the EIC Spack package:
```sh
spack unload eic-smear
```

3. Unload all Spack packages:
```sh
spack unload -a
```

## Using EIC Spack Packages in Environments

1. Create and activate a new Spack environment:
```sh
spack env create eic-smear
spack env activate eic-smear
```

2. Install an EIC Spack package:
```sh
spack install eic-smear
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
cd $SPACK_ROOT/var/spack/environments/eic-smear/
spack containerize > Dockerfile
```
