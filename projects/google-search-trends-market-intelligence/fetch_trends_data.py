"""
Google Trends Data Fetcher (2026 Update)
=====================================
Rewritten from pytrends (archived April 2025) to trendspy (maintained successor).
Fetches interest over time, interest by region, and related queries
for tech, health, and finance topics.

Data Source: Google Trends via trendspy library (https://github.com/vassiliskrikonis/trendspy)
Also references BigQuery public dataset: bigquery-public-data.google_trends

Author: Sierra Napier | The Data Vigilante
"""
import os
import time
import pandas as pd
from trendspy import Trends
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize with longer request delay to avoid rate limits
# trendspy handles NID cookie warmup automatically
pytrends = Trends(request_delay=2.0)

# Categories of keywords to track
KEYWORD_GROUPS = {
    "tech": ["AI", "machine learning", "ChatGPT", "Bitcoin", "Tesla", "Netflix", "Amazon"],
    "health": ["telehealth", "mental health", "fitness"],
    "finance": ["inflation", "recession", "stock market", "crypto"],
}

ALL_KEYWORDS = [kw for group in KEYWORD_GROUPS.values() for kw in group]
TIMEFRAME = "today 5-y"  # Last 5 years
GEO_WORLDWIDE = ""
GEO_US = "US"


def fetch_interest_over_time(keywords, timeframe=TIMEFRAME, geo=GEO_WORLDWIDE, label="ww"):
    """Fetch interest-over-time for keywords via trendspy."""
    print(f"[FETCH] interest_over_time | keywords={keywords} | geo={geo or 'worldwide'} | tf={timeframe}")
    try:
        df = pytrends.interest_over_time(keywords, timeframe=timeframe)
        if df is None or df.empty:
            print(f"  ⚠️ Empty response for {keywords}")
            return None
        if "isPartial" in df.columns:
            df = df.drop(columns=["isPartial"])
        df["geo"] = geo or "worldwide"
        df["fetched_at"] = datetime.utcnow().isoformat()
        return df
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None


def fetch_interest_by_region(keyword, geo=GEO_US, label="us"):
    """Fetch interest by region for a single keyword."""
    print(f"[FETCH] interest_by_region | keyword={keyword} | geo={geo}")
    try:
        df = pytrends.interest_by_region(keyword, geo=geo)
        if df is None or df.empty:
            print(f"  ⚠️ Empty response for {keyword}")
            return None
        df = df.reset_index()
        df["keyword"] = keyword
        df["geo"] = geo
        df["fetched_at"] = datetime.utcnow().isoformat()
        return df
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None


def fetch_related_queries(keyword, geo=GEO_WORLDWIDE):
    """Fetch rising and top related queries for a keyword."""
    print(f"[FETCH] related_queries | keyword={keyword}")
    try:
        top_df, rising_df = pytrends.related_queries(keyword)
        if top_df is not None:
            top_df["keyword"] = keyword
            top_df["type"] = "top"
            top_df["fetched_at"] = datetime.utcnow().isoformat()
        if rising_df is not None:
            rising_df["keyword"] = keyword
            rising_df["type"] = "rising"
            rising_df["fetched_at"] = datetime.utcnow().isoformat()
        return top_df, rising_df
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None, None


def batch_fetch_interest_over_time(keywords, geo=GEO_WORLDWIDE, label="ww"):
    """Fetch in batches of 5 (Google Trends limit per payload)."""
    batches = [keywords[i : i + 5] for i in range(0, len(keywords), 5)]
    frames = []
    for batch in batches:
        df = fetch_interest_over_time(batch, geo=geo, label=label)
        if df is not None:
            frames.append(df)
        time.sleep(3)  # Rate limit politeness between batches
    if frames:
        return pd.concat(frames, axis=1)
    return None


def main():
    print("=" * 60)
    print("Google Trends Data Fetch — Real Data via trendspy")
    print("(Successor to pytrends, archived April 2025)")
    print("=" * 60)

    # 1. Interest over time — Worldwide
    print("\n--- 1. Interest Over Time (Worldwide) ---")
    df_ww = batch_fetch_interest_over_time(ALL_KEYWORDS, geo=GEO_WORLDWIDE, label="ww")
    if df_ww is not None:
        path = os.path.join(DATA_DIR, "interest_over_time_worldwide.csv")
        df_ww.to_csv(path)
        print(f"  Saved: {path} | shape={df_ww.shape}")

    # 2. Interest over time — US
    print("\n--- 2. Interest Over Time (US) ---")
    df_us = batch_fetch_interest_over_time(ALL_KEYWORDS, geo=GEO_US, label="us")
    if df_us is not None:
        path = os.path.join(DATA_DIR, "interest_over_time_us.csv")
        df_us.to_csv(path)
        print(f"  Saved: {path} | shape={df_us.shape}")

    # 3. Interest by region (US states) for each keyword
    print("\n--- 3. Interest By Region (US) ---")
    region_frames = []
    for kw in ALL_KEYWORDS:
        df = fetch_interest_by_region(kw, geo=GEO_US)
        if df is not None:
            region_frames.append(df)
        time.sleep(2)
    if region_frames:
        df_region = pd.concat(region_frames, ignore_index=True)
        path = os.path.join(DATA_DIR, "interest_by_region_us.csv")
        df_region.to_csv(path, index=False)
        print(f"  Saved: {path} | shape={df_region.shape}")

    # 4. Related queries (rising + top)
    print("\n--- 4. Related Queries (Rising + Top) ---")
    top_frames, rising_frames = [], []
    for kw in ALL_KEYWORDS:
        top_df, rising_df = fetch_related_queries(kw)
        if top_df is not None:
            top_frames.append(top_df)
        if rising_df is not None:
            rising_frames.append(rising_df)
        time.sleep(2)
    if top_frames:
        df_top = pd.concat(top_frames, ignore_index=True)
        path = os.path.join(DATA_DIR, "related_queries_top.csv")
        df_top.to_csv(path, index=False)
        print(f"  Saved: {path} | shape={df_top.shape}")
    if rising_frames:
        df_rising = pd.concat(rising_frames, ignore_index=True)
        path = os.path.join(DATA_DIR, "related_queries_rising.csv")
        df_rising.to_csv(path, index=False)
        print(f"  Saved: {path} | shape={df_rising.shape}")

    print("\n" + "=" * 60)
    print("Fetch complete. All data saved to ./data/")
    print("=" * 60)


if __name__ == "__main__":
    main()
