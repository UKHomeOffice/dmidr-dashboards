import dash

from dash import html

from .report_1 import *
from components import report_header

dash.register_page(
    __name__, 
    path="/live-cases",
    title="Live Cases",
    name="Live Cases"
)

layout = html.Div(
    className="report-background-box govuk-body",
    children=[
        html.Div(
            className="tab-controls",
            style={
                "borderTop":"1px solid #000"
            },
            children=[
                html.P(
                    className="govuk-body-l",
                    style={"marginBottom": "0px"},
                    children="Controls",
                )
            ],
        ),
        report_header(
            report_title="Open Cases"
        ),
        html.Div(
            className="govuk-grid-row",
            children=[
                html.Div(
                    className="govuk-grid-column-two-thirds",
                    children=[
                        html.Div(
                            className="govuk-grid-row",
                            children=[
                                html.Div(
                                    className="information-box",
                                    children=[
                                        html.Span(
                                            className="govuk-caption-m",
                                            children="When are tickets completed through the week",
                                        ),
                                        html.H3(
                                            className="govuk-heading-m",
                                            children="Ticket completion",
                                        ),
                                        example_bar
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            className="govuk-grid-row",
                            children=[
                                ticket_details_sec
                            ]
                        ),
                    ],
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        html.Div(
                            className="information-box",
                            children=[
                                html.Span(
                                    className="govuk-caption-m",
                                    children="All business targets",
                                ),
                                html.H3(
                                    className="govuk-heading-m",
                                    children="Performance",
                                ),
                                example_gauge,
                                performance_table_sec
                            ],
                        )
                    ],
                ),
            ],
        ),
    ],
)
