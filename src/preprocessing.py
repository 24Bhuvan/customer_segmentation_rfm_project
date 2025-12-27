import pandas as pd


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean transaction data for RFM analysis.
    """
    df = df.copy()

    # Drop missing critical fields
    df = df.dropna(subset=["CustomerID", "PurchaseDate"])

    # Remove zero or negative amounts
    df = df[df["TransactionAmount"] > 0]

    # Remove duplicate orders
    df = df.drop_duplicates(subset="OrderID")

    return df


def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save cleaned transactions to CSV.
    """
    df.to_csv(output_path, index=False)
