import pandas as pd
import numpy as np
from scipy.stats import spearmanr


def compute_ic(factor: pd.Series, future_returns: pd.Series) -> float:
    """
    Compute Spearman rank IC between a factor and future returns.
    """
    common = pd.concat([factor, future_returns], axis=1).dropna()
    if common.shape[0] < 10:
        return np.nan
    ic, _ = spearmanr(common.iloc[:, 0], common.iloc[:, 1])
    return ic


def ic_decay(ff: pd.DataFrame, max_horizon: int = 12) -> pd.Series:
    """
    Compute IC decay for a given factor (SMB, HML) against future market returns.

    Parameters
    ----------
    ff : pd.DataFrame
        Fama-French monthly data.
    max_horizon : int
        Maximum prediction horizon in months.

    Returns
    -------
    pd.Series
        IC values indexed by horizon.
    """
    results = {}

    # Market total return as target
    market_ret = ff["Mkt-RF"] + ff["RF"]

    for h in range(1, max_horizon + 1):
        future_ret = market_ret.shift(-h)

        # Example: use SMB as factor
        ic_val = compute_ic(ff["SMB"], future_ret)
        results[h] = ic_val

    return pd.Series(results, name="IC")