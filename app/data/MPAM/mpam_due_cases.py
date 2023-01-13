import os

import pandas as pd
import datetime

from app.data.create_db_connection import create_db_connection

MPAM_DUE_CASES_QUERY = "SELECT * FROM public.mpam_due_cases"
MPAM_DUE_CASES_AGGREGATE_QUERY = "SELECT * FROM public.mpam_due_cases_aggregate"

due_data = []
n_days = 10
base = pd.Timestamp.today()
timestamp_list = [base + datetime.timedelta(days=x) for x in range(n_days)]
for x in timestamp_list:
    due_data.append(x)


def get_mpam_due_cases():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        data = pd.read_csv("./data/MPAM/mocks/mpam_due_cases_mock.csv")
        # Overwriting due date with code to ensure data fits report timeframe.
        data["Due Date"] = due_data
    else:
        with create_db_connection() as connection:
            data = pd.read_sql_query(MPAM_DUE_CASES_QUERY, connection)

    data["Due Date"] = pd.to_datetime(data["Due Date"]).dt.date
    return data


def get_mpam_due_cases_aggregate():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        data = pd.read_csv("./data/MPAM/mocks/mpam_due_cases_aggregate_mock.csv")
    else:
        with create_db_connection() as connection:
            data = pd.read_sql_query(MPAM_DUE_CASES_AGGREGATE_QUERY, connection)

    # This data should only ever be a single row. Squeezing dataframe into a series.
    return data.squeeze()
