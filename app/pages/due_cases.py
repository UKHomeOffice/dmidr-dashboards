import dash 
from dash import html, dcc

from components import *
from app.pages.operational_report import *

dash.register_page(
    __name__, 
    name="Due cases",
    path="/due-cases"
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