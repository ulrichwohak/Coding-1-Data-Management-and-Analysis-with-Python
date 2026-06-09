# Course Setup

This course uses `uv` for Python version and dependency management.

## 1. Install `uv`

- macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows PowerShell: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

Close and reopen your terminal after installation if the `uv` command is not found.

## 2. Create the Course Environment

From the repository root:

```bash
uv sync
```

This creates `.venv/` and installs the package versions recorded in `uv.lock`.

## 3. Download Data

```bash
uv run python scripts/fetch_data.py
```

The script writes external datasets to `data/raw/`.

## 4. Start JupyterLab

```bash
uv run jupyter lab
```

Open the notebooks from the `lectures/` or `exercises/` folders and choose the `Python 3 (ipykernel)` kernel from this course environment.
