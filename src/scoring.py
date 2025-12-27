import pandas as pd
import numpy as np


def percentile_score(series: pd.Series, reverse: bool = False) -> pd.Series:
    pct = series.rank(method="average", pct=True)

    if reverse:
        pct = 1 - pct

    return np.clip(np.ceil(pct * 4), 1, 4).astype(int)


def score_rfm(rfm_df: pd.DataFrame) -> pd.DataFrame:
    df = rfm_df.copy()

    df["R_Score"] = percentile_score(df["Recency"], reverse=True)
    df["F_Score"] = percentile_score(df["Frequency"])
    df["M_Score"] = percentile_score(df["Monetary"])

    return df
