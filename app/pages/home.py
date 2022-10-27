import dash

from dash import html, dcc

dash.register_page(__name__, path="/")

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
                html.Div(
                    className="govuk-grid-column-one-third",
                    style={
                        "textAlign":"right"
                    }
,                    children=[
                        html.A(
                            className="govuk-link govuk-body-l",
                            href="/login",
                            children="Sign out"
                        )
                    ]
                )
            ],
        ),
        html.Hr(
            className="decs-section-break"
        ), 
    ],
)