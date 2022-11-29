# Third party imports
from dash import html

decs_header = html.Header(
    role="banner",
    **{"data-module": "govuk-header"},
    children=[
        html.Div(
            className="decs-grid-row",
            style={
                "padding":"10px 1%",
            },
            children=[
                html.Div(
                    className="decs-grid-column-one-third",
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
                    className="decs-grid-column-one-third",
                    children=[
                        html.P(
                            className="govuk-body-l", 
                            style={
                                "margin":"7.5px 0px", 
                                "textAlign":"center",
                            },
                            children="DECS Reporting"
                        ),
                    ]
                ),
                html.Div(
                    className="decs-grid-column-one-third",
                    style={
                        "textAlign":"right",
                        "margin":"10px 0px"
                    },                    
                    children=[
                        html.A(
                            className="govuk-link govuk-body",
                            href="/login",
                            children="Sign out"
                        )
                    ]
                )
            ],
        ),
    ]
)
