"""
preprocessing.py

This module handles data cleaning and preparation for RFM analysis.

Responsibilities:
- Remove invalid or missing records
- Filter incorrect transaction values
- Remove duplicate transactions
- Save cleaned data for downstream processing

Used in:
- Data preprocessing pipeline
- RFM calculation
- Customer segmentation workflow
"""

import pandas as pd


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw transaction data before analysis.

    Cleaning steps:
    - Remove rows with missing CustomerID or PurchaseDate
    - Remove transactions with zero or negative amount
    - Remove duplicate orders

    Parameters
    ----------
    df : pd.DataFrame
        Raw transaction data.

    Returns
    -------
    pd.DataFrame
        Cleaned transaction dataset ready for analysis.
    """

    df = df.copy()

    # Drop records with missing critical fields
    df = df.dropna(subset=["CustomerID", "PurchaseDate"])

    # Remove invalid transaction amounts
    df = df[df["TransactionAmount"] > 0]

    # Remove duplicate orders
    df = df.drop_duplicates(subset="OrderID")

    return df


def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save cleaned transaction data to a CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned transaction data.
    output_path : str
        Destination path for the cleaned CSV file.
    """

    df.to_csv(output_path, index=False)



# Optional test run (for development use only)
if __name__ == "__main__":
    from data_loading import load_transactions

    df_raw = load_transactions("../data/raw/transactions.csv")
    df_clean = clean_transactions(df_raw)

    save_cleaned_data(df_clean, "../data/processed/cleaned_transactions.csv")

    print("✅ Data cleaned and saved successfully.")
