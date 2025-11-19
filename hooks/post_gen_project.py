import os
from glob import glob
from shutil import rmtree
import re

REMOVE_PATHS = (
    "{% if not cookiecutter.use_bsd3_license %}LICENSE{% endif %}",
    "{% if not cookiecutter.add_precommit_workflows %}.github/workflows/pre-commit*.yml{% endif %}",
    "{% if not cookiecutter.automerge_bot_prs %}.github/workflows/auto-merge.yml{% endif %}",
    "{% if cookiecutter.packaging != 'pip-tools' %}requirements.txt{% endif %}",
    "{% if cookiecutter.packaging != 'pip-tools' %}dev-requirements.txt{% endif %}",
    "{% if cookiecutter.packaging != 'pip-tools' or not cookiecutter.mkdocs %}doc-requirements.txt{% endif %}",
    "{% if not cookiecutter.mkdocs %}docs{% endif %}",
    "{% if not cookiecutter.mkdocs %}.github/workflows/docs.yml{% endif %}",
    "README.*.jinja",
)


def main():
    # {% if cookiecutter.packaging == 'poetry' %}
    update_poetry_dependencies()
    # {% endif %}
    # {% if cookiecutter.packaging == 'uv' %}
    update_uv_dependencies()
    # {% endif %}
    remove_unneeded_files()


def read_package_versions(*filenames: str) -> dict[str, str]:
    """Read package versions from *requirements.txt."""
    regex = re.compile("^([^# ]+)==(.+)$")
    packages: dict[str, str] = {}
    for filename in filenames:
        with open(filename) as f:
            for line in f.readlines():
                if match := regex.match(line):
                    name = match.group(1).lower()
                    version = match.group(2)
                    packages[name] = version
    return packages


def update_poetry_dependencies(pyproject_path: str = "pyproject.toml"):
    """Patch the versions of packages in pyproject.toml."""
    packages = read_package_versions(
        "doc-requirements.txt", "dev-requirements.txt", "requirements.txt"
    )

    output = ""
    regex = re.compile('^([^ ]+) = "VERSION"$')
    with open(pyproject_path) as f:
        for line in f.readlines():
            if match := regex.match(line):
                name = match.group(1)
                output += f'{name} = "^{packages[name.lower()]}"\n'
            else:
                output += line
    with open(pyproject_path, "w") as f:
        f.write(output)


def update_uv_dependencies(pyproject_path: str = "pyproject.toml"):
    """Patch the versions of packages in pyproject.toml."""
    packages = read_package_versions(
        "doc-requirements.txt", "dev-requirements.txt", "requirements.txt"
    )

    output = ""
    regex = re.compile(r'"([A-Za-z0-9_\-]+)\s*([=<>!~]+)\s*VERSION"')
    with open(pyproject_path) as f:
        for line in f.readlines():
            if match := regex.match(line.strip()):
                name = match.group(1)
                operator = match.group(2)
                version = packages[name.lower()]
                comma = "," if line.strip().endswith(",") else ""
                output += f'    "{name}{operator}{version}"{comma}\n'
            else:
                output += line
    with open(pyproject_path, "w") as f:
        f.write(output)


def remove_unneeded_files():
    for path in REMOVE_PATHS:
        path = path.strip()
        if path:
            for inode in glob(path):
                if os.path.isfile(inode):
                    os.unlink(inode)
                else:
                    rmtree(path)


if __name__ == "__main__":
    main()
