try:
    from spack_repo.eic.packages.epic.package import Epic
except ImportError:
    from spack.pkg.eic.epic import Epic


class EpicEic(Epic):
    pass
