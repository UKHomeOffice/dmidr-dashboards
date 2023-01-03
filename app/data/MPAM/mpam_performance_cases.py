import os

import pandas as pd

from app.data.create_db_connection import create_db_connection

MPAM_PERFORMANCE_QUERY = "SELECT * FROM public.mpam_performance"
MPAM_PERFORMANCE_BY_DATE_QUERY = "SELECT * FROM public.mpam_performance_by_dates"


def get_mpam_performance_cases():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return pd.read_csv("data/MPAM/mocks/mpam_performance_mock.csv")

    with create_db_connection() as connection:
        data = pd.read_sql_query(MPAM_PERFORMANCE_QUERY, connection)

        return data

def get_mpam_performance_by_date():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return pd.read_csv("data/MPAM/mocks/mpam_performance_by_dates_mock.csv")

    with create_db_connection() as connection:
        data = pd.read_sql_query(MPAM_PERFORMANCE_BY_DATE_QUERY, connection)

        return data
