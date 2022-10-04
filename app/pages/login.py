import dash

from dash import html, dcc, callback
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

from authentication.keycloak_auth import KeycloakAuth
from urllib.parse import parse_qs

dash.register_page(__name__, path="/login")

layout = html.Div(
    className="govuk-grid-row",
    children=[
        dcc.Location(id="url", pathname="/login"),
        html.Div(
            className="govuk-grid-column-one-third",
            children=[
                html.H1(
                    className="govuk-heading-l", 
                    children="Sign in with..."
                ),
                html.Div(
                    className="govuk-button-group",
                    children=[
                        html.Button(
                            className="govuk-button",
                            children="POISE",
                        ),
                        html.Button(
                            className="govuk-button",
                            children="DECS Admin",
                        ),
                    ]
                ),
                html.Div(
                    className="govuk-form-group",
                    children=[
                        html.Label(
                            className="govuk-label govuk-label--m", 
                            children="Username or email"
                        ),
                        dcc.Input(
                            id="username",
                            className='govuk-input govuk-input--width-20',
                            type="text", 
                            placeholder="Enter Username",
                        ),
                    ]
                ),
                html.Div(
                    className="govuk-form-group",
                    children=[
                        html.Label(
                            className="govuk-label govuk-label--m", 
                            children="Password"
                        ),
                        dcc.Input(
                            id="password",
                            className='govuk-input govuk-input--width-20',
                            type="text", 
                            placeholder="Enter Password",
                        ),
                    ]
                ),
                html.Div(
                    className="govuk-button-group",
                    children=[
                        html.Button(
                            className="govuk-button",
                            children="Continue",
                            id="verify",
                        ),
                        html.A(
                            className="govuk-link",
                            children="Cancel",
                            href="/"
                        )
                    ]
                ),
            ]
        ),
        html.Div(id="login_error", children=[]),
    ]
)


@callback(
    [
        Output(component_id="url", component_property="pathname"), 
        Output(component_id="login_error", component_property="children")
    ],
    [
        Input(component_id="verify", component_property="n_clicks")
    ],
    [
        State(component_id="username", component_property="value"), 
        State(component_id="password", component_property="value"), 
        State(component_id="url", component_property="search")
    ],
)
def update_output(n_clicks, username, password, querystring):
    if n_clicks is None:
        raise PreventUpdate
    else:
        keycloak_auth = KeycloakAuth()

        auth_error = keycloak_auth.login(username, password)

        if auth_error:
            return "/login", auth_error

        redirect = "/"

        if querystring:
            params = parse_qs(querystring.replace("?", ""))
            redirect = params["redirect"][0]

        return redirect, None
