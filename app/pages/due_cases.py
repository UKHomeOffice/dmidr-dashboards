import dash
import pandas as pd
from dash import html, dcc

from app.components import *
from app.pages.due_cases_comp import *

from app.data.MPAM.mpam_due_cases import get_mpam_due_cases

import datetime

def filter_due_cases_4_weeks():
    cases_df = get_mpam_due_cases()
    cases_df_4_week = cases_df.set_index("Due Date").loc[datetime.datetime.now().date():datetime.datetime.now().date() + datetime.timedelta(weeks=4)].reset_index()
    cases_df_4_week = cases_df_4_week[["CTSRef", "Workflow", "Directorate", "Signee", "Business Area", "Date on CTS", "Stage", "Current Handler", "Due Date"]]
    return auto_govuk_table(cases_df_4_week, title="Case details", title_size="m")

def filter_none_due_cases():
    cases_df = get_mpam_due_cases()
    cases_df = cases_df[["CTSRef", "Workflow", "Directorate", "Signee", "Business Area", "Date on CTS", "Stage", "Current Handler", "Due Date"]]
    return auto_govuk_table(cases_df, title="Case details", title_size="m")

def filter_dates_out_of_service():
    cases_df = get_mpam_due_cases()
    cases_df_out_of_service = cases_df[(cases_df["Due Date"] < pd.to_datetime(datetime.datetime.now().date()))]
    cases_df_out_of_service = cases_df_out_of_service[["CTSRef", "Workflow", "Directorate", "Signee", "Business Area", "Date on CTS", "Stage", "Current Handler", "Due Date"]]
    return auto_govuk_table(cases_df_out_of_service, title="Case details", title_size="m")


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
                        mpam_due_cases(filter_none_due_cases, True, "")
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
                    mpam_due_cases(filter_due_cases_4_weeks, False, "four-week-")
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
                        mpam_due_cases(filter_dates_out_of_service, False, "out-service-")
                    ]
                )
            ]
        ),
    ]
)