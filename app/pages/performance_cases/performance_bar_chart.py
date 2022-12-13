from dash import html, dcc
import pandas as pd

import plotly.express as px

import datetime


def performance_bar_func(unit_df):
    performance_bar = html.Div(
        children=[
            dcc.Graph(
                figure={
                    "data": [
                        {
                            "x": unit_df["date"],
                            "y": unit_df["Answered on time"],
                            "type": "bar",
                            "name": "Answered on time",
                            "marker": {"color": "#1d70b8"},
                        },
                        {
                            "x": unit_df["date"],
                            "y": unit_df["Due"],
                            "type": "bar",
                            "name": "Due",
                            "marker": {"color": "#4c2c92"},
                        },
                                                {
                            "x": unit_df["date"],
                            "y": unit_df["Performance"],
                            "type": "line",
                            "name": "performance",
                            "marker": {"color": "#4c2c92"},
                        },
                    ],
                    "layout": {
                        "title": "Cases due vs day",
                        "xaxis": {"title": "Days", "showgrid": "False"},
                        "yaxis": {"title": "Due cases vs on times",},
                    },
                }
            )
        ]
    )
    return performance_bar