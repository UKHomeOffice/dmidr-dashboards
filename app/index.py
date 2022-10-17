import dash
from dash import Dash, html, callback, Output, Input
from flask import Flask, session
import os

from components import *

server = Flask(__name__)

if os.environ.get("STAGE") == "PRODUCTION":
    from authentication.auth_middleware import AuthMiddleware

    server.wsgi_app = AuthMiddleware(server)

app = Dash(__name__, use_pages=True, server=server)

app.layout = html.Div(
    children=[
        html.Span(id="login-status-text", children=[]),
        govuk_header,
        html.Div(
            className="govuk-grid-row",
            style={"padding": "10px 2% 0% 2%"},
            children=[
                html.A(
                    className="govuk-link govuk-!-font-size-27",
                    style={"float": "left", "marginRight": "30px",},
                    children=f"{page['name']}",
                    href=page["relative_path"],
                )
                for page in dash.page_registry.values()
            ],
        ),
        dash.page_container,
        html.Div(id="main"),
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


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True, port=8050)
