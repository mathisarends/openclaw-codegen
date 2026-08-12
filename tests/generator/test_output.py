from pathlib import Path

from openclaw_codegen.generator.output import apply_outputs, obsolete_outputs
from openclaw_codegen.generator.types import GenerationPaths


def test_obsolete_outputs_lists_legacy_paths_per_domain(tmp_path: Path) -> None:
    paths = GenerationPaths.from_package_root(tmp_path)
    obsolete = obsolete_outputs(paths, ["chat"])
    assert paths.generated / "namespaces" / "chat.py" in obsolete
    assert paths.generated / "chat" / "client.py" in obsolete
    assert paths.generated / "chat" / "events.py" in obsolete
    assert paths.generated / "models.py" in obsolete


def test_apply_outputs_check_mode_reports_changes_without_writing(tmp_path: Path) -> None:
    target = tmp_path / "out.py"
    assert apply_outputs({target: "content"}, [], check=True) is True
    assert not target.exists()


def test_apply_outputs_writes_new_files_and_is_idempotent(tmp_path: Path) -> None:
    target = tmp_path / "sub" / "out.py"
    assert apply_outputs({target: "content"}, [], check=False) is True
    assert target.read_text(encoding="utf-8") == "content"
    assert apply_outputs({target: "content"}, [], check=False) is False


def test_apply_outputs_removes_obsolete_files_only_when_not_checking(tmp_path: Path) -> None:
    obsolete = tmp_path / "old.py"
    obsolete.write_text("legacy", encoding="utf-8")

    assert apply_outputs({}, [obsolete], check=True) is True
    assert obsolete.exists()

    assert apply_outputs({}, [obsolete], check=False) is True
    assert not obsolete.exists()
