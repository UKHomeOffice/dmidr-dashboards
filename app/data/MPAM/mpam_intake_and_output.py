import os
import pandas as pd

from app.data.create_db_connection import create_db_connection

MPAM_INTAKE_OUTPUT_QUERY = "SELECT * FROM public.mpam_intake_and_output"


def get_mpam_intake_and_output():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return pd.read_csv("./data/MPAM/mocks/mpam_intake_output_mock.csv")

    with create_db_connection() as connection:
        data = pd.read_sql_query(MPAM_INTAKE_OUTPUT_QUERY, connection)

        return data
