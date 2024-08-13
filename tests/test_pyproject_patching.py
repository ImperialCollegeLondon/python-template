from hooks.post_gen_project import read_package_versions, update_poetry_dependencies
from pathlib import Path
from unittest.mock import patch, Mock


def test_read_package_versions(tmp_path: Path):
    REQUIREMENTS1 = """
# This is a comment
package_a==1.2.3
package_b==4.5.6
"""
    path1 = tmp_path / "requirements1.txt"
    with path1.open("w") as f:
        f.write(REQUIREMENTS1)

    # Single file
    assert read_package_versions(str(path1)) == {
        "package_a": "1.2.3",
        "package_b": "4.5.6",
    }

    REQUIREMENTS2 = """
package_b==1.2.3
# Another comment
package_c==4.5.6
"""
    path2 = tmp_path / "requirements2.txt"
    with path2.open("w") as f:
        f.write(REQUIREMENTS2)

    # Multiple files
    assert read_package_versions(str(path1), str(path2)) == {
        "package_a": "1.2.3",
        "package_b": "1.2.3",
        "package_c": "4.5.6",
    }

    REQUIREMENTS3 = "package_B==1.2.3"
    path3 = tmp_path / "requirements3.txt"
    with path3.open("w") as f:
        f.write(REQUIREMENTS3)

    # Package names should be converted to lowercase
    assert read_package_versions(str(path1), str(path3)) == {
        "package_a": "1.2.3",
        "package_b": "1.2.3",
    }


PYPROJECT = """[tool.poetry]
name = "my_project"
authors = [
    "Jane Doe <jane_doe@imperial.ac.uk>",
]

[tool.poetry.dependencies]
python = "^3.12"
package_a = "{package_a}"

[tool.poetry.group.dev.dependencies]
package_b = "{package_b}"

[tool.mypy]
disallow_any_explicit = true

def test_update_poetry_dependencies(tmp_path: Path):
"""


@patch("hooks.post_gen_project.read_package_versions")
def test_update_poetry_dependencies(read_versions_mock: Mock, tmp_path: Path):
    pyproject_path = tmp_path / "pyproject.toml"
    with pyproject_path.open("w") as f:
        f.write(PYPROJECT.format(package_a="VERSION", package_b="VERSION"))

    read_versions_mock.return_value = {"package_a": "1.2.3", "package_b": "4.5.6"}
    update_poetry_dependencies(str(pyproject_path))
    with pyproject_path.open() as f:
        content = f.read()
    assert content == PYPROJECT.format(package_a="^1.2.3", package_b="^4.5.6")
