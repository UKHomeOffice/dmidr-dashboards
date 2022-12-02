import pandas as pd

from app.data.get_data import create_db_connection

MPAM_DUE_CASES_QUERY = "SELECT * FROM public.mpam_due_cases"
MPAM_DUE_CASES_AGGREGATE_QUERY = "SELECT * FROM public.mpam_due_cases_aggregate"


def get_mpam_due_cases():
        with create_db_connection() as connection:
            data = pd.read_sql_query(MPAM_DUE_CASES_QUERY, connection)

            return data


def get_mpam_due_cases_aggregate():
        with create_db_connection() as connection:
            data = pd.read_sql_query(MPAM_DUE_CASES_AGGREGATE_QUERY, connection)

            return data.squeeze()
