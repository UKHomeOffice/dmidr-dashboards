from dash import html, dcc
import pandas as pd

df = pd.DataFrame(
    data={
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "count_1": [2, 4, 6, 8, 10],
        "count_2": [2, 3, 4, 9, 11],
    }
)

performance_bar = html.Div(
    children=[
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df["day"],
                        "y": df["count_1"],
                        "type": "bar",
                        "name": "Answered on time",
                        "marker": {"color": "#1d70b8"},
                    },
                    {
                        "x": df["day"],
                        "y": df["count_2"],
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