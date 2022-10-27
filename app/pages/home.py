import dash

from dash import html
from components import board_link_card


dash.register_page(__name__, path="/")

layout = html.Div(
    style={
        "backgroundColor": "#f1f1f1",
        "paddingBottom":"20px"
    },
    children=[
        html.Div(
            className="govuk-grid-row",
            style={
                "padding":"10px 5px"
            },
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
                        "textAlign":"center"
                    },
                    children=[
                        html.H1(
                            className="govuk-heading-l", 
                            style={"margin":"0px"},
                            children="DECS Reporting"
                        ),
                    ]
                ), 
                html.Div(
                    className="govuk-grid-column-one-third",
                    style={
                        "textAlign":"right"
                    },                    
                    children=[
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
        html.Div(
            className="govuk-grid-row",
            children=[
                html.Div(
                    style={
                        "margin":"3% 15% 10% 15%"
                    },
                    children=[
                        html.Div(
                            className="govuk-grid-row",
                            style={"padding":"0px 15px"},
                            children=[
                                html.H1(
                                    className="govuk-heading-l",
                                    children="DECS reporting home"
                                )
                            ]
                        ),
                        html.Div(
                            className="govuk-grid-row",
                            children=[
                                board_link_card(dash_title="Open cases", dash_link="/open-cases"),
                                board_link_card(dash_title="Due cases", dash_link="/due-cases"),
                                board_link_card(dash_title="Closed cases", dash_link="/closed-cases"),
                            ]
                        ),
                        html.Div(
                            className="govuk-grid-row",
                            style={"paddingTop":"15px"},
                            children=[
                                board_link_card(dash_title="Performance summary", dash_link="/performance-summary"),
                                board_link_card(dash_title="Intake and output"),
                            ]
                        )
                    ]
                )
            ]
        )
    ],
)