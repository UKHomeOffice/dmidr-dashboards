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
