# Architecture & Data Flow

This document describes how data flows through the Sierra Business Intelligence portfolio.

## High-Level Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   TMDB API      │     │ Stanford SNAP   │     │ Google Trends   │
│   (Live REST)   │     │   (Static)      │     │   (Live API)    │
│   7,498 titles  │     │  495MB JSON.gz  │     │  1,771 records  │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                     INGESTION LAYER                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │fetch_tmdb_   │  │fetch_amazon_ │  │fetch_trends_ │           │
│  │data.py       │  │data.py       │  │data.py       │           │
│  │· auth key    │  │· 1/13 sample │  │· trendspy    │           │
│  │· rate limit  │  │· seed=42     │  │· 14 keywords │           │
│  │· 40 req/10s  │  │· streaming   │  │· 262 weeks   │           │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘           │
└─────────┼─────────────────┼─────────────────┼────────────────────┘
          ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                     STORAGE / RAW                                │
│  netflix_catalog.csv     amazon_reviews.csv    trends_*.csv      │
│  (8,807 rows)            (67,325 rows)         (1,771 rows)      │
└─────────┬─────────────────┬─────────────────┬────────────────────┘
          ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                     TRANSFORMATION                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │DuckDB SQL    │  │DuckDB/SQLite │  │pandas +      │           │
│  │· 10 queries  │  │· 10 queries  │  │  scipy       │           │
│  │· window fn   │  │· correlation │  │· peak detect │           │
│  │· UNNEST      │  │· seasonal    │  │· correlation │           │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘           │
└─────────┼─────────────────┼─────────────────┼────────────────────┘
          ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                     VISUALIZATION                                │
│  matplotlib · seaborn · Plotly                                   │
│  101 static figures + 8 interactive HTML dashboards              │
└─────────┬─────────────────┬─────────────────┬────────────────────┘
          ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                     DELIVERY                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │Streamlit     │  │Jupyter       │  │GitHub Pages  │           │
│  │Dashboard     │  │Notebooks     │  │Portfolio     │           │
│  │· 11 views    │  │· 3 per proj  │  │· 101 figs    │           │
│  │· live data   │  │· executed    │  │· 8 dash      │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

## Pipeline Details

### Netflix — Content Strategy

```
TMDB /discover (provider=8, flatrate, US)
    → fetch_tmdb_data.py (authenticated, rate-limited)
    → netflix_catalog.csv (7,498 rows)
    → DuckDB: window functions, UNNEST genres/countries
    → Matplotlib/Plotly: 30 figures + 8 interactive dashboards
    → Streamlit: 11-view dashboard
```

**Key design decision:** Used TMDB Discover API (not just Kaggle CSV) to get live popularity scores and upcoming release pipeline. This enables real-time genre opportunity scoring.

### Amazon — Review Intelligence

```
Stanford SNAP (reviews_Electronics_5.json.gz, 495MB)
    → fetch_amazon_data.py (streaming, 1/13 sample, seed=42)
    → amazon_reviews.csv (67,325 rows)
    → DuckDB/SQLite: brand ranking, helpfulness leaderboard, seasonal analysis
    → Matplotlib/Seaborn/Plotly: 49 figures
    → Streamlit: 6-view dashboard
```

**Key design decision:** Streaming download with deterministic sampling avoids loading 495MB into memory. Seed=42 makes the sample reproducible.

### Google — Search Trends

```
Google Trends (trendspy)
    → fetch_trends_data.py (14 keywords, 3 geo levels)
    → trends_*.csv (1,771 rows)
    → pandas + scipy: peak detection, correlation matrix
    → Plotly: 22 figures including choropleth maps
    → Streamlit: 4 executive views
```

**Key design decision:** trendspy (successor to archived pytrends) handles NID cookie warmup automatically. Multi-granularity alignment (worldwide → US → regional) required custom time-series merging.

## CI/CD Automation

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `execute-notebooks.yml` | Push/PR | Verifies all 9 notebooks execute without errors |
| `netflix-catalog.yml` | Daily cron | Refreshes TMDB catalog snapshot |
| `netflix-enrich.yml` | Weekly cron | Enrich Kaggle data with live TMDB metadata |
| `tmdb-refresh.yml` | Manual | On-demand refresh of trending/top-rated data |

## Environment

- **Python:** 3.11+
- **Memory:** 4GB RAM sufficient for all pipelines
- **Runtime:** ~2 minutes per project on standard laptop
- **Storage:** ~600MB total (mostly raw Amazon JSON.gz)
