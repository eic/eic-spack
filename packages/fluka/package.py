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
    url = "https://flukafiles.web.cern.ch/flukafiles/fluka-4-2.3/fluka-4-2.3.x86-Linux-gfor9.tgz"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version(
        "4-3.4",
        sha256="be3197c8162b4e2727dcda88c1b35320b8b01152c3ca9e83c4567bfb8da2b02b",
    )
    version(
        "4-3.3",
        sha256="f22a6e81ac4e149baabac4cf5d5060bf2d5190774f1bd299b6891988fd1e93a1",
    )
    version(
        "4-3.2",
        sha256="9c196cb2dccc07fbe46e0e20e6355621069d3a5eb762927c4e58766d6bce51b7",
    )
    version(
        "4-3.1",
        sha256="e4174e3bcd8eb728cb581028a13e38168ed763bfb57dcf324559991daa906dc5",
    )
    version(
        "4-3.0",
        sha256="d9f7f4ec0764c35a24ed412e48d7017d03966a0e3a6515b0c171539c5cc995f7",
    )
    version(
        "4-2.2",
        sha256="15fe7ad9e45604e1e9f8c3a8c24db2c53181155712c07f7dee3242a890229997",
    )
    version(
        "4-2.1",
        sha256="a78a8e9bdb75e4b7eda0c190dc7241b399d1abffcbc3fd6f42505b789f1cdb5f",
        url="file://{}/fluka-4-2.1.x86-Linux-gfor9.tgz".format(os.getcwd()),
    )
    version(
        "4-2.0",
        sha256="a3b3f9617079aa64d39632b32a01b65dc32375d01804bb80ae1d3e87de599393",
        url="file://{}/fluka-4-2.0.x86-Linux-gfor9.tgz".format(os.getcwd()),
    )

    conflicts("%gcc@:7", when="@4.2.0")

    depends_on("fortran", type="build")

    manual_download = True

    @property
    def download_instr(self):
        v = self.spec.version
        file = self.file_for_version(v)
        url = f"https://flukafiles.web.cern.ch/flukafiles/fluka-{v}/{file}"
        return f"""Manual download is required for {self.spec.name}.
            Register as a FLUKA user at https://fluka.cern/download/registration,
            then authenticate and download {url} into the current directory."""

    def file_for_version(self, version):
        return f"fluka-{version}.x86-Linux-gfor9.tgz"

    def url_for_version(self, version):
        return f"file://{os.getcwd()}/{self.file_for_version(version)}"

    def install(self, spec, prefix):
        with working_dir("src"):
            make()
        install_tree("bin", prefix.bin)
        install_tree("lib", prefix.lib)
        install_tree("data", prefix.data)
        install_tree("include", prefix.include)
        install_tree("doc", join_path(prefix.share, "doc"))
        install_tree("examples", join_path(prefix.share, "examples"))
        for file in [
            "AUTHORS",
            "INSTALL",
            "LICENSE",
            "REFERENCES",
            "RELEASE-NOTES",
            "README.md",
            "Version.tag",
        ]:
            install(file, prefix.share)

    def setup_run_environment(self, env):
        env.set("FLUDIR", self.spec.prefix)
