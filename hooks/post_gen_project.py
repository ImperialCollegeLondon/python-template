import subprocess
import os
from glob import glob
from shutil import rmtree

REMOVE_PATHS = (
    "{% if not cookiecutter.use_bsd3_license %}LICENSE{% endif %}",
    "{% if not cookiecutter.add_precommit_workflows %}.github/workflows/pre-commit*.yml{% endif %}",
    "{% if not cookiecutter.automerge_bot_prs %}.github/workflows/auto-merge.yml{% endif %}",
    "{% if not cookiecutter.mkdocs %}docs{% endif %}",
    "{% if not cookiecutter.mkdocs %}.github/workflows/docs.yml{% endif %}",
    "README.*.jinja",
)

DEV_DEPS = (
    "ruff",
    "mypy",
    "pre-commit",
    "pytest",
    "pytest-cov",
    "pytest-mock",
)

# mkdocs v2 will include breaking changes.
# See: https://github.com/ImperialCollegeLondon/python-template/discussions/530
DOC_DEPS = (
    "mkdocs<2",
    "mkdocstrings",
    "mkdocstrings-python",
    "mkdocs-material",
    "mkdocs-gen-files",
    "mkdocs-literate-nav",
    "mkdocs-section-index",
)

MKDOCS_ENABLED = "{{ cookiecutter.mkdocs }}" == "True"


def main():
    check_uv_installed()
    add_uv_dependencies()
    remove_unneeded_files()


def check_uv_installed():
    try:
        subprocess.run(["uv", "--version"], check=True, stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        print(
            "Error: 'uv' command not found. Please install 'uv' to use this template."
        )
        exit(1)


def add_uv_dependencies():
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["uv", "add", "--dev", *DEV_DEPS], check=True)
    if MKDOCS_ENABLED:
        subprocess.run(["uv", "add", "--group", "doc", *DOC_DEPS], check=True)


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
