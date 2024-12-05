"""The main module for {{ cookiecutter.project_name }}."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("MUSE_OS")
except PackageNotFoundError:
    pass
