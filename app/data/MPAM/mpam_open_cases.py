import os

import pandas as pd

from app.data.create_db_connection import create_db_connection

MPAM_OPEN_CASES_QUERY = "SELECT * FROM public.mpam_open_cases"


def get_mpam_open_cases():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return pd.read_csv("data/MPAM/mocks/mpam_open_cases_mock.csv")

    with create_db_connection() as connection:
        data = pd.read_sql_query(MPAM_OPEN_CASES_QUERY, connection)

        return data
