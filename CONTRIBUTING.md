# Contributing to Sierra Business Intelligence

Thank you for your interest in improving this portfolio. While this is primarily a personal project, constructive feedback, data corrections, and reproducibility improvements are welcome.

## How to Contribute

### Reporting Data Issues
If you find an inaccuracy in a figure, dataset claim, or citation:

1. Check the [Data Provenance & Limitations](README.md#data-provenance--limitations) section first
2. Open an issue using the **Data Correction** template
3. Include: the specific claim, the source you verified against, and a link or screenshot

### Suggesting Enhancements
For feature requests or new dataset integrations:

1. Open an issue using the **Feature Request** template
2. Describe the business value, proposed data source, and estimated scope

### Code Contributions
For bug fixes or tooling improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b fix/description`)
3. Make your changes with clear commit messages
4. Ensure notebooks execute cleanly (`jupyter execute` or run via CI)
5. Open a Pull Request using the provided template

## Development Setup

```bash
# Python 3.11 recommended
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Verify setup
python -c "import duckdb, pandas, plotly; print('OK')"
```

## Standards

- **Data integrity:** Any new dataset must include a Data Availability Statement (source, URL, access date, license)
- **Reproducibility:** Notebooks must execute top-to-bottom without errors on a clean environment
- **No synthetic data:** All figures must be generated from real, citable datasets
- **Commit messages:** Use present tense, imperative mood (`Fix trendspy timeout`, not `Fixed timeout`)

## Code of Conduct

Be respectful, constructive, and specific. This portfolio exists to demonstrate real-world data skills — help keep the bar high.
