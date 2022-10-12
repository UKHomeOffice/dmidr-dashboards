from dash import html, dcc
import pandas as pd

df = pd.DataFrame(
    data={"count_1": [2, 4, 6, 8, 10, 4, 6, 2, 9, 7, 11, 3, 2, 9, 10, 4, 8, 1, 4, 5],}
)

example_case_count = html.Div(
    className="govuk-grid-row",
    style={"marginBottom": "30px"},
    children=[
        html.Div(
            className="information-box",
            children=[
                html.Span(
                    className="govuk-caption-m",
                    children="How long does it take to complete tickets",
                ),
                html.H3(className="govuk-heading-m", children="Ticket completion time"),
                dcc.Graph(
                    figure={
                        "data": [
                            {
                                "y": df["count_1"],
                                "type": "bar",
                                "name": "SF",
                                "marker": {"color": "#1d70b8"},
                            },
                        ],
                        "layout": {
                            "title": "Days taken to resolve case",
                            "xaxis": {"title": "Time to complete [days]",},
                            "yaxis": {"title": "Count",},
                        },
                    }
                ),
            ],
        )
    ],
)
