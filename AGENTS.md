# Agent Instructions

This repository contains student-facing materials for **Coding 1: Data Management and Analysis with Python**.

## Course Constraints

- Use `uv` only for Python environment management.
- Do not add `pip`, `pipenv`, `Pipfile`, `%pip`, or `!pip` instructions to student-facing materials, except explicit "do not use" warnings.
- Keep Python targeted at 3.12 through `.python-version`, `pyproject.toml`, and `uv.lock`.
- Keep downloaded datasets out of Git. `scripts/fetch_data.py` writes external OSF files to `data/raw/`, which is ignored except for `.gitkeep`.
- Do not add grading, assessments, full syllabus policy, or solution notebooks unless explicitly requested.

## Expected Checks

Run these before opening or merging changes:

```bash
uv lock --check
uv sync --locked
uv run python scripts/fetch_data.py
uv run python scripts/check_no_pip.py
uv run python scripts/check_notebooks.py
```

For quick documentation-only edits, run at least:

```bash
uv run python scripts/check_no_pip.py
```

## Notebook Standards

- Notebooks should use the `Python 3 (ipykernel)` kernelspec.
- Keep notebooks valid JSON and clear large generated outputs unless the output is required for teaching.
- Prefer local data paths resolved from the repository root or `data/raw/`; do not read external datasets directly from notebooks.
- Student exercises should contain prompts and starter cells only, not solutions.

## Git Hygiene

- Treat `dev-notes/` as local working material unless the user explicitly asks to include it.
- Avoid committing `.venv/`, `data/raw/*.csv`, notebook checkpoints, or scratch exercise output.
- When splitting work into pull requests, keep one lecture directory per lecture PR and put shared infrastructure, schedule, data scripts, and exercises in separate focused PRs.
