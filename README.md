<div align="center">

<img src="https://raw.githubusercontent.com/thedatavigilante/sierra-business-intelligence/main/docs/avatar-aia.png" width="100" style="border-radius: 50%; border: 2px solid #f59e0b;" alt="Sierra Napier">

<h1>Sierra Business Intelligence</h1>

<p><b>101 production figures · 3 verified datasets · 0 synthetic records</b></p>

<p>
  <a href="https://thedatavigilante.github.io/sierra-business-intelligence/">
    <img src="https://img.shields.io/badge/Portfolio-Live-FFB800?logo=githubpages" alt="Live Portfolio">
  </a>
  <a href="https://github.com/thedatavigilante/sierra-business-intelligence/actions/workflows/execute-notebooks.yml">
    <img src="https://github.com/thedatavigilante/sierra-business-intelligence/actions/workflows/execute-notebooks.yml/badge.svg" alt="CI">
  </a>
  <img src="https://img.shields.io/badge/python-3.11-blue?logo=python" alt="Python 3.11">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License MIT">
</p>

</div>

---

## 🚀 6-Second Scan

| | |
|:---|:---|
| **101 figures** | 30 Netflix · 49 Amazon · 22 Google |
| **8 dashboards** | Interactive Plotly + Streamlit |
| **9 notebooks** | 3 per project, fully executed |
| **76,594 records** | TMDB · Stanford SNAP · Google Trends |
| **0 synthetic** | Every number from real data |

**[→ Live Portfolio](https://thedatavigilante.github.io/sierra-business-intelligence/)**

---

## What This Is

A business intelligence portfolio bridging three domains — **content strategy**, **review intelligence**, and **market trends** — using the same end-to-end pattern: ingest real data, run SQL analytics, and ship stakeholder-ready dashboards.

Built for hiring managers who need proof that a candidate can work with messy real data, write clean SQL, and communicate findings to decision-makers.

---

## Verified Data Sources

| Project | Dataset | Records | Method |
|---------|---------|---------|--------|
| **Netflix** | TMDB Discover API (provider 8) | 7,498 titles | Live REST API |
| **Amazon** | Stanford SNAP — Amazon Reviews (Electronics 5-core) | 67,325 reviews | JSON.gz stream, 1/13 sample |
| **Google** | Google Trends via trendspy | 1,771 records | Live API, weekly granularity |

**Academic citation:** Ni, J., Li, J., & McAuley, J. (2019). *Justifying recommendations using distantly-labeled reviews and fined-grained aspects.* Proceedings of EMNLP.

---

## Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
  <img src="https://img.shields.io/badge/DuckDB-0.10-yellow?logo=duckdb">
  <img src="https://img.shields.io/badge/pandas-2.0-purple?logo=pandas">
  <img src="https://img.shields.io/badge/Plotly-5.15-blue?logo=plotly">
  <img src="https://img.shields.io/badge/Streamlit-1.28-red?logo=streamlit">
  <img src="https://img.shields.io/badge/SciPy-1.11-green?logo=scipy">
</p>

---

## Quick Start

```bash
# Clone
git clone https://github.com/thedatavigilante/sierra-business-intelligence.git
cd sierra-business-intelligence

# Install (Python 3.11 recommended)
pip install -r requirements.txt

# Run any project
cd projects/netflix-content-strategy-intelligence
python fetch_tmdb_data.py        # Live data from TMDB
jupyter lab notebooks/           # 3 executed notebooks
streamlit run dashboard.py       # Interactive dashboard
```

**Runtime:** ~2 minutes per project on a standard laptop. All notebooks are executed in CI on every push.

---

## Project Structure

```
sierra-business-intelligence/
├── projects/
│   ├── netflix-content-strategy-intelligence/      # 30 figs · 8 dashboards · 3 notebooks
│   ├── amazon-product-customer-intelligence/       # 49 figs · 3 notebooks
│   └── google-search-trends-market-intelligence/   # 22 figs · 3 notebooks
├── docs/
│   ├── index.html                                  # Live portfolio (GitHub Pages)
│   └── ARCHITECTURE.md                             # Data flow diagram
├── .github/workflows/                              # CI: notebook execution + data refresh
├── CITATION.cff                                    # Cite this repository
├── requirements.txt
└── LICENSE (MIT)
```

---

## Key Results

<details>
<summary><b>Netflix — Content Mix & Genre Strategy</b></summary>

- 69.6% movies vs. 30.4% TV shows — but TV turns around 2.5× faster (2.1 vs. 5.3 years)
- International Movies at 14.2% = largest untapped expansion opportunity
- [Interactive analysis →](https://thedatavigilante.github.io/sierra-business-intelligence/netflix-analysis.html)

</details>

<details>
<summary><b>Amazon — Review Quality Signals</b></summary>

- 59.5% of reviews are 5-star; 1-star reviews are 16% longer (642 vs. 553 chars)
- Long reviews achieve 91% helpfulness vs. 78% for short reviews
- 83.7% overall helpfulness rate across 67,325 real reviews

</details>

<details>
<summary><b>Google — Trend Breakout Detection</b></summary>

- AI search interest surged +70.7% YoY; inflation +68.9%; mental health +62.5%
- 262 weeks × 14 keywords × 3 granularity levels (worldwide / US / regional)
- Automated peak detection via `scipy.signal.find_peaks`

</details>

---

## Data Provenance & Limitations

All datasets are **public domain or CC0**. Zero synthetic records. No `generate_data.py`.

| Dataset | Host | Years | Limitation |
|---------|------|-------|------------|
| Netflix (TMDB) | Live API | 2026 | Snapshot in time; catalog changes daily |
| Amazon (SNAP) | Static archive | 1999–2014 | 15+ years old; patterns may not reflect current e-commerce |
| Google Trends | Live API | 2021–2026 | Sampling methodology undisclosed by Google; relative indices only |

---

## Citation

If you use this portfolio or its data pipeline in academic work:

```bibtex
@software{napier_sbi_2026,
  author = {Napier, Sierra},
  title = {Sierra Business Intelligence},
  url = {https://github.com/thedatavigilante/sierra-business-intelligence},
  year = {2026}
}
```

Or click **"Cite this repository"** in the right sidebar (powered by `CITATION.cff`).

---

## Contact

| | |
|:---|:---|
| 🐙 **GitHub** | [github.com/thedatavigilante](https://github.com/thedatavigilante) |
| 💼 **LinkedIn** | [linkedin.com/in/sierran](https://linkedin.com/in/sierran) |
| 📧 **Email** | s.napier430@gmail.com |
| 🌐 **Portfolio** | [thedatavigilante.github.io/sierra-business-intelligence](https://thedatavigilante.github.io/sierra-business-intelligence/) |

---

Built by **Sierra Napier** · License: MIT · Data follows original source terms
