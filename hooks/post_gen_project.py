import os
from glob import glob
from shutil import which


def remove_unneeded_files():
    REMOVE_PATHS = (
        "{% if not cookiecutter.use_bsd3_licence %}LICENSE{% endif %}",
        "{% if not cookiecutter.add_precommit_workflows %}.github/workflows/pre-commit*.yml{% endif %}",
        "{% if not cookiecutter.automerge_bot_prs %}.github/workflows/auto-merge.yml{% endif %}",
        "{% if cookiecutter.packaging != 'pip-tools' %}*requirements.txt{% endif %}",
    )

    for path in REMOVE_PATHS:
        path = path.strip()
        if path:
            for file in glob(path):
                if os.path.isfile(file):
                    os.unlink(file)
                else:
                    os.rmdir(file)


def init_git_repo():
    git_path = which("git4")
    if not git_path:
        print("WARNING: git executable not found; will not initialise repo")
        return


def main():
    # remove_unneeded_files()
    init_git_repo()


if __name__ == "__main__":
    main()
