import plotly.graph_objects as go
from dash import html, dcc

def barchart(x_data, y_data, plot_title:str=None, x_axis_title:str=None, y_axis_title:str=None):
    bar_chart = go.Figure()
    bar_chart.add_trace(
        go.Bar(
            x=x_data,
            y=y_data,
            text=y_data,
            marker_color="#832CAD",
            textposition='outside', 
        )
    )

    bar_chart.update_layout(
        paper_bgcolor="#fff",
        plot_bgcolor="#fff",
        yaxis=dict(
            title=f"{y_axis_title if y_axis_title else y_data.name}",
            linecolor="#c1c1c1",
            gridcolor="#c1c1c1"
        ), 
        xaxis=dict(
            title=f"{x_axis_title if x_axis_title else x_data.name}",
            linecolor="#c1c1c1",
        ),
        margin=dict(l=80, r=80, t=40, b=80)
    )

    return html.Div(
        style={"background":"#fff"},
        children=[
            html.H3(
                className="govuk-heading-m", 
                style={
                    "padding":"15px",
                    "marginBottom":"0px"
                },
                children=plot_title
            ),
            dcc.Graph(figure=bar_chart)
        ]
    )
