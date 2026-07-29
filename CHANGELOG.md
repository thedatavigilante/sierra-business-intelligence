# Changelog

All notable changes to this portfolio are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-07-29

### Changed
- **Complete README rewrite** — Reduced from ~500 lines to ~120 lines; restructured as landing page with collapsible deep dives
- **Data source accuracy** — Amazon source corrected from "UCSD" to "Stanford SNAP mirror of UCSD"
- **Tool accuracy** — Google Trends tool updated from archived `pytrends` to maintained `trendspy` successor
- **Record counts verified** — Netflix 7,498 titles (TMDB), Amazon 67,325 reviews, Google 1,771 records
- **Figure counts verified** — Total: 101 production figures + 8 interactive dashboards

### Added
- `CITATION.cff` — Enables GitHub "Cite this repository" widget
- `CONTRIBUTING.md` — Contributor guidelines and development setup
- `CHANGELOG.md` — This file
- `.github/ISSUE_TEMPLATE/` — Bug report, data correction, and feature request templates
- `.github/PULL_REQUEST_TEMPLATE.md` — Standardized PR checklist
- `docs/ARCHITECTURE.md` — Data flow diagram for all three pipelines

### Removed
- Dead domain reference `e3-ai.com` from contact section
- Outdated `pytrends` references in requirements and documentation

## [1.0.0] — 2026-05-21

### Added
- Initial portfolio release with 3 projects:
  - Netflix Content Strategy Intelligence (TMDB API)
  - Amazon Product Review Intelligence (Stanford SNAP)
  - Google Search Trends Market Intelligence (trendspy)
- 9 Jupyter notebooks (3 per project)
- 101 production figures (matplotlib + Plotly)
- 8 interactive Plotly dashboards
- Live GitHub Pages portfolio site
- CI/CD workflows: notebook execution, data refresh, catalog sync
