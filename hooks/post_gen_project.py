import os
from glob import glob
from shutil import rmtree

REMOVE_PATHS = (
    "{% if not cookiecutter.use_bsd3_licence %}LICENSE{% endif %}",
    "{% if not cookiecutter.add_precommit_workflows %}.github/workflows/pre-commit*.yml{% endif %}",
    "{% if not cookiecutter.automerge_bot_prs %}.github/workflows/auto-merge.yml{% endif %}",
    "{% if cookiecutter.packaging != 'pip-tools' %}requirements.txt{% endif %}",
    "{% if cookiecutter.packaging != 'pip-tools' %}dev-requirements.txt{% endif %}",
    "{% if cookiecutter.packaging != 'pip-tools' or not cookiecutter.mkdocs %}doc-requirements.txt{% endif %}",
    "{% if not cookiecutter.mkdocs %}docs{% endif %}",
    "README.*.jinja",
)

for path in REMOVE_PATHS:
    path = path.strip()
    if path:
        for inode in glob(path):
            if os.path.isfile(inode):
                os.unlink(inode)
            else:
                rmtree(path)
