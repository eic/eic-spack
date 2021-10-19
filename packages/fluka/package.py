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
    url      = "https://flukafiles.web.cern.ch/flukafiles/fluka-4-1.1/fluka-4-1.1.Linux-gfor9.tgz"
    list_url = "https://fluka.cern/download/latest-fluka-release"

    maintainers = ['wdconinc']

    tags = ['eic']

    version('4.1.1',
            sha256='68cc4b81c04fe2d37f4e7ebeb0f8dfd452e1d8558cae8a611a9e1d7a93613f71',
            url='file://{0}/fluka-4-1.1.Linux-gfor9.tgz'.format(os.getcwd()))

    conflicts('%gcc@:7', when='@4.1.1')

    gfor_ver = {
        '4.1.1': '9',
    }

    manual_download = True

    def url_for_version(self, version):
        url = "https://flukafiles.web.cern.ch/flukafiles/fluka-{0}-{1}.fluka-{0}-{1}.Linux-gfor{2}.tgz"
        return url.format(version[0], version[1:], gfor_ver[version])

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
