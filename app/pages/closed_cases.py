import dash
import pandas as pd
from dash import html, dcc

from app.components import *
from app.pages.report_base import report_base
from app.data.MPAM.mpam_closed_cases import get_mpam_closed_cases_aggregate, get_mpam_closed_cases_by_age

dash.register_page(__name__, name="Closed cases", path="/closed-cases")

data = get_mpam_closed_cases_by_age()
data["binned_days"] = pd.cut(
    data["Age (days)"],
    bins=[0, 5, 10, 15, 20],
    labels=["0 to 5", "6 to 10", "11 to 15", "16 to 20"]
    )

def df_count_aggregation_by_column(column):
    return (
        data.groupby(column)
        .agg("sum")
        .reset_index()
    )

layout = report_base(
    title="Closed Cases",
    body=[
        html.Div(
            className="decs-grid-row",
            style={"padding": "0px 15px"},
            children=[
                html.Div(className="govuk-grid-column-one-third", children=pie_chart(df_count_aggregation_by_column("binned_days"), values_col="Total cases closed", names="binned_days", legend_title="Case age", pie_name="Cases by age",)),
                html.Div(className="govuk-grid-column-one-third", children=pie_chart(df_count_aggregation_by_column("binned_days"), values_col="Total cases closed", names="binned_days", legend_title="Case outcome", pie_name="Cases by outcome",)),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        counter(text="counter 1", count=10),
                        counter(text="counter 2", count=20),
                        counter(text="counter 3", count=30)
                    ],
                ),
            ],
        ),
        html.Div(
            className="decs-grid-row",
            style={"padding": "0px 15px"},
            children=barchart(x_data=data["Age (days)"], y_data=data["Total cases closed"]),
        ),
        html.Div(
            className="decs-grid-row", style={"padding": "0px 15px"}, children="table",
        ),
    ],
)
