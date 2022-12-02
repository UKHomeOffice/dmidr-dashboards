import dash
import psycopg2
from dash import Dash, html, callback, Output, Input
import os
from flask import Flask

from app.components import *

server = Flask(__name__)

app = Dash(__name__, use_pages=True, server=server)

app.layout = html.Div(
    id="main",
    children=[
        decs_header,
        dash.page_container,
        html.Span(id="login-status-text", children=[]),
        decs_footer
    ]
)


def create_db_connection():
    return psycopg2.connect(
        host=os.environ.get(f"transformation_db_host"),
        user=os.environ.get(f"transformation_db_username"),
        password=os.environ.get(f"transformation_db_password"),
        database=os.environ.get(f"transformation_db_name"),
        port=int(os.environ.get(f"transformation_db_port"))
    )


def try_connection():
    print("Attempting to connect to database.")
    try:
        with create_db_connection() as transform_connection:
            with transform_connection.cursor() as transform_cursor:
                transform_cursor.execute(
                    "SELECT * FROM public.mpam_due_cases_aggregate")
                rows = transform_cursor.fetchall()
                if not rows == None:
                    print("Connection to database successful.")
                    for row in rows:
                        print(row)
    except TypeError as e:
        print("No credentials provided")
    except Exception as e:
        print("Connection to database failed, retrying.")
        raise Exception


try_connection()

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True, port=8050)
