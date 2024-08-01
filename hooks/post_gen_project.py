import os
from glob import glob
from itertools import chain

REMOVE_PATHS = chain(
    (
        "{% if not cookiecutter.use_bsd3_licence %}LICENSE{% endif %}",
        "{% if not cookiecutter.add_precommit_workflows %}.github/workflows/pre-commit*.yml{% endif %}",
        "{% if not cookiecutter.automerge_bot_prs %}.github/workflows/auto-merge.yml{% endif %}",
        "{% if cookiecutter.packaging != 'pip-tools' %}*requirements.txt{% endif %}",
    ),
    glob("README.*.jinja"),
)

for path in REMOVE_PATHS:
    path = path.strip()
    if path:
        for file in glob(path):
            if os.path.isfile(file):
                os.unlink(file)
            else:
                os.rmdir(file)
