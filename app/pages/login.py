import dash

from dash import html, dcc, callback
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

from authentication.keycloak_auth import KeycloakAuth

dash.register_page(__name__, path="/login")

layout = html.Div(
    [
        dcc.Location(id="url", pathname="/login"),
        html.Div(
            dcc.Input(
                id="username",
                type="text",
                placeholder="Enter Username",
                style={
                    "margin-left": "35%",
                    "width": "450px",
                    "height": "45px",
                    "padding": "10px",
                    "margin-top": "60px",
                    "font-size": "16px",
                    "border-width": "3px",
                    "border-color": "#a0a3a2",
                },
            ),
        ),
        html.Div(
            dcc.Input(
                id="password",
                type="text",
                placeholder="Enter Password",
                style={
                    "margin-left": "35%",
                    "width": "450px",
                    "height": "45px",
                    "padding": "10px",
                    "margin-top": "10px",
                    "font-size": "16px",
                    "border-width": "3px",
                    "border-color": "#a0a3a2",
                },
            ),
        ),
        html.Div(
            html.Button(
                "Verify",
                id="verify",
                style={"border-width": "3px", "font-size": "14px"},
            ),
            style={"margin-left": "45%", "padding-top": "30px"},
        ),
        html.Div(id="login_error", children=[]),
    ]
)


@callback(
    [Output("url", "pathname"), Output("login_error", "children")],
    [Input("verify", "n_clicks")],
    [State("username", "value"), State("password", "value")],
)
def update_output(n_clicks, username, password):
    if n_clicks is None:
        raise PreventUpdate
    else:
        keycloak_auth = KeycloakAuth()

        auth_error = keycloak_auth.login(username, password)

        if auth_error:
            return "/login", auth_error

        return "/", None
