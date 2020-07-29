FROM centos:7

# Install build essentials
RUN yum install -q -y file git make automake cmake gcc gcc-c++ gcc-gfortran unzip patch python3 bzip2 rsync

# Install spack
ENV SPACK_VERSION v0.15
RUN git clone --branch releases/${SPACK_VERSION} https://github.com/spack/spack.git /spack \
 && chmod a+w /spack/var/spack

# Work in /spack
WORKDIR /spack

# Switch to using bash instead of sh
SHELL ["/bin/bash", "-c"]

# Print arch
RUN source /spack/share/spack/setup-env.sh \
 && spack arch
# Find compilers
RUN source /spack/share/spack/setup-env.sh \
 && spack compiler find --scope defaults \
 && cat /spack/etc/spack/defaults/compilers.yaml
# Add GPG key
RUN source /spack/share/spack/setup-env.sh \
 && spack gpg init \
 && spack gpg create 'EIC Spack Build System' 'eic-spack@github.com' \
 && spack gpg list

# Install packages as x86_64 in /cvmfs (fixed rpaths, allows buildcache create -a)
RUN sed -i 's|install_tree: .*|install_tree: /cvmfs/eic.opensciencegrid.org/packages|' /spack/etc/spack/defaults/config.yaml
RUN sed -i 's|install_path_scheme: .*|install_path_scheme: "\${PACKAGE}/\${VERSION}/\${ARCHITECTURE}-\${COMPILERNAME}-\${COMPILERVER}-\${HASH}"|' /spack/etc/spack/defaults/config.yaml
RUN sed -i 's|  all:|  all:\n    target: [x86_64]|' /spack/etc/spack/defaults/packages.yaml

# Install EIC spack
RUN git clone https://github.com/eic/eic-spack.git /spack/var/spack/repos/eic-spack
RUN source /spack/share/spack/setup-env.sh \
 && spack repo add --scope defaults /spack/var/spack/repos/eic-spack

# Setup mirror
RUN mkdir /spack/mirror && chmod a+w /spack/mirror
RUN source /spack/share/spack/setup-env.sh && spack mirror add --scope defaults local file:///spack/mirror

# Setup /cvmfs permissions
RUN chmod -R a+w /cvmfs/eic.opensciencegrid.org/packages

# Tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

# Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/tini", "--", "/entrypoint.sh"] 
