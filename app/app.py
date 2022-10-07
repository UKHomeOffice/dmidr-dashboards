import dash
from dash import Dash, html, callback, Output, Input
from flask import Flask, session
import os

from components import *

server = Flask(__name__)

if os.environ.get("STAGE") == "PRODUCTION":
    from flask_keycloak.core import FlaskKeycloak

    config_path = os.path.join(os.path.dirname(__file__), "authentication/keycloak.json")
    FlaskKeycloak.from_kc_oidc_json(server, config_path=config_path)

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


if __name__ == "__main__":
    app.run_server(debug=True)
