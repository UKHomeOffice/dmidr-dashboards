import dash 
from dash import html, dcc

from components import *
from .operational_report import *

dash.register_page(
    __name__, 
    path="/operational-report",
    title="Operational Report",
    name="Operational Report"
)

layout = html.Div(
    className="report-background-box govuk-body", 
    children=[
        dcc.Tabs(
            parent_className="custom-tabs",
            className="custom-tabs-container",
            children=[
                dcc.Tab(
                    label="Cases due this week",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                    children=[
                        html.Div(
                            className="tab-controls",
                            children=[
                                html.P(
                                    className="govuk-body-l",
                                    style={"marginBottom": "0px"},
                                    children="Controls",
                                )
                            ],
                        ),
                        report_header("Cases due this week"),
                        operational_report_body
                    ]
                ),
                dcc.Tab(
                    label="Cases due in next 4 weeks",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                    children=[
                        html.Div(
                            className="tab-controls",
                            children=[
                                html.P(
                                    className="govuk-body-l",
                                    style={"marginBottom": "0px"},
                                    children="Controls",
                                )
                            ],
                        ),
                        report_header("Cases due in the next 4 weeks"),
                    ]
                ),
                dcc.Tab(
                    label="Out of service standard cases",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                    children=[
                        html.Div(
                            className="tab-controls",
                            children=[
                                html.P(
                                    className="govuk-body-l",
                                    style={"marginBottom": "0px"},
                                    children="Controls",
                                )
                            ],
                        ),
                        report_header("Out of service standard cases"),
                    ]
                )
            ]
        ), 
    ]
)