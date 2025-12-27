import pandas as pd


def load_transactions(file_path: str) -> pd.DataFrame:
    """
    Load transactions CSV and enforce correct data types.
    """
    df = pd.read_csv(file_path)

    # Convert data types
    df["PurchaseDate"] = pd.to_datetime(df["PurchaseDate"], errors="coerce")
    df["TransactionAmount"] = pd.to_numeric(df["TransactionAmount"], errors="coerce")

    return df
