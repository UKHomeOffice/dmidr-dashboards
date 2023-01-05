import dash
from dash import html, dcc

from data.MPAM.mpam_performance_cases import (
    get_mpam_performance_cases,
    get_mpam_performance_by_date,
)
from app.pages.report_base import report_base
from app.components import grouped_histogram, auto_govuk_table


dash.register_page(
    __name__, 
    name="Intake and Output",
    path="/intake-output"
)

layout = report_base(
    "Intake and Output",
    body=[
        html.Div(
            className="decs-grid-row",
            style={
                "padding": "0px 15px"
            },
            children=grouped_histogram(
                get_mpam_performance_by_date(),
                x_cols="date",
                y_cols=["Amount Answered On Time", "Amount Due"],
                plot_title="Intake and Output",
                y_axis_title="Intake and Output",
                x_axis_title="Date"
            )
        ),
        html.Div(
            className="decs-grid-row",
            style={
                "padding": "0px 15px"
            },
            children=auto_govuk_table(
                get_mpam_performance_cases()[["Business Area", "Due", "Answered", "Completed in time", "Performance", "Unanswered"]],
                title="Performance details",
                title_size="m",
                bold_lead=True,
                hidden_lead_head=False,
            ),
        ),
    ]
)