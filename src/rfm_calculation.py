"""
rfm_calculation.py

This module calculates RFM (Recency, Frequency, Monetary) metrics
from cleaned transaction data.

RFM is widely used for:
- Customer segmentation
- Identifying high-value customers
- Marketing and retention strategies
"""

import pandas as pd


def calculate_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate Recency, Frequency, and Monetary values per customer.

    Definitions:
    - Recency   : Days since the customer's last purchase
    - Frequency : Number of unique orders placed
    - Monetary  : Total spending amount

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned transaction dataset containing:
        - CustomerID
        - PurchaseDate
        - OrderID
        - TransactionAmount

    Returns
    -------
    pd.DataFrame
        RFM table with columns:
        - CustomerID
        - Recency
        - Frequency
        - Monetary
    """

    # Reference date for recency calculation
    reference_date = df["PurchaseDate"].max() + pd.Timedelta(days=1)

    # Calculate RFM metrics
    rfm = (
        df.groupby("CustomerID")
          .agg(
              Recency=("PurchaseDate", lambda x: (reference_date - x.max()).days),
              Frequency=("OrderID", "nunique"),
              Monetary=("TransactionAmount", "sum"),
          )
          .reset_index()
    )

    return rfm


# Optional test run (for development use only)

if __name__ == "__main__":
    from data_loading import load_transactions
    from preprocessing import clean_transactions

    df_raw = load_transactions("../data/raw/transactions.csv")
    df_clean = clean_transactions(df_raw)

    rfm_df = calculate_rfm(df_clean)

    print("✅ RFM calculation completed")
    print(rfm_df.head())
