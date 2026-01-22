import pandas as pd
import zipfile
import io
import requests


def load_ff_factors_monthly(start_year=2000):
    """
    Load Fama-French 3-factor monthly data directly from the official website.

    Returns
    -------
    pd.DataFrame
        Columns: ['Mkt-RF', 'SMB', 'HML', 'RF'] in decimal.
    """
    url = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip"

    r = requests.get(url)
    r.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        with z.open("F-F_Research_Data_Factors.csv") as f:
            ff = pd.read_csv(f, skiprows=3)

    # Find the end of the data table
    ff = ff[ff.iloc[:, 0].str.match(r"^\d{6}$", na=False)]

    ff.columns = ["Date", "Mkt-RF", "SMB", "HML", "RF"]
    ff["Date"] = pd.to_datetime(ff["Date"], format="%Y%m")
    ff.set_index("Date", inplace=True)

    ff = ff.astype(float) / 100.0
    ff = ff[ff.index.year >= start_year]

    return ff