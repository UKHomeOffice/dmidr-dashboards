import psycopg2
import os

def create_db_connection():
    return psycopg2.connect(
        host=os.environ.get(f"transformation_db_host"),
        user=os.environ.get(f"transformation_db_username"),
        password=os.environ.get(f"transformation_db_password"),
        database=os.environ.get(f"transformation_db_name"),
        port=int(os.environ.get(f"transformation_db_port"))
    )


def get_mpam_due_cases():
    query = "SELECT * FROM public.mpam_due_cases_aggregate"

    with create_db_connection as connection:
        data = pd.read_sql_query(query, connection)

        return data
