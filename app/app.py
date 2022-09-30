import dash
from dash import Dash, html, Output, Input
from flask import Flask, session
from keycloak_middleware import KeycloakMiddleware
from keycloak import KeycloakOpenID

from components import *

server = Flask(__name__)
keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8080/",
    client_id="test_client",
    realm_name="KeyCloak",
    client_secret_key="xJWJXqD8ZMPZf04n6WEAaUWkgCqe2zKn",
)

server.wsgi_app = KeycloakMiddleware(server, keycloak_openid)

app = Dash(__name__, use_pages=True, server=server)

app.layout = html.Div(
    children=[
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
