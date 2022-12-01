import pandas as pd

from app.data.get_data import create_db_connection

QUERY = "SELECT * FROM public.mpam_due_cases"

def get_mpam_due_cases():
    with create_db_connection as connection:
        data = pd.read_sql_query(QUERY, connection)

        return data