<!-- markdownlint-disable MD041 -->
[![poetry](https://github.com/alexdewar/cookiecutter-python-template/actions/workflows/ci-poetry.yml/badge.svg)](https://github.com/alexdewar/cookiecutter-python-template/actions/workflows/ci-poetry.yml)
[![pip-tools](https://github.com/alexdewar/cookiecutter-python-template/actions/workflows/ci-pip-tools.yml/badge.svg)](https://github.com/alexdewar/cookiecutter-python-template/actions/workflows/ci-pip-tools.yml)

# Python project template

This repo contains a [`cookiecutter`] template for a Python project, including
[`pre-commit`] hooks for linting and GitHub Actions for automatically running tests
using [`pytest`].

The template supports two Python packaging tools: [`poetry`] and [`pip-tools`].

[`cookiecutter`]: https://cookiecutter.readthedocs.io/en/stable/
[`pre-commit`]: https://pre-commit.com/
[`pytest`]: https://pytest.org/
[`poetry`]: https://python-poetry.org/
[`pip-tools`]: https://github.com/jazzband/pip-tools

## Usage

To use this template for your own application:

1. [Install `cookiecutter`] following the instructions for your OS.
1. Create your own project using this template: `cookiecutter
   gh:alexdewar/cookiecutter-python-template`
1. Choose the options you want for your project
1. To get started, follow the instructions in the readme of the newly created project

[Install `cookiecutter`]:
    https://cookiecutter.readthedocs.io/en/stable/README.html#installation
