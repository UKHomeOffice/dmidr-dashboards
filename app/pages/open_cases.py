# Third party imports
import dash
from dash import html
import pandas as pd

# Project imports
from app.components import *
from app.pages.open_cases_comp import *
from app.pages.report_base import report_base
from app.data.MPAM.mpam_open_cases import get_mpam_open_cases

dash.register_page(
    __name__, 
    path="/open-cases",
    name="Open Cases"
)

open_cases_df = get_mpam_open_cases()

### Case age in days
open_cases_df["binned_days"] = pd.cut(
    open_cases_df["Age"],
    bins=[0, 5, 10, 15, 20],
    labels=["0 to 5", "6 to 10", "11 to 15", "16 to 20"],
)

def df_count_aggregation_by_column(column, outside_service_standard):
    df = open_cases_df[
        open_cases_df["Outside Service Standard"] == outside_service_standard
    ]

    return (
        df.groupby(column)
        .agg(count=pd.NamedAgg(column=column, aggfunc="count"))
        .reset_index()
    )


def df_business_area_by_age():
    age_counts_df = (
        open_cases_df.groupby(by="Business Area")["Age"]
        .value_counts()
        .unstack(level=1)
        .reset_index()
    )
    for col in age_counts_df.columns:
        age_counts_df = age_counts_df.rename(columns={col: f"{col} Days"})
    return age_counts_df.fillna(0)

layout = report_base(
    title="Open Cases",
    body=[
        html.Div(
            className="decs-grid-row",
            children=[
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        pie_chart(
                            df_count_aggregation_by_column(
                                "binned_days", outside_service_standard=False
                            ),
                            values_col="count",
                            names="binned_days",
                            pie_name="Cases within service standard by age range",
                            legend_title="Case age",
                        )
                    ],
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        pie_chart(
                            df_count_aggregation_by_column(
                                "Business Area", outside_service_standard=False
                            ),
                            values_col="count",
                            names="Business Area",
                            pie_name="Cases within service standard by business unit",
                            legend_title="Business unit",
                        )
                    ],
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        pie_chart(
                            df_count_aggregation_by_column(
                                "Stage", outside_service_standard=False
                            ),
                            values_col="count",
                            names="Stage",
                            pie_name="Cases within service standard by stage",
                            legend_title="Case stage"
                        )
                    ]
                ),
            ]
        ),
        html.Div(
            className="decs-grid-row",
            style={"padding": "0px 15px",},
            children=[
                barchart(
                    x_data=open_cases_df["Age"]
                    .loc[open_cases_df["Outside Service Standard"] == 0]
                    .value_counts()
                    .index,
                    y_data=open_cases_df["Age"]
                    .loc[open_cases_df["Outside Service Standard"] == 0]
                    .value_counts(),
                    plot_title="Cases with service standard by age",
                    x_axis_title="Case age [Days]",
                    y_axis_title="Open cases [count]"
                )
            ]
        ),
        html.Div(
            className="decs-grid-row",
            children=[
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        counter(text="Total open cases", count=open_cases_df.shape[0]),
                        counter(
                            text="Open cases inside of service",
                            count=open_cases_df.loc[
                                open_cases_df["Outside Service Standard"] == 0
                            ].shape[0],
                        ),
                        counter(
                            text="Open cases outside of service",
                            count=open_cases_df.loc[
                                open_cases_df["Outside Service Standard"] == 1
                            ].shape[0],
                        ),
                    ]
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        pie_chart(
                            df_count_aggregation_by_column(
                                "Business Area", outside_service_standard=False
                            ),
                            values_col="count",
                            names="Business Area",
                            pie_name="Cases outside of service standard by business unit",
                            legend_title="Business unit"
                        )
                    ]
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        pie_chart(
                            df_count_aggregation_by_column(
                                "Stage", outside_service_standard=True
                            ),
                            values_col="count",
                            names="Stage",
                            pie_name="Cases outside of service standard by stage",
                            legend_title="Case stage"
                        )
                    ]
                ),
            ]
        ), 
        html.Div(
            className="decs-grid-row",
            style={"padding": "0px 15px"},
            children=[auto_govuk_table(df_business_area_by_age(), bold_lead=True)],
        ),
    ],
)
