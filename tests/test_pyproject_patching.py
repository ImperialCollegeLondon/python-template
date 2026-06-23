from unittest.mock import patch

from hooks import post_gen_project


def test_check_uv_installed_success(monkeypatch):
    with patch("hooks.post_gen_project.subprocess.run") as mock_run:
        post_gen_project.check_uv_installed()
    mock_run.assert_called_once_with(["uv", "--version"], check=True, stdout=-3)


def test_check_uv_installed_failure(monkeypatch):
    with patch("hooks.post_gen_project.subprocess.run", side_effect=FileNotFoundError):
        with patch("builtins.print") as mock_print:
            with patch("builtins.exit") as mock_exit:
                post_gen_project.check_uv_installed()
    mock_print.assert_called_once_with(
        "Error: 'uv' command not found. Please install 'uv' to use this template."
    )
    mock_exit.assert_called_once_with(1)


def test_add_uv_dependencies_dev_only(monkeypatch):
    monkeypatch.setattr(post_gen_project, "MKDOCS_ENABLED", False)
    with patch("hooks.post_gen_project.subprocess.run") as mock_run:
        post_gen_project.add_uv_dependencies()
    assert mock_run.call_count == 2
    call = mock_run.call_args_list[1]
    assert call.args[0] == ["uv", "add", "--dev", *post_gen_project.DEV_DEPS]
    assert call.kwargs["check"] is True


def test_add_uv_dependencies_includes_doc_group_when_mkdocs_enabled(monkeypatch):
    monkeypatch.setattr(post_gen_project, "MKDOCS_ENABLED", True)
    with patch("hooks.post_gen_project.subprocess.run") as mock_run:
        post_gen_project.add_uv_dependencies()
    assert mock_run.call_count == 3
    assert mock_run.call_args_list[1].args[0] == [
        "uv",
        "add",
        "--dev",
        *post_gen_project.DEV_DEPS,
    ]
    assert mock_run.call_args_list[2].args[0] == [
        "uv",
        "add",
        "--group",
        "doc",
        *post_gen_project.DOC_DEPS,
    ]


def test_mkdocs_constraint_preserves_v2_upper_bound():
    mkdocs_pin = next(d for d in post_gen_project.DOC_DEPS if d.startswith("mkdocs<"))
    assert "<2" in mkdocs_pin
