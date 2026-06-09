"""Reject legacy package-management commands in student-facing materials."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECK_ROOTS = ["README.md", "lectures", "exercises", "data", "schedule"]
PATTERNS = (
    re.compile(r"(?<!uv\s)\bpip\b", re.IGNORECASE),
    re.compile(r"\bpip3\b", re.IGNORECASE),
    re.compile(r"\bpipenv\b", re.IGNORECASE),
    re.compile(r"\bPipfile(?:\.lock)?\b"),
    re.compile(r"[%!]pip\b", re.IGNORECASE),
)
ALLOWED_PHRASES = (
    "do not use `pip`",
    "do not use `pip`, `pipenv`",
)


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for item in CHECK_ROOTS:
        path = ROOT / item
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(
                p
                for p in path.rglob("*")
                if p.is_file()
                and ".ipynb_checkpoints" not in p.parts
                and p.suffix.lower() in {".md", ".py", ".txt", ".ipynb", ".yml", ".yaml"}
            )
    return sorted(files)


def notebook_lines(path: Path) -> list[tuple[int, str]]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    lines: list[tuple[int, str]] = []
    line_number = 1
    for cell in notebook.get("cells", []):
        for line in cell.get("source", []):
            lines.append((line_number, line.rstrip("\n")))
            line_number += 1
    return lines


def text_lines(path: Path) -> list[tuple[int, str]]:
    return [
        (index, line.rstrip("\n"))
        for index, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1)
    ]


def is_allowed(line: str) -> bool:
    lowered = line.lower()
    return any(phrase in lowered for phrase in ALLOWED_PHRASES)


def main() -> int:
    failures: list[str] = []
    for path in iter_text_files():
        lines = notebook_lines(path) if path.suffix == ".ipynb" else text_lines(path)
        for line_number, line in lines:
            if is_allowed(line):
                continue
            if any(pattern.search(line) for pattern in PATTERNS):
                rel = path.relative_to(ROOT)
                failures.append(f"{rel}:{line_number}: {line}")

    if failures:
        print("Legacy package-management references found:")
        print("\n".join(failures))
        return 1
    print("No legacy package-management references found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
