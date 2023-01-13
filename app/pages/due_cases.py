import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd

from app.pages.report_base import report_base
from app.components import auto_govuk_table


from app.pages.due_cases_comp.day_selector_row import day_selector_row_func
from app.pages.due_cases_comp.counting_section import counting_section

from app.data.MPAM.mpam_due_cases import (
    get_mpam_due_cases,
    get_mpam_due_cases_aggregate,
)

import datetime

case_counts = get_mpam_due_cases_aggregate()

COLUMN_ORDER = [
    "CTSRef",
    "Workflow",
    "Directorate",
    "Signee",
    "Business Area",
    "Stage",
    "Current Handler User Id",
    "Due Date",
]


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
    controls=[
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
            className="tab-controls",
            children=[
                html.Span(
                    className="govuk-body-l",
                    style={"marginBottom": "0px"},
                    children=[
                        html.Span(id="control-items", children=day_selector_row_func),
                    ],
                )
            ],
        ),
    ],
    body=[
        html.Div(
            id="page-content",
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className="decs-grid-row",
                            style={"marginBottom": "30px",},
                            children=[
                                counting_section(
                                    "Total due cases",
                                    bold_section="this week",
                                    count=case_counts["Total due this week"],
                                ),
                                counting_section(
                                    "Total due cases",
                                    bold_section="next 4 weeks",
                                    count=case_counts["Total due next 4 weeks"],
                                ),
                                counting_section(
                                    "Total due cases",
                                    bold_section="out of service standard",
                                    count=case_counts["Total out of service standard"],
                                ),
                                counting_section(
                                    "Total due cases",
                                    bold_section="all time",
                                    count=case_counts["Total cases"],
                                ),
                            ],
                        ),
                        html.Div(
                            className="decs-grid-row",
                            style={"padding": "0px 15px"},
                            children=[
                                html.Div(
                                    id="table-section",
                                    style={
                                        "backgroundColor": "#fff",
                                        "padding": "10px",
                                    },
                                    children=[]
                                )
                            ],
                        ),
                    ]
                ),
            ],
        ),
    ],
)


@callback(
    Output(component_id="control-items", component_property="style"),
    Input(component_id="report-tabs", component_property="value"),
)
def update_controls(selected_tab):
    style = None
    if not selected_tab == "tab-1":
        style = {"display": "none"}

    return style


@callback(
    Output(component_id="table-section", component_property="children"),
    [
        Input(component_id="report-tabs", component_property="value"),
        Input(component_id="week-day-store", component_property="data"),
    ],
)
def tab_selected(selected_tab, day_filter):

    if selected_tab == "tab-1":
        df = filter_this_weeks_due_cases()
        if day_filter:
            df = df.loc[df["Day"] == day_filter]
    elif selected_tab == "tab-2":
        df = filter_due_cases_4_weeks()
    elif selected_tab == "tab-3":
        df = filter_dates_out_of_service()

    return auto_govuk_table(df[COLUMN_ORDER], title="Case details", title_size="m",)
