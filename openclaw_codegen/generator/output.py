"""Format and synchronize generated files."""

import shutil
import subprocess
from pathlib import Path

from openclaw_codegen.generator.types import GenerationPaths


def format_outputs(outputs: dict[Path, str], *, package_root: Path) -> dict[Path, str]:
    return {
        path: _format_python(path, content, package_root=package_root) if path.suffix == ".py" else content
        for path, content in outputs.items()
    }


def _format_python(path: Path, content: str, *, package_root: Path) -> str:
    candidates = [
        package_root / ".venv" / "Scripts" / "ruff.exe",
        package_root / ".venv" / "bin" / "ruff",
    ]
    discovered_ruff = shutil.which("ruff")
    if discovered_ruff is not None:
        candidates.append(Path(discovered_ruff))
    ruff = next((candidate for candidate in candidates if candidate.exists()), None)
    if ruff is None:
        raise RuntimeError("Ruff is required to generate the OpenClaw client")
    checked = subprocess.run(
        [str(ruff), "check", "--fix", "--fix-only", "--stdin-filename", str(path), "-"],
        cwd=package_root,
        input=content,
        capture_output=True,
        check=True,
        text=True,
    ).stdout
    return subprocess.run(
        [str(ruff), "format", "--stdin-filename", str(path), "-"],
        cwd=package_root,
        input=checked,
        capture_output=True,
        check=True,
        text=True,
    ).stdout


def obsolete_outputs(paths: GenerationPaths, domains: list[str]) -> list[Path]:
    outputs = [
        paths.generated / "models.py",
        paths.generated / "operations.py",
        paths.generated / "namespaces.py",
        paths.generated / "namespaces" / "__init__.py",
    ]
    outputs.extend(paths.generated / "namespaces" / f"{domain}.py" for domain in domains)
    outputs.extend(paths.generated / domain / "models.py" for domain in domains)
    for domain in domains:
        outputs.extend(
            [
                paths.generated / domain / "__init__.py",
                paths.generated / domain / "client.py",
                paths.generated / domain / "events.py",
            ]
        )
    return outputs


def apply_outputs(outputs: dict[Path, str], obsolete: list[Path], *, check: bool) -> bool:
    changed = False
    for path in obsolete:
        if path.exists():
            changed = True
            if not check:
                path.unlink()
    for path, content in outputs.items():
        existing = path.read_text(encoding="utf-8") if path.exists() else None
        if existing != content:
            changed = True
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")
    return changed
