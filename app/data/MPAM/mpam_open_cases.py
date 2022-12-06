import pandas as pd


open_cases_df = pd.read_csv(
    "app/data/MPAM/mpam_open_cases_mock.csv"
)
open_cases_df["open_date"] = pd.to_datetime(open_cases_df["open_date"], dayfirst=True)
