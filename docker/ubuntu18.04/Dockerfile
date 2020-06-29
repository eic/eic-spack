FROM ubuntu:18.04 AS eic-spack-builder-ubuntu18.04-base

# Install build essentials
RUN apt-get update -q \
 && apt-get install -q -y \
        curl \
        build-essential \
        gfortran \
        git \
        gnupg2 \
        python-dev \
 && apt-get clean -q -y

# Install spack
RUN git clone https://github.com/spack/spack.git /spack

# Work in /spack
WORKDIR /spack

# Switch to using bash instead of sh
SHELL ["/bin/bash", "-c"]

# Print arch
RUN source /spack/share/spack/setup-env.sh && spack arch
# Find compilers
RUN source /spack/share/spack/setup-env.sh && spack compiler find && cat /root/.spack/compilers.yaml
# Find externals
RUN source /spack/share/spack/setup-env.sh && spack external find && cat /root/.spack/packages.yaml

# Setup mirror
RUN source /spack/share/spack/setup-env.sh && spack mirror add local file:///spack/mirror
RUN source /spack/share/spack/setup-env.sh && spack buildcache list && spack mirror list


FROM eic-spack-builder-ubuntu18.04-base AS eic-spack-builder-ubuntu18.04

# Switch to using bash instead of sh
SHELL ["/bin/bash", "-c"]

# Install compilers
COPY install-compilers.txt .
RUN source /spack/share/spack/setup-env.sh \
 && cat install-compilers.txt | \
    while read package ; do \
      spack install ${package} target=x86_64 ; \
    done
# Find compilers
RUN source /spack/share/spack/setup-env.sh \
 && spack compiler find \
 && cat /root/.spack/compilers.yaml

# Install dependencies
COPY install-deps.txt .
RUN source /spack/share/spack/setup-env.sh \
 && cat install-deps.txt | \
    while read package ; do \
      spack install --only dependencies ${package} target=x86_64 ; \
    done

# Install packages
COPY install-full.txt .
RUN source /spack/share/spack/setup-env.sh \
 && cat install-full.txt | \
    while read package ; do \
      spack install ${package} target=x86_64 ; \
    done
