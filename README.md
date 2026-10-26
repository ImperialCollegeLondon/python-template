<!-- markdownlint-disable MD041 -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![uv](https://github.com/ImperialCollegeLondon/python-template/actions/workflows/ci-uv.yml/badge.svg)](https://github.com/ImperialCollegeLondon/python-template/actions/workflows/ci-uv.yml)

# Python project template

This repo contains a [`cookiecutter`] template for a Python project, including
[`pre-commit`] hooks for linting and GitHub Actions for automatically running tests
using [`pytest`].

The template supports the Python packaging tool [`uv`].

It is particularly geared towards the needs of Imperial College's [Research Software
Engineering team], but hopefully it should be generically useful. If you find any
problems or have any questions, please [raise an issue].

[`cookiecutter`]: https://cookiecutter.readthedocs.io/en/stable/
[`pre-commit`]: https://pre-commit.com/
[`pytest`]: https://pytest.org/
[`uv`]: https://docs.astral.sh/uv/
[Research Software Engineering team]: https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/service-offering/research-software-engineering/
[raise an issue]: https://github.com/ImperialCollegeLondon/python-template/issues/new

## Usage

To use this template for your own application:

1. [Install `uv`] following the instructions for your OS.
2. Create your own project using this template: `uvx cookiecutter
gh:ImperialCollegeLondon/python-template`
3. Choose the options you want for your project
4. To get started, follow the instructions in the readme of the newly created project

# Extra setup

## Auto-merging bot PRs

This template optionally includes a [GitHub Actions] workflow to automatically
merge PRs from bots (specifically for [dependabot] and [pre-commit.ci]).
However, in order for this to work, you will first need to [follow GitHub's instructions]
for enabling auto-merge on your repository.

[GitHub Actions]: https://github.com/features/actions
[dependabot]: https://github.com/dependabot
[pre-commit.ci]: https://pre-commit.ci
[follow GitHub's instructions]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request#enabling-auto-merge

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/service-offering/research-software-engineering/"><img src="https://avatars.githubusercontent.com/u/23149834?v=4?s=100" width="100px;" alt="Alex Dewar"/><br /><sub><b>Alex Dewar</b></sub></a><br /><a href="https://github.com/ImperialCollegeLondon/python-template/commits?author=alexdewar" title="Code">💻</a></td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td align="center" size="13px" colspan="7">
        <img src="https://raw.githubusercontent.com/all-contributors/all-contributors-cli/1b8533af435da9854653492b1327a23a4dbd0a10/assets/logo-small.svg">
          <a href="https://all-contributors.js.org/docs/en/bot/usage">Add your contributions</a>
        </img>
      </td>
    </tr>
  </tfoot>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
