import dash
from dash import html, dcc

from data.MPAM.mpam_performance_cases import get_mpam_performance_cases
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
        html.Div(
            style={"paddingLeft":"10px"},
            children=[
                html.A(
                    className="govuk-back-link",
                    children="Back",
                    href="/"
                ),
            ]
        ),
        dcc.Tabs(
            parent_className="custom-tabs",
            className="custom-tabs-container",
            children=[
                dcc.Tab(
                    label="Report One",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                    children=[
                        html.Div(
                            className="tab-controls",
                            children=[
                                html.P(
                                    className="govuk-body",
                                    style={"marginBottom": "0px"},
                                    children="There is a date here: 10/02/2022",
                                )
                            ],
                        ),
                        report_header("Performance Summary"),
                        html.Div(
                            className="decs-grid-row",
                            children=[
                                html.Div(
                                    className="decs-grid-row",
                                    children=[
                                       performance_table_func(get_mpam_performance_cases())
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
    ],
)
