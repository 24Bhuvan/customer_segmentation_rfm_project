"""
scoring.py

This module converts RFM values into standardized RFM scores
using percentile-based ranking.

The scores are used for:
- Customer segmentation
- Behavioral analysis
- Marketing strategy development
"""

import pandas as pd
import numpy as np


def percentile_score(series: pd.Series, reverse: bool = False) -> pd.Series:
    """
    Convert a numeric series into percentile-based scores (1–4).

    Parameters
    ----------
    series : pd.Series
        Numeric values to be scored.
    reverse : bool, optional
        If True, lower values receive higher scores
        (used for Recency where lower = better).

    Returns
    -------
    pd.Series
        Integer scores ranging from 1 to 4.
    """

    pct = series.rank(method="average", pct=True)

    if reverse:
        pct = 1 - pct

    return np.clip(np.ceil(pct * 4), 1, 4).astype(int)


def score_rfm(rfm_df: pd.DataFrame) -> pd.DataFrame:
    """
    Assign RFM scores to each customer.

    Scoring Logic:
    - Recency: lower days → higher score
    - Frequency: higher count → higher score
    - Monetary: higher spend → higher score

    Parameters
    ----------
    rfm_df : pd.DataFrame
        DataFrame containing RFM metrics.

    Returns
    -------
    pd.DataFrame
        RFM DataFrame with added:
        - R_Score
        - F_Score
        - M_Score
    """

    df = rfm_df.copy()

    df["R_Score"] = percentile_score(df["Recency"], reverse=True)
    df["F_Score"] = percentile_score(df["Frequency"])
    df["M_Score"] = percentile_score(df["Monetary"])

    return df



# Optional test run (for development use only)
if __name__ == "__main__":
    from rfm_calculation import calculate_rfm
    from data_loading import load_transactions
    from preprocessing import clean_transactions

    df_raw = load_transactions("../data/raw/transactions.csv")
    df_clean = clean_transactions(df_raw)
    rfm = calculate_rfm(df_clean)

    scored = score_rfm(rfm)

    print("✅ RFM scoring completed")
    print(scored.head())
