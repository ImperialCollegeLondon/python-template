"""Tests for the main module."""

from {{ cookiecutter.project_slug }} import __version__


def test_version() -> None:
    """Check that the version is acceptable."""
    assert __version__ == "0.1.0"
