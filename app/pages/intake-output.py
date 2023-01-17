import dash
from dash import html, dcc
import plotly.graph_objects as go

from app.data.MPAM.mpam_intake_and_output import (
    get_mpam_intake_and_output,
)
from app.pages.report_base import report_base
from app.components import auto_govuk_table


dash.register_page(
    __name__, 
    name="Intake and Output",
    path="/intake-output"
)

df = get_mpam_intake_and_output()

table_df = df.groupby(by="Business Area").agg({
    "Total created": "sum",
    "Total received": "sum",
    "Total responded": "sum",
    "Total completed": "sum"
}).reset_index()
histogram_df = df.groupby(by="date").agg({
    "Total created": "sum",
    "Total received": "sum",
    "Total responded": "sum",
    "Total completed": "sum"
}).reset_index()


def figure_hover_text(value_title:str):
    return f"{value_title}:" + "%{y}<extra></extra>"

fig = go.Figure(
    data=[
        go.Bar(
            name="Total Created",
            x=histogram_df["date"],
            y=histogram_df["Total created"],
            offsetgroup=0,
            marker_color='#8F23B3',
            hovertemplate=figure_hover_text('Total Created')
        ),
        go.Bar(
            name="Total Received",
            x=histogram_df["date"],
            y=histogram_df["Total received"],
            offsetgroup=0,
            base=histogram_df["Total created"],
            marker_color='#A73379',
            hovertemplate=figure_hover_text('Total Received')
        ),
        go.Bar(
            name="Total Completed",
            x=histogram_df["date"],
            y=histogram_df["Total completed"],
            offsetgroup=1,
            marker_color='#54C1FF',
            hovertemplate=figure_hover_text('Total Completed')
        ),
        go.Bar(
            name="Total Responded",
            x=histogram_df["date"],
            y=histogram_df["Total responded"],
            offsetgroup=1,
            base=histogram_df["Total completed"],
            marker_color='#4E75FF',
            hovertemplate=figure_hover_text('Total Responded')
        )
    ],
    layout=go.Layout(
        yaxis_title="Intake and output",
        margin=dict(t=0, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
        )
    )
)

fig.update_yaxes(rangemode="tozero")
fig.update_layout(paper_bgcolor="#fff", plot_bgcolor="#fff")

layout = report_base(
    "Intake and Output",
    body=[
        html.Div(
            className="decs-grid-row",
            style={
                "padding": "0px 15px"
            },
            children=[
                html.Div(
                    style={"background":"#fff"},
                    children=[
                        html.H3(
                            className="govuk-heading-m",
                            style={
                                "padding":"15px",
                                "marginBottom":"0px"
                            },
                            children="Intake and Output by all Business Areas"
                        ),
                        dcc.Graph(figure=fig)
                    ]
                )
            ]
        ),
        html.Div(
            className="decs-grid-row",
            style={
                "padding": "0px 15px"
            },
            children=auto_govuk_table(
                table_df,
                title="Performance details",
                title_size="m",
                bold_lead=True,
                hidden_lead_head=False,
            ),
        ),
    ]
)