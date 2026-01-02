"""
segmentation.py

This module assigns business-friendly customer segments
based on aggregated RFM scores.

Segmentation Strategy:
- Segment A → High-value customers (Top 25%)
- Segment B → Medium-value customers
- Segment C → Low-value / at-risk customers

Used for:
- Marketing targeting
- Customer retention strategies
- Revenue analysis
"""

import pandas as pd


def label_customers(rfm_scored: pd.DataFrame) -> pd.DataFrame:
    """
    Assign customer segments based on RFM score distribution.

    Segmentation Logic:
    - Segment A: Top 25% of customers (highest RFM scores)
    - Segment B: Middle group
    - Segment C: Bottom 40% (low value or inactive)

    Parameters
    ----------
    rfm_scored : pd.DataFrame
        DataFrame containing:
        - R_Score
        - F_Score
        - M_Score

    Returns
    -------
    pd.DataFrame
        DataFrame with:
        - RFM_Total
        - Segment label (A / B / C)
    """

    df = rfm_scored.copy()

    # Calculate total RFM score
    df["RFM_Total"] = df["R_Score"] + df["F_Score"] + df["M_Score"]

    # Quantile thresholds
    q75 = df["RFM_Total"].quantile(0.75)  # Top 25%
    q40 = df["RFM_Total"].quantile(0.40)  # Bottom 40%

    # Default segment
    df["Segment"] = "B"

    # Assign segments
    df.loc[df["RFM_Total"] >= q75, "Segment"] = "A"
    df.loc[df["RFM_Total"] <= q40, "Segment"] = "C"

    return df



# Optional test run (for development use only)
if __name__ == "__main__":
    from scoring import score_rfm
    from rfm_calculation import calculate_rfm
    from data_loading import load_transactions
    from preprocessing import clean_transactions

    df_raw = load_transactions("../data/raw/transactions.csv")
    df_clean = clean_transactions(df_raw)
    rfm = calculate_rfm(df_clean)
    scored = score_rfm(rfm)

    segmented = label_customers(scored)

    print("✅ Customer segmentation completed")
    print(segmented["Segment"].value_counts())
