import pandas as pd


def cumulative_curve(returns: pd.Series) -> pd.Series:
    """
    Convert a return series into a cumulative return curve.
    """
    return (1 + returns).cumprod()


def build_return_curves(ff: pd.DataFrame) -> pd.DataFrame:
    """
    Build cumulative return curves for Market, SMB, and HML.

    Parameters
    ----------
    ff : pd.DataFrame
        Fama-French monthly factor data with columns:
        ['Mkt-RF', 'SMB', 'HML', 'RF']

    Returns
    -------
    pd.DataFrame
        Cumulative return curves.
    """
    curves = pd.DataFrame(index=ff.index)

    # Market total return (S&P 500 proxy)
    curves["Market"] = ff["Mkt-RF"] + ff["RF"]

    # Factor returns
    curves["SMB"] = ff["SMB"]
    curves["HML"] = ff["HML"]

    # Convert to cumulative returns
    curves = curves.apply(cumulative_curve)

    return curves

############################
def sector_exposure(weights: pd.Series, sector_map: pd.DataFrame) -> pd.Series:
    """
    Aggregate asset-level weights into sector-level exposure.

    Parameters
    ----------
    weights : pd.Series
        Index: ticker, Values: weights
    sector_map : pd.DataFrame
        Columns: ['ticker', 'sector']

    Returns
    -------
    pd.Series
        Sector-level weights
    """
    df = sector_map.copy()
    df = df.set_index("ticker")

    df["weight"] = weights
    df = df.dropna(subset=["weight"])

    return df.groupby("sector")["weight"].sum()