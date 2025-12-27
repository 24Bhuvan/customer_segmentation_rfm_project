import os
import matplotlib.pyplot as plt
import pandas as pd


def plot_distribution(series: pd.Series, title: str, xlabel: str, output_path: str):
    plt.figure()
    plt.hist(series, bins=30)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_segment_counts(df: pd.DataFrame, output_path: str):
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
