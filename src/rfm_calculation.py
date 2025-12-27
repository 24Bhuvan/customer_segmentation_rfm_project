import pandas as pd


def calculate_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate Recency, Frequency, Monetary (RFM) values per customer.
    """
    reference_date = df["PurchaseDate"].max() + pd.Timedelta(days=1)

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
