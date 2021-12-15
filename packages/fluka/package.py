from spack import *
import os
import tarfile


class Fluka(Package):
    """FLUKA is a general purpose Monte Carlo code for the interaction
    and transport of hadrons, leptons, and photons from keV (with the
    exception of neutrons, tracked down to thermal energies) to cosmic
    ray energies in any material.

    Note: A manual download is required for FLUKA.
       Spack will search your current directory for the download file.
       Alternatively, add this file to a mirror so that Spack can find it.
       For instructions on how to set up a mirror, see
       https://spack.readthedocs.io/en/latest/mirrors.html"""

    homepage = "https://fluka.cern"
    list_url = "https://fluka.cern/download/latest-fluka-release"

    maintainers = ['wdconinc']

    tags = ['eic']

    version('4.2.1',
            sha256='a78a8e9bdb75e4b7eda0c190dc7241b399d1abffcbc3fd6f42505b789f1cdb5f',
            url='file://{}/fluka-4-2.1.x86-Linux-gfor9.tgz'.format(os.getcwd()))
    version('4.2.0',
            sha256='a3b3f9617079aa64d39632b32a01b65dc32375d01804bb80ae1d3e87de599393',
            url='file://{}/fluka-4-2.0.x86-Linux-gfor9.tgz'.format(os.getcwd()))

    conflicts('%gcc@:7', when='@4.2.0')

    manual_download = True

    def install(self, spec, prefix):
        with working_dir('src'):
            make()
        install_tree('bin', prefix.bin)
        install_tree('lib', prefix.lib)
        install_tree('data', prefix.data)
        install_tree('include', prefix.include)
        install_tree('doc', join_path(prefix.share, 'doc'))
        install_tree('examples', join_path(prefix.share, 'examples'))
        for file in ['AUTHORS', 'INSTALL', 'LICENSE', 'REFERENCES',
                     'RELEASE-NOTES', 'README.md', 'Version.tag']:
            install(file, prefix.share)
