from dash import html, dcc
import pandas as pd

import datetime

df = pd.DataFrame(
    data={
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "count_1": [2, 4, 6, 8, 10],
        "count_2": [2, 3, 4, 9, 11],
    }
)

def performance_bar_func(unit_df):
    df = pd.DataFrame(
    data={
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        }
    )
    week_day=datetime.datetime.now().isocalendar()[2]
    start_date=datetime.datetime.now() - datetime.timedelta(days=week_day)
    dates=[str((start_date + datetime.timedelta(days=i)).date()) for i in range(5)]
    print(dates)
    df["time"] = dates
    print(df["time"])
    performance_bar = html.Div(
        children=[
            dcc.Graph(
                figure={
                    "data": [
                        {
                            "x": df["day"] + " " + df["time"],
                            "y": unit_df["Answered on time"],
                            "type": "bar",
                            "name": "Answered on time",
                            "marker": {"color": "#1d70b8"},
                        },
                        {
                            "x": df["day"] + " " +  df["time"],
                            "y": unit_df["Due"],
                            "type": "bar",
                            "name": "Due",
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