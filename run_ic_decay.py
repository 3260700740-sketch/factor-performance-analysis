from src.data_loader import load_ff_factors_monthly
from src.ic_analysis import ic_decay
from src.visualization import plot_ic_decay

ff = load_ff_factors_monthly(start_year=2000)

ic_series = ic_decay(ff, max_horizon=12)
print(ic_series)

plot_ic_decay(
    ic_series,
    save_path="results/figures/ic_decay_smb.png"
)