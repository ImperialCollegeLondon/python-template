import os

REMOVE_PATHS = [
    "{% if not cookiecutter.use_bsd3_licence %}LICENSE{% endif %}",
    "{% if not cookiecutter.add_precommit_workflows %}.github/workflows/pre-commit.yml{% endif %}",
    "{% if not cookiecutter.add_precommit_workflows %}.github/workflows/pre-commit_autoupdate.yml{% endif %}"
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)
