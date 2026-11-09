{%- set slug = cookiecutter.project_slug -%}
# Copilot Instructions

## Project layout and architecture

- This is a single Python 3.14+ package, `{{ slug }}`, managed with `uv` and built by setuptools. The version is dynamic: `{{ slug }}.__init__` reads installed package metadata, with `setuptools-scm` deriving it from Git tags.
- `{{ slug }}/__main__.py` is the `python -m {{ slug }}` entry point. Keep user-facing application behavior there or in package modules it calls.
- Keep tests in `tests/`; pytest collects doctests from package modules as well as test files.
{%- if cookiecutter.mkdocs %}
- Documentation is an MkDocs Material site. `docs/gen_ref_nav.py` generates API reference pages and navigation from `{{ slug }}/**/*.py`; it deliberately excludes `__main__.py` and maps package `__init__.py` files to `index.md`.
{%- endif %}

## Commands

```bash
# Install all development and documentation dependencies
uv sync --all-groups

# Run the package, tests, or one test
uv run python -m {{ slug }}
uv run pytest
uv run pytest tests/test_{{ slug }}.py::test_version

# Match CI quality checks
uv run mypy .
{%- if cookiecutter.mkdocs %}
uv run mkdocs build --strict
{%- endif %}
uv run pre-commit run --all-files
```

CI uses `uv sync`, then runs `mypy .` and `pytest`{% if cookiecutter.mkdocs %}; it installs the `doc` group before the strict MkDocs build.{% endif %}

## Repository conventions

- Maintain Python 3.14-compatible code. Mypy is strict for package code (`disallow_untyped_defs`, explicit `Any`, and generic `Any` are disallowed); only `tests.*` is exempt from mandatory typed definitions.
- Ruff enforces Google-style docstrings plus pycodestyle, Pyflakes, import sorting, pyupgrade, and Ruff rules. Test modules may omit module/package docstrings, but public package code should retain them.
- Use `uv add` / `uv remove` for dependencies, adding `--dev` or `--group <name>` for dependency groups; commit the resulting `pyproject.toml` and `uv.lock` changes.
- Pre-commit formats JSON, YAML, TOML, Markdown, and Python, runs Ruff with fixes, mypy, codespell, and GitHub workflow/schema validation.{% if cookiecutter.mkdocs %} Avoid hand-formatting generated reference files; MkDocs regenerates them.{% endif %}
- This project is a collaboration between research software engineers and domain experts. We avoid complex architectures, convoluted abstractions and software engineering jargon.
- The project directory may also contain an AGENTS.local.md. The file is git ignored and provides developer preferences for the current session.
