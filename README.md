# Coding 1: Data Management and Analysis with Python

Course materials for the MSc Business Analytics Coding 1 course, running from **September 15, 2026** to **December 12, 2026**.

## Setup

1. Install `uv` from the official installer:
   - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - Windows PowerShell: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Clone or download this repository.
3. From the repository root, create the course environment:

```bash
uv sync
```

4. Download the external datasets used in the lectures:

```bash
uv run python scripts/fetch_data.py
```

5. Start JupyterLab:

```bash
uv run jupyter lab
```

In JupyterLab, use the `Python 3 (ipykernel)` kernel from this `uv` environment.

## Repository Layout

- `lectures/`: adapted lecture notebooks from `lecture00-intro` through `lecture10-intro-to-regression`
- `exercises/`: short practice notebooks for substantive teaching sessions
- `data/README.md`: dataset inventory and source links
- `scripts/fetch_data.py`: downloads external OSF datasets into `data/raw/`
- `schedule/session_plan.md`: 24-session teaching plan with `READING_WEEK_TBD`

## Validation

Run these checks from the repository root:

```bash
uv lock --check
uv sync --locked
uv run python scripts/fetch_data.py
uv run python scripts/check_no_pip.py
uv run python scripts/check_notebooks.py
```

Student-facing setup uses `uv` only. Do not use `pip`, `pipenv`, or notebook install commands for this course environment.

## AI Attribution

AIA HAb SeCeNc Hin R GPT-5.5 Opus4.7 v1.0
