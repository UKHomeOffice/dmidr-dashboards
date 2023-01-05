import dash
from dash import html, dcc

from data.MPAM.mpam_performance_cases import (
    get_mpam_performance_cases,
    get_mpam_performance_by_date,
)
from app.pages.performance_cases import *
from app.pages.report_base import report_base
from app.components import grouped_histogram


dash.register_page(
    __name__, 
    name="Performance summary",
    path="/performance-summary"
)

layout = report_base(
    "Performance Summary",
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
                plot_title="Performance",
                y_axis_title="Due cases vs on time",
                x_axis_title="Days"
            )
        ),
        html.Div(
            className="decs-grid-row",
            style={
                "padding": "0px 15px"
            },
            children=performance_table(get_mpam_performance_cases()),
        ),
    ]
)