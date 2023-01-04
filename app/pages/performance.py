import dash
from dash import html, dcc

from data.MPAM.mpam_performance_cases import get_mpam_performance_cases, get_mpam_performance_by_date
from app.pages.performance_cases import *
from app.components import report_header


dash.register_page(
    __name__, 
    name="Performance summary",
    path="/performance-summary"
)

layout = html.Div(
    className="report-background-box govuk-body",
    children=[
        html.Hr(
            className="decs-section-break"
        ),
        html.Div(
            style={"paddingLeft": "10px"},
            children=[
                html.A(
                    className="govuk-back-link govuk-link--no-underline govuk-!-font-size-19",
                    style={
                        "paddingLeft": "20px"
                    },
                    children="Back to home",
                    href="/"
                ),
            ]
        ),
        html.Div(
                className="tab-controls",
                children=[
                    html.P(
                        className="govuk-body-l",
                        style={"marginBottom": "0px"},
                        children=[
                            "Controls",
                        ],
                    )
                ],
            ),
        report_header("Performance Summary"),
        html.Div(
            className="decs-grid-row",
            style={
                "padding": "0px 15px"
            },
            children=performance_bar(get_mpam_performance_by_date(), plot_title="Performance")
        ),
        html.Div(
            className="decs-grid-row",
            style={
                "padding": "0px 15px"
            },
            children=performance_table(get_mpam_performance_cases()),
        ),
    ]
),
