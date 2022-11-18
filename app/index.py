import dash
import psycopg2
from dash import Dash, html, callback, Output, Input
from flask import Flask, session
import os

from app.components import *

server = Flask(__name__)

if os.environ.get("STAGE") == "PRODUCTION":
    from authentication.auth_middleware import AuthMiddleware

    server.wsgi_app = AuthMiddleware(server)

app = Dash(__name__, use_pages=True, server=server)

app.layout = html.Div(
    id="main",
    children=[
        html.Span(id="login-status-text", children=[]),
        govuk_header,
        dash.page_container,
        govuk_footer,
    ]
)


# Need this callback to access the session.
# Probably can be done another way, but this is simple for now.
@callback(
    Output(component_id="login-status-text", component_property="children"),
    Input(component_id="main", component_property="children")
)
def login_status(value):
    if "userinfo" in session:
        return f"logged in as: {session['userinfo']['preferred_username']}"

    return "Not logged in"


def create_db_connection():
    return psycopg2.connect(
        host=os.environ.get(f"transformation_db_host"),
        user=os.environ.get(f"transformation_db_username"),
        password=os.environ.get(f"transformation_db_password"),
        database=os.environ.get(f"transformation_db_name"),
        port=int(os.environ.get(f"transformation_db_port"))
    )


def try_connection():
    print("Starting to connect to database.")
    try:
        with create_db_connection() as transform_connection:
            with transform_connection.cursor() as transform_cursor:
                transform_cursor.execute(
                    "SELECT * FROM information_schema.tables")
                row = transform_cursor.fetchone()
                if not row == None:
                    print("Connection to database successful.")
    except Exception as e:
        print("Connection to database failed, retrying.")
        raise Exception


try_connection()

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True, port=8050)
