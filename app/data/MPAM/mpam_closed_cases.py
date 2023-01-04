import os

import pandas as pd

from app.data.create_db_connection import create_db_connection

MPAM_CLOSED_CASES_AGGREGATE = "SELECT * FROM public.mpam_aggregate_closed_cases"
MPAM_CLOSED_CASES_BY_AGE = "SELECT * FROM public.mpam_aggregate_closed_cases_by_age"
MPAM_CLOSED_CASES_BY_OUTCOME = "SELECT * FROM public.mpam_aggregate_closed_cases_by_age"


def get_mpam_closed_cases_aggregate():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return pd.read_csv("./data/MPAM/mocks/mpam_closed_cases_aggregate_mock.csv")

    with create_db_connection() as connection:
        data = pd.read_sql_query(MPAM_CLOSED_CASES_AGGREGATE, connection)
        return data


def get_mpam_closed_cases_by_age():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return pd.read_csv("data/MPAM/mocks/mpam_closed_cases_aggregate_by_age_mock.csv")

    with create_db_connection() as connection:
        data = pd.read_sql_query(MPAM_CLOSED_CASES_BY_AGE, connection)
        return data
