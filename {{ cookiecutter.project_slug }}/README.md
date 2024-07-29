# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

{% if cookiecutter.packaging == "poetry" -%}
This is a Python application that uses [poetry](https://python-poetry.org) for packaging
and dependency management. It also provides [pre-commit](https://pre-commit.com/) hooks
(for [ruff](https://pypi.org/project/ruff/) and
[mypy](https://mypy.readthedocs.io/en/stable/)) and automated tests using
[pytest](https://pytest.org/) and [GitHub Actions](https://github.com/features/actions).

## For developers

This is a Python application that uses [poetry](https://python-poetry.org) for packaging
and dependency management. It also provides [pre-commit](https://pre-commit.com/) hooks
for various linters and formatters and automated tests using
[pytest](https://pytest.org/) and [GitHub Actions](https://github.com/features/actions).
Pre-commit hooks are automatically kept updated with a dedicated GitHub Action.

To get started:

1. [Download and install Poetry](https://python-poetry.org/docs/#installation) following the instructions for your OS.
1. Clone this repository and make it your working directory
1. Set up the virtual environment:

   ```bash
   poetry install
   ```

1. Activate the virtual environment (alternatively, ensure any Python-related command is preceded by `poetry run`):

   ```bash
   poetry shell
   ```

1. Install the git hooks:

   ```bash
   pre-commit install
   ```

1. Run the main app:

   ```bash
   python -m {{ cookiecutter.project_slug }}
   ```

{% elif cookiecutter.packaging == "pip-tools" -%}
This is a minimal Python 3.12 application that uses [`pip-tools`] for packaging and dependency management. It also provides [`pre-commit`](https://pre-commit.com/) hooks (for for [ruff](https://pypi.org/project/ruff/) and [`mypy`](https://mypy.readthedocs.io/en/stable/)) and automated tests using [`pytest`](https://pytest.org/) and [GitHub Actions](https://github.com/features/actions). Pre-commit hooks are automatically kept updated with a dedicated GitHub Action, this can be removed and replace with [pre-commit.ci](https://pre-commit.ci) if using an public repo. It was developed by the [Imperial College Research Computing Service](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/).

[`pip-tools`] is chosen as a lightweight dependency manager that adheres to the [latest standards](https://peps.python.org/pep-0621/) using `pyproject.toml`.

## Usage

To use this repository as a template for your own application:

1. Click the green "Use this template" button above
2. Name and create your repository
3. Clone your new repository and make it your working directory
4. Replace instances of `myproject` with your own application name. Edit:
   - `pyproject.toml` (also change the list of authors here)
   - `tests/test_myproject.py`
   - Rename `myproject` directory
5. Create and activate a Virtual Environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate # with Powershell on Windows: `.venv\Scripts\Activate.ps1`
   ```

6. Install development requirements:

   ```bash
   pip install -r dev-requirements.txt
   ```

7. Install the git hooks:

   ```bash
   pre-commit install
   ```

8. Run the main app:

   ```bash
   python -m myproject
   ```

9. Run the tests:

   ```bash
   pytest
   ```

### Updating Dependencies

To add or remove dependencies:

1. Edit the `dependencies` variables in the `pyproject.toml` file (aim to keep development tools separate from the project requirements).
2. Update the requirements files:
   - `pip-compile` for `requirements.txt` - the project requirements.
   - `pip-compile --extra dev -o dev-requirements.txt` for `dev-requirements.txt` - the development requirements.
3. Sync the files with your installation (install packages):
   - `pip-sync dev-requirements.txt requirements.txt`

To upgrade pinned versions, use the `--upgrade` flag with `pip-compile`.

Versions can be restricted from updating within the `pyproject.toml` using standard python package version specifiers, i.e. `"black<23"` or `"pip-tools!=6.12.2"`

### Customising

All configuration can be customised to your preferences. The key places to make changes
for this are:

- The `pyproject.toml` file, where you can edit:
  - The build system (change from setuptools to other packaging tools like [Hatch](https://hatch.pypa.io/) or [flit](https://flit.pypa.io/)).
  - The python version.
  - The project dependencies. Extra optional dependencies can be added by adding another list under `[project.optional-dependencies]` (i.e. `doc = ["mkdocs"]`).
  - The `mypy` and `pytest` configurations.
- The `.pre-commit-config.yaml` for pre-commit settings.
- The `.github` directory for all the CI configuration.
  - This repo uses `pre-commit.ci` to update pre-commit package versions and automatically merges those PRs with the `auto-merge.yml` workflow.
  - Note that `pre-commit.ci` is an external service and free for open source repos. For private repos uncomment the commented portion of the `pre-commit_autoupdate.yml` workflow.

[`pip-tools`]: https://pip-tools.readthedocs.io/en/latest/
{% endif %}

### Publishing

The GitHub workflow includes an action to publish on release.
To run this action, uncomment the commented portion of `publish.yml`, and modify the steps for the desired behaviour (publishing a Docker image, publishing to PyPI, deploying documentation etc.)
