from dash import html, dcc
import plotly.graph_objects as go

example_gauge = dcc.Graph(
    figure=go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=270,
            domain={"x": [0, 1], "y": [0, 1]},
            title={"text": "Speed"},
        )
    )
)
