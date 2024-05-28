# Poetry Template

[![Test and build](https://github.com/ImperialCollegeLondon/poetry_template_2/actions/workflows/ci.yml/badge.svg)](https://github.com/ImperialCollegeLondon/poetry_template_2/actions/workflows/ci.yml)

This is a minimal Python 3.12 application that uses [poetry](https://python-poetry.org) for packaging and dependency management. It also provides [pre-commit](https://pre-commit.com/) hooks (for [ruff](https://pypi.org/project/ruff/) and [mypy](https://mypy.readthedocs.io/en/stable/)) and automated tests using [pytest](https://pytest.org/) and [GitHub Actions](https://github.com/features/actions). Pre-commit hooks are automatically kept updated with a dedicated GitHub Action, this can be removed and replace with [pre-commit.ci](https://pre-commit.ci) if using an public repo. It was developed by the [Imperial College Research Computing Service](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/).

## Usage

To use this repository as a template for your own application:

1. [Download and install Poetry](https://python-poetry.org/docs/#installation) following the instructions for your OS.
2. Click the green "Use this template" button above
3. Name and create your repository
4. Clone your new repository and make it your working directory
5. Replace instances of `myproject` with your own application name. Edit:
   - `pyproject.toml`
   - `tests/test_myproject.py`
   - Rename `myproject` directory
6. Set up the virtual environment:

   ```bash
   poetry install
   ```

7. Activate the virtual environment (alternatively, ensure any python-related command is preceded by `poetry run`):

   ```bash
   poetry shell
   ```

8. Install the git hooks:

   ```bash
   pre-commit install
   ```

9. Run the main app:

   ```bash
   python -m myproject
   ```

10. Run the tests:

    ```bash
    pytest
    ```

### Publishing

The GitHub workflow includes an action to publish on release.
To run this action, uncomment the commented portion of `publish.yml`, and modify the steps for the desired behaviour (ie. publishing a Docker image, publishing to PyPI, deploying documentation etc.)
