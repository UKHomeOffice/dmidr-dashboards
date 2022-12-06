import dash
from dash import html, dcc

from app.components import *
from app.pages.due_cases_comp import *

dash.register_page(
    __name__, 
    name="Due cases",
    path="/due-cases"
)

layout = html.Div(
    className="report-background-box govuk-body",
    children=[
        html.Hr(
            className="decs-section-break"
        ),
        html.Div(
            style={"paddingLeft":"10px"},
            children=[
                html.A(
                    className="govuk-back-link govuk-link--no-underline govuk-!-font-size-19",
                    style={
                        "paddingLeft":"20px"
                    },
                    children="Back to home",
                    href="/"
                ),
            ]
        ),
        report_header("Due Cases"),
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
                        due_case_body
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
                    mpam_due_cases()
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
                    ]
                )
            ]
        ),
    ]
)