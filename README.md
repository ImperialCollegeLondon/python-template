<!-- markdownlint-disable MD041 -->
[![poetry](https://github.com/ImperialCollegeLondon/python-template/actions/workflows/ci-poetry.yml/badge.svg)](https://github.com/ImperialCollegeLondon/python-template/actions/workflows/ci-poetry.yml)
[![pip-tools](https://github.com/ImperialCollegeLondon/python-template/actions/workflows/ci-pip-tools.yml/badge.svg)](https://github.com/ImperialCollegeLondon/python-template/actions/workflows/ci-pip-tools.yml)

# Python project template

This repo contains a [`cookiecutter`] template for a Python project, including
[`pre-commit`] hooks for linting and GitHub Actions for automatically running tests
using [`pytest`].

The template supports two Python packaging tools: [`poetry`] and [`pip-tools`].

It is particularly geared towards the needs of Imperial College's [Research Software
Engineering team], but hopefully it should be generically useful. If you find any
problems or have any questions, please [raise an issue].

[`cookiecutter`]: https://cookiecutter.readthedocs.io/en/stable/
[`pre-commit`]: https://pre-commit.com/
[`pytest`]: https://pytest.org/
[`poetry`]: https://python-poetry.org/
[`pip-tools`]: https://github.com/jazzband/pip-tools
[Research Software Engineering team]: https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/service-offering/research-software-engineering/
[raise an issue]: https://github.com/ImperialCollegeLondon/python-template/issues/new

## Usage

To use this template for your own application:

1. [Install `cookiecutter`] following the instructions for your OS.
1. Create your own project using this template: `cookiecutter
   gh:ImperialCollegeLondon/python-template`
1. Choose the options you want for your project
1. To get started, follow the instructions in the readme of the newly created project

[Install `cookiecutter`]:
    https://cookiecutter.readthedocs.io/en/stable/README.html#installation

# Extra setup

## Auto-merging bot PRs

This template optionally includes a [GitHub Actions] workflow to automatically merge PRs
from bots (specifically for [dependabot] and [pre-commit.ci]). However, in order for
this to work, you will first need to [follow GitHub's instructions] for enabling
auto-merge on your repository.

[GitHub Actions]: https://github.com/features/actions
[dependabot]: https://github.com/dependabot
[pre-commit.ci]: https://pre-commit.ci
[follow GitHub's instructions]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request#enabling-auto-merge
