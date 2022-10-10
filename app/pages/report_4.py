import dash 
from dash import html, dcc
from datetime import date

from components import *

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
                    selected_className="custom-tab--selected"
                ),
                dcc.Tab(
                    label="Cases due in next 4 weeks",
                    className="custom-tab",
                    selected_className="custom-tab--selected"
                ),
                dcc.Tab(
                    label="Out of service standard cases",
                    className="custom-tab",
                    selected_className="custom-tab--selected"
                )
            ]
        ), 
    ]
)