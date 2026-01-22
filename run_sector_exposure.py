import pandas as pd
from src.visualization import plot_sector_exposure
from src.factor_returns import sector_exposure

# Example factor-based weights (illustrative)
weights = pd.Series(
    {
        "AAPL": 0.20,
        "MSFT": 0.20,
        "NVDA": 0.15,
        "JPM": 0.15,
        "BAC": 0.10,
        "XOM": 0.10,
        "CVX": 0.10,
    }
)

sector_map = pd.read_csv("data/processed/sector_map.csv")

sector_weights = sector_exposure(weights, sector_map)
print(sector_weights)

plot_sector_exposure(
    sector_weights,
    save_path="results/figures/sector_exposure.png"
)