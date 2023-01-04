import dash
from dash import html, dcc

from data.MPAM.mpam_performance_cases import get_mpam_performance_cases, get_mpam_performance_by_date
from app.pages.performance_cases import *
from app.pages.report_base import report_base
from app.components import report_header


dash.register_page(
    __name__, 
    name="Performance summary",
    path="/performance-summary"
)

layout = report_base(title="Performance Summary",
                     body=[
                         html.Div(
                             className="decs-grid-row",
                             children=[
                                 html.Div(
                                     className="decs-grid-row",
                                     style={
                                         "padding": "0px 15px"
                                     },
                                     children=performance_bar(get_mpam_performance_by_date(), plot_title="Performance"),
                                 ),
                             ],
                         ),
                         html.Div(
                             className="decs-grid-row",
                             children=[
                                 html.Div(
                                     className="decs-grid-row",
                                     style={
                                         "padding": "0px 15px"
                                     },
                                     children=performance_table(get_mpam_performance_cases()),
                                 ),
                             ],
                         ),
                     ])
