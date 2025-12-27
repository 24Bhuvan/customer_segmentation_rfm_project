import pandas as pd


def label_customers(rfm_scored: pd.DataFrame) -> pd.DataFrame:
    """
    Label customers into A / B / C using quantiles
    to keep Segment A small and premium.
    """
    df = rfm_scored.copy()

    df["RFM_Total"] = df["R_Score"] + df["F_Score"] + df["M_Score"]

    # Quantile thresholds
    q75 = df["RFM_Total"].quantile(0.75)  # Top 25%
    q40 = df["RFM_Total"].quantile(0.40)  # Bottom 40%

    df["Segment"] = "B"
    df.loc[df["RFM_Total"] >= q75, "Segment"] = "A"
    df.loc[df["RFM_Total"] <= q40, "Segment"] = "C"

    return df
