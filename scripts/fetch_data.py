"""Download external datasets used by the course notebooks."""

from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "raw"


@dataclass(frozen=True)
class Dataset:
    filename: str
    url: str
    description: str


DATASETS = (
    Dataset("hotel_vienna_raw.csv", "https://osf.io/yzntm/download", "Hotels Vienna raw data"),
    Dataset("hotels_europe_price.csv", "https://osf.io/p6tyr/download", "Hotels Europe prices"),
    Dataset("hotels_europe_features.csv", "https://osf.io/utwjs/download", "Hotels Europe features"),
    Dataset("sp500.csv", "https://osf.io/4pgrf/download", "S&P 500 data"),
    Dataset("billion_prices.csv", "https://osf.io/yhbr5/download", "Billion Prices data"),
    Dataset("hotels_vienna.csv", "https://osf.io/y6jvb/download", "Hotels Vienna regression data"),
)


def download(dataset: Dataset, force: bool) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    target = DATA_DIR / dataset.filename
    if target.exists() and target.stat().st_size > 0 and not force:
        print(f"exists: {target.relative_to(ROOT)}")
        return

    temp = target.with_suffix(target.suffix + ".tmp")
    print(f"download: {dataset.description} -> {target.relative_to(ROOT)}")
    request = urllib.request.Request(dataset.url, headers={"User-Agent": "coding-1-course/2026"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response, temp.open("wb") as output:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                output.write(chunk)
    except (urllib.error.URLError, TimeoutError) as exc:
        if temp.exists():
            temp.unlink()
        raise RuntimeError(f"failed to download {dataset.url}: {exc}") from exc

    if temp.stat().st_size == 0:
        temp.unlink()
        raise RuntimeError(f"downloaded empty file for {dataset.url}")
    temp.replace(target)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="re-download files that already exist")
    args = parser.parse_args()

    try:
        for dataset in DATASETS:
            download(dataset, force=args.force)
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
