"""
visualization.py

This module handles all visualization tasks for the RFM analysis project.

It generates:
- Distribution plots for Recency, Frequency, and Monetary values
- Customer segment distribution chart

All plots are saved to disk and used in reports or presentations.
"""

import os
import matplotlib.pyplot as plt
import pandas as pd


def plot_distribution(series: pd.Series, title: str, xlabel: str, output_path: str):
    """
    Plot and save a histogram for a given numeric feature.

    Parameters
    ----------
    series : pd.Series
        Data to plot.
    title : str
        Title of the chart.
    xlabel : str
        Label for X-axis.
    output_path : str
        Path where the image will be saved.
    """

    plt.figure()
    plt.hist(series, bins=30)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_segment_counts(df: pd.DataFrame, output_path: str):
    """
    Plot customer count per RFM segment.

    Parameters
    ----------
    df : pd.DataFrame
        RFM dataset with 'Segment' column.
    output_path : str
        File path to save the chart.
    """

    counts = df["Segment"].value_counts().sort_index()

    plt.figure()
    counts.plot(kind="bar")
    plt.title("Customer Segment Counts (A / B / C)")
    plt.xlabel("Segment")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def create_all_plots(df: pd.DataFrame, output_dir: str):
    """
    Generate all required plots for RFM analysis.

    Plots generated:
    - Recency distribution
    - Frequency distribution
    - Monetary distribution
    - Customer segment counts

    Parameters
    ----------
    df : pd.DataFrame
        Final RFM-labeled dataset.
    output_dir : str
        Directory where plots will be saved.
    """

    os.makedirs(output_dir, exist_ok=True)

    plot_distribution(
        df["Recency"],
        "Recency Distribution",
        "Recency (days)",
        f"{output_dir}/recency_distribution.png",
    )

    plot_distribution(
        df["Frequency"],
        "Frequency Distribution",
        "Frequency",
        f"{output_dir}/frequency_distribution.png",
    )

    plot_distribution(
        df["Monetary"],
        "Monetary Distribution",
        "Monetary Value",
        f"{output_dir}/monetary_distribution.png",
    )

    plot_segment_counts(
        df,
        f"{output_dir}/segment_counts.png",
    )


# -------------------------------------------------------
# Optional test run (for development use only)
# -------------------------------------------------------
if __name__ == "__main__":
    from data_loading import load_transactions
    from preprocessing import clean_transactions
    from rfm_calculation import calculate_rfm
    from scoring import score_rfm
    from segmentation import label_customers

    df_raw = load_transactions("../data/raw/transactions.csv")
    df_clean = clean_transactions(df_raw)
    rfm = calculate_rfm(df_clean)
    scored = score_rfm(rfm)
    labeled = label_customers(scored)

    create_all_plots(labeled, "../outputs/charts")

    print("✅ All visualizations generated successfully.")
