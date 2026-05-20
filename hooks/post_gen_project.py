import os
import subprocess
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
    "ruff>=0.15.10",
    "mypy>=1.20.1",
    "pre-commit>=4.5.1",
    "pytest>=9.0.3",
    "pytest-cov>=7.1.0",
    "pytest-mock>=3.15.1",
)

# mkdocs v2 will include breaking changes.
# See: https://github.com/ImperialCollegeLondon/python-template/discussions/530
DOC_DEPS = (
    "mkdocs>=1.6.1,<2.0.0",
    "mkdocstrings>=1.0.3",
    "mkdocstrings-python>=2.0.3",
    "mkdocs-material>=9.7.6",
    "mkdocs-gen-files>=0.6.1",
    "mkdocs-literate-nav>=0.6.3",
    "mkdocs-section-index>=0.3.11",
)

MKDOCS_ENABLED = "{{ cookiecutter.mkdocs }}" == "True"


def main():
    add_uv_dependencies()
    remove_unneeded_files()


def add_uv_dependencies():
    # setuptools-scm derives the version from git, which doesn't exist yet at generation time. # noqa: 501
    env = {**os.environ, "SETUPTOOLS_SCM_PRETEND_VERSION": "0.0.0"}
    subprocess.run(["uv", "add", "--dev", *DEV_DEPS], check=True, env=env)
    if MKDOCS_ENABLED:
        subprocess.run(["uv", "add", "--group", "doc", *DOC_DEPS], check=True, env=env)


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
