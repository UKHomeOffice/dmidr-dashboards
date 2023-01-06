import dash
import pandas as pd
from dash import html, dcc

from app.components import *
from app.pages.report_base import report_base
from app.data.MPAM.mpam_closed_cases import (
    get_mpam_closed_cases_aggregate,
    get_mpam_closed_cases_by_age,
    get_mpam_closed_cases_by_outcome,
)

dash.register_page(__name__, name="Closed cases", path="/closed-cases")

count_data = get_mpam_closed_cases_aggregate()

data = get_mpam_closed_cases_by_age()
data["binned_days"] = pd.cut(
    data["Age (days)"],
    bins=[0, 5, 10, 15, 20],
    labels=["0 to 5", "6 to 10", "11 to 15", "16 to 20"],
)


def df_count_aggregation_by_column(column):
    return data.groupby(column).agg("sum").reset_index()


layout = report_base(
    title="Closed Cases",
    body=[
        html.Div(
            className="decs-grid-row",
            children=[
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=pie_chart(
                        df_count_aggregation_by_column("binned_days"),
                        values_col="Total cases closed",
                        names="binned_days",
                        legend_title="Case age",
                        pie_name="Cases by age",
                    ),
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=pie_chart(
                        df_count_aggregation_by_column("binned_days"),
                        values_col="Total cases closed",
                        names="binned_days",
                        legend_title="Case outcome",
                        pie_name="Cases by outcome",
                    ),
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        counter(
                            text="Total cases closed",
                            count=count_data["Total cases closed"][0],
                        ),
                        counter(
                            text="Cases closed inside of service standard",
                            count=count_data["Cases closed inside of service standard"][0],
                        ),
                        counter(
                            text="Cases closed outside of service standard",
                            count=count_data["Cases closed outside of service standard"][0],
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="decs-grid-row",
            style={"padding": "0px 15px"},
            children=barchart(
                x_data=data["Age (days)"], y_data=data["Total cases closed"]
            ),
        ),
        html.Div(
            className="decs-grid-row",
            style={"padding": "0px 15px"},
            children=auto_govuk_table(
                get_mpam_closed_cases_by_outcome(),
                title="Case outcomes by business unit",
                title_size="m",
                bold_lead=True,
                hidden_lead_head=True,
            ),
        ),
    ],
)
