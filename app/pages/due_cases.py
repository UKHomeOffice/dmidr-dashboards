import dash
import pandas as pd
from dash import html, dcc

from app.components import *
from app.pages.due_cases_comp import *

import datetime

COLUMN_ORDER = ["CTSRef", "Workflow", "Directorate", "Signee", "Business Area", "Stage", "Current Handler User Id", "Due Date"]


def filter_due_cases_4_weeks(cases_df):
    today = datetime.datetime.now().date()
    # ToDo: James M. Feedback: Update to look at following 3 weeks, starting from the next monday
    cases_df_4_week_mask = (cases_df['Due Date'] > today) & (cases_df['Due Date'] < today + datetime.timedelta(weeks=4))
    cases_df_4_week = cases_df.loc[cases_df_4_week_mask]
    return cases_df_4_week[COLUMN_ORDER]


def filter_this_weeks_due_cases(cases_df):
    dt = datetime.datetime.now().date()
    start = dt - datetime.timedelta(days=dt.weekday())
    end = start + datetime.timedelta(days=6)
    filter_mask = (cases_df['Due Date'] >= start) & (cases_df['Due Date'] <= end)
    cases_df = cases_df[filter_mask]
    return cases_df[COLUMN_ORDER]


def filter_dates_out_of_service(cases_df):
    cases_df_out_of_service = cases_df[(cases_df["Due Date"] < datetime.datetime.now().date())]
    return cases_df_out_of_service[COLUMN_ORDER]


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
                        mpam_due_cases(filter_this_weeks_due_cases, True, "")
                    ]
                ),
                dcc.Tab(
                    label="Cases due in next 4 weeks",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                    children=[
                        mpam_due_cases(filter_due_cases_4_weeks, False, "four-week-")
                    ]
                ),
                dcc.Tab(
                    label="Out of service standard cases",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                    children=[
                        mpam_due_cases(filter_dates_out_of_service, False, "out-service-")
                    ]
                )
            ]
        ),
    ]
)