# Data Sources

## Primary Data Source

| Source | Type | Description | URL |
|--------|------|-------------|-----|
| Stanford SNAP mirror of UCSD Amazon Reviews Dataset | Public Dataset | Amazon product reviews for electronics category (5-core subset), mirrored on Stanford SNAP | https://snap.stanford.edu/data/amazon/productGraph/categoryFiles/ |

**Note:** This dataset was originally compiled by Julian McAuley at UCSD and is mirrored on Stanford SNAP for distribution. Both URLs resolve to the same dataset.

## Data Provenance

- Original author: Julian McAuley (UCSD)
- Mirror host: Stanford Network Analysis Project (SNAP)
- Dataset: Amazon Reviews — Electronics category, 5-core subset
- Citation: Ni, J., Li, J., & McAuley, J. (2019). *Justifying recommendations using distantly-labeled reviews and fined-grained aspects.* Proceedings of EMNLP.
- Records: 67,325 real reviews (1/13 uniform sample from 1.69M total)
- Unique products: 27,832
- Unique reviewers: 53,609
- Date span: 2003-01-01 to 2013-12-09

## Download URL

Direct download link used by fetch script:
```
http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Electronics_5.json.gz
```

## Data Files

| File | Description | Size (approx) |
|------|-------------|---------------|
| `amazon_reviews_electronics_5core.csv` | Processed UCSD Amazon electronics reviews (5-core subset, 1/13 sample) | ~50MB |
| `reviews_Electronics_5.json.gz` | Raw Stanford SNAP source (not tracked in repo) | 495MB |

## Refresh Strategy

- Dataset is static historical data; no live refresh required
- Re-download from Stanford SNAP if updates are published
- Sampling (1/13, seed=42) is deterministic and reproducible
