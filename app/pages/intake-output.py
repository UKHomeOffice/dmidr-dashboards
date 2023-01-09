import dash
from dash import html, dcc

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

table_df = df.groupby(by="Business Area").agg("sum").reset_index()

histogram_df = df.groupby(by="Date").agg("sum").reset_index()

import plotly.graph_objects as go

fig = go.Figure(
    data=[
        go.Bar(
            name="Total Created",
            x=histogram_df["Date"],
            y=histogram_df["Total Created"],
            offsetgroup=0,
            marker_color='#8F23B3',
        ),
        go.Bar(
            name="Total Received",
            x=histogram_df["Date"],
            y=histogram_df["Total Received"],
            offsetgroup=0,
            base=histogram_df["Total Created"],
            marker_color='#A73379',
        ),
        go.Bar(
            name="Total Completed",
            x=histogram_df["Date"],
            y=histogram_df["Total Completed"],
            offsetgroup=1,
            marker_color='#54C1FF',
        ),
        go.Bar(
            name="Total Responded",
            x=histogram_df["Date"],
            y=histogram_df["Total Responded"],
            offsetgroup=1,
            base=histogram_df["Total Completed"],
            marker_color='#4E75FF',
        )
    ],
    layout=go.Layout(
        yaxis_title="Intake and output",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=0.4
        )
    )
)

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