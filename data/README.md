# Data

The repository keeps small local teaching files with the relevant lecture folders. Larger or external datasets are downloaded into `data/raw/` by:

```bash
uv run python scripts/fetch_data.py
```

Downloaded files are ignored by Git so the repository stays lightweight.

| Local file | Source | Used by |
| --- | --- | --- |
| `data/raw/hotel_vienna_raw.csv` | <https://osf.io/yzntm/download> | lecture04 data munging |
| `data/raw/hotels_europe_price.csv` | <https://osf.io/p6tyr/download> | lecture05 plotnine |
| `data/raw/hotels_europe_features.csv` | <https://osf.io/utwjs/download> | lecture05 plotnine |
| `data/raw/sp500.csv` | <https://osf.io/4pgrf/download> | lecture05 matplotlib and function practice |
| `data/raw/billion_prices.csv` | <https://osf.io/yhbr5/download> | lecture07 data exploration |
| `data/raw/hotels_vienna.csv` | <https://osf.io/y6jvb/download> | lecture10 regression |
