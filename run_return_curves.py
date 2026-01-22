from src.data_loader import load_ff_factors_monthly
from src.factor_returns import build_return_curves
from src.visualization import plot_curves

ff = load_ff_factors_monthly(start_year=2000)
curves = build_return_curves(ff)
plot_curves(curves, save_path="results/figures/factor_return_curves.png")