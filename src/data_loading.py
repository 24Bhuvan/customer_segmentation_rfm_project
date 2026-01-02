"""
data_loading.py

This module handles loading raw transaction data and enforcing
basic data type consistency required for downstream analytics.

Responsibilities:
- Load transaction CSV files
- Convert columns to correct data types
- Return a clean pandas DataFrame

Used in:
- Data Cleaning
- RFM Analysis
- Customer Segmentation
"""

import pandas as pd


def load_transactions(file_path: str) -> pd.DataFrame:
    """
    Load transaction data from a CSV file and enforce correct data types.

    Parameters
    ----------
    file_path : str
        Path to the raw transactions CSV file.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with:
        - PurchaseDate converted to datetime
        - TransactionAmount converted to numeric
    """

    # Read CSV file
    df = pd.read_csv(file_path)

    # Convert data types
    df["PurchaseDate"] = pd.to_datetime(
        df["PurchaseDate"], errors="coerce"
    )

    df["TransactionAmount"] = pd.to_numeric(
        df["TransactionAmount"], errors="coerce"
    )

    return df


# Optional test run (for debugging / development only)
if __name__ == "__main__":
    sample_path = "../data/raw/transactions.csv"
    df = load_transactions(sample_path)

    print("Data Loaded Successfully")
    print(df.info())
    print(df.head())
