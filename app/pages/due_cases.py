import dash
from dash import html, dcc, callback, Input, Output

from app.components import *
from app.pages.due_cases_comp import *
from app.pages.report_base import report_base

from app.data.MPAM.mpam_due_cases import get_mpam_due_cases

import datetime


def filter_due_cases_4_weeks():
    cases_df = get_mpam_due_cases()
    today = datetime.datetime.now().date()
    # ToDo: James M. Feedback: Update to look at following 3 weeks, starting from the next Monday. This would
    # remove the need for a user to scroll past cases they can look at in this "Due this week" tab.
    cases_df_4_week_mask = (cases_df["Due Date"] > today) & (
        cases_df["Due Date"] < today + datetime.timedelta(weeks=4)
    )
    cases_df_4_week = cases_df.loc[cases_df_4_week_mask]
    return cases_df_4_week


def filter_this_weeks_due_cases():
    cases_df = get_mpam_due_cases()
    dt = datetime.datetime.now().date()
    start = dt - datetime.timedelta(days=dt.weekday())
    end = start + datetime.timedelta(days=6)
    filter_mask = (cases_df["Due Date"] >= start) & (cases_df["Due Date"] <= end)
    cases_df = cases_df[filter_mask]
    return cases_df


def filter_dates_out_of_service():
    cases_df = get_mpam_due_cases()
    cases_df_out_of_service = cases_df[
        (cases_df["Due Date"] < datetime.datetime.now().date())
    ]
    return cases_df_out_of_service


dash.register_page(__name__, name="Due cases", path="/due-cases")

layout = report_base(
    title="Due Cases",
    body=[
        dcc.Tabs(
            id="report-tabs",
            parent_className="custom-tabs",
            className="custom-tabs-container",
            children=[
                dcc.Tab(
                    label="Cases due this week",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Cases due in next 4 weeks",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Out of service standard cases",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
            ],
        ),
        html.Div(
            id="page-content",
            children=mpam_due_cases(filter_this_weeks_due_cases, True, ""),
        ),
    ],
)


@callback(
    Output(component_id="page-content", component_property="children"),
    Input(component_id="report-tabs", component_property="value"),
)
def tab_selected(selected_tab):
    if selected_tab == "tab-1":
        return mpam_due_cases(filter_this_weeks_due_cases, True, "")
    elif selected_tab == "tab-2":
        return mpam_due_cases(filter_due_cases_4_weeks, False, "four-week-")
    elif selected_tab == "tab-3":
        return mpam_due_cases(filter_dates_out_of_service, False, "out-service-")
