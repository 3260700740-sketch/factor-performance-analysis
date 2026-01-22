import matplotlib.pyplot as plt
from pathlib import Path


def plot_curves(curves, save_path=None):
    plt.figure(figsize=(11, 6))
    for col in curves.columns:
        plt.plot(curves.index.astype(str), curves[col], label=col)

    plt.title("Factor Cumulative Return vs Market (Monthly)")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.tight_layout()

    if save_path is not None:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=150)

    plt.show()


def plot_ic_decay(ic_series, save_path=None):
    plt.figure(figsize=(8, 5))
    plt.plot(ic_series.index, ic_series.values, marker="o")
    plt.axhline(0.0, color="black", linestyle="--", linewidth=1)

    plt.title("IC Decay (Spearman Rank Correlation)")
    plt.xlabel("Prediction Horizon (Months)")
    plt.ylabel("Information Coefficient")
    plt.tight_layout()

    if save_path is not None:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=150)

    plt.show()


def plot_sector_exposure(sector_weights, save_path=None):
    plt.figure(figsize=(7, 7))
    sector_weights.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.ylabel("")
    plt.title("Sector Exposure")

    if save_path is not None:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=150)

    plt.tight_layout()
    plt.show()