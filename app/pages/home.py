import dash

from dash import html

from app.components import board_link_card

dash.register_page(__name__, path="/")

layout = html.Div(
    style={
        "backgroundColor": "#f1f1f1",
        "paddingBottom":"20px"
    },
    children=[
        html.Hr(
            className="decs-section-break"
        ),
        html.Div(
            className="decs-grid-row",
            children=[
                html.Div(
                    style={
                        "margin":"3% 15% 10% 15%"
                    },
                    children=[
                        html.Div(
                            className="decs-grid-row",
                            style={"padding":"0px 15px"},
                            children=[
                                html.Span(
                                    className="govuk-caption-l",
                                    children="UKVI MPAM"
                                ),
                                html.H1(
                                    className="govuk-heading-l",
                                    children="DECS reporting home"
                                )
                            ]
                        ),
                        html.Div(
                            className="decs-grid-row",
                            children=[
                                board_link_card(dash_title="Open cases", dash_link="/open-cases"),
                                board_link_card(dash_title="Due cases", dash_link="/due-cases"),
                                board_link_card(dash_title="Closed cases", dash_link="/closed-cases"),
                            ]
                        ),
                        html.Div(
                            className="decs-grid-row",
                            style={"paddingTop":"15px"},
                            children=[
                                board_link_card(dash_title="Performance summary", dash_link="/performance-summary"),
                                board_link_card(dash_title="Intake and output", dash_link="/intake-output"),
                            ]
                        )
                    ]
                )
            ]
        )
    ],
)