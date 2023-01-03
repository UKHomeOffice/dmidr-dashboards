import plotly.express as px
from dash import html, dcc

def performance_bar(data, plot_title:str=None):
    fig = px.histogram(data, x="Date", y=["Amount Answered On Time", "Amount Due"], barmode='group', height=400)

    fig.update_layout(
        paper_bgcolor="#fff",
        plot_bgcolor="#fff",
        legend_title="",
        yaxis=dict(
            title="Due cases vs on time",
            linecolor="#c1c1c1",
            gridcolor="#c1c1c1"
        ),
        xaxis=dict(
            title="Days",
            linecolor="#c1c1c1",
        ),
        margin=dict(l=80, r=80, t=40, b=80),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=0.2
        )
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
            dcc.Graph(figure=fig)
        ]
    )
