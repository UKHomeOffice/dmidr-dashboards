import dash

from dash import html, dcc

dash.register_page(__name__, path="/login")

layout = html.Div(
    style={"backgroundColor": "#f1f1f1", "padding": "20px 0px"},
    children=[
        html.Div(
            className="govuk-grid-row",
            children=[
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        html.Img(
                            className="ho-logo-image",
                            src="/assets/images/uk-home-office-logo.png",
                        ),
                        html.P(
                            className="ho-logo-text govuk-body-l", 
                            children="Home Office"
                        ),
                    ]
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    style={
                        "verticalAlign":"middle"
                    },
                    children=[
                        html.P(
                            className="ho-logo-text govuk-body-l", 
                            children="DECS Reporting"
                        ),
                    ]
                ), 
            ],
        ),
        html.Hr(
            className="decs-section-break"
        ), 
        html.Div(
            className="govuk-grid-row",
            style={
                "marginLeft":"10%",
                "marginTop":"60px",
                "marginBottom":"30px"
            },
            children=[
                html.H2(
                    className="govuk-heading-m",
                    children="Sign In"
                ),
                html.Div(
                    className="govuk-form-group",
                    children=[
                        html.Label(
                            className="govuk-label", 
                            children="Username or email address"
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
                            className="govuk-label", 
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
                        html.A(
                            className="govuk-button",
                            children="Sign in",
                            id="verify",
                            href="/"
                        ),
                    ]
                ),
                html.A(
                    className="govuk-link",
                    children="I have forgotten my password",
                    href="/"
                )
            ]
        )
    ],
)