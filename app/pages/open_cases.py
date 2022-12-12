# Third party imports
import dash
from dash import html
import pandas as pd
import datetime as dt

# Project imports
from app.components import *
from app.pages.open_cases_comp import *
from app.data.MPAM.mpam_open_cases import open_cases_df

dash.register_page(
    __name__, 
    path="/open-cases",
    name="Open Cases"
)

open_cases_df = open_cases_df

### Case age in days
today = dt.datetime.now()
open_cases_df["case_age"] = (today - open_cases_df["open_date"]).dt.days
open_cases_df["binned_days"] = pd.cut(
    open_cases_df["case_age"], 
    bins=[5, 10, 15, 20, 25, 30, 35],
    labels=["0 to 5", "6 to 10", "11 to 15", "16 to 20", "21 to 25", "26 to 30"]
    )


layout = html.Div(
    className="report-background-box govuk-body",
    children=[
        html.Hr(
            className="decs-section-break"
        ),
        html.Div(
            style={"paddingLeft":"10px"},
            children=[
                html.A(
                    className="govuk-back-link govuk-link--no-underline govuk-!-font-size-19",
                    style={
                        "paddingLeft":"20px"
                    },
                    children="Back to home",
                    href="/"
                ),
            ]
        ),
        report_header("Open Cases"),
        html.Div(
            className="decs-grid-row",
            children=[
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        decs_open_cases_pie(
                            open_cases_df, 
                            values_col="binned_days",
                            pie_name="Cases within service standard by age range",
                            legend_title="Case age"
                        )
                    ]
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        decs_open_cases_pie(
                            open_cases_df, 
                            values_col="unit",
                            pie_name="Cases within service standard by business unit",
                            legend_title="Business unit"
                        )
                    ]
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        decs_open_cases_pie(
                            open_cases_df, 
                            values_col="stage",
                            pie_name="Cases within service standard by stage",
                            legend_title="Case stage"
                        )
                    ]
                ),
            ]
        ),
        html.Div(
            className="decs-grid-row", 
            style={
                "padding":"0px 15px", 
                "margin":"15px 0px"
            },
            children=[
                open_cases_age_bar(
                    x_data=open_cases_df["case_age"].value_counts().index,
                    y_data=open_cases_df["case_age"].value_counts(),
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
                        html.Div(children=["Place holder"]),
                    ]
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        decs_open_cases_pie(
                            open_cases_df, 
                            values_col="stage",
                            pie_name="Cases outside of service standard by business unit",
                            legend_title="Business unit"
                        )
                    ]
                ),
                html.Div(
                    className="govuk-grid-column-one-third",
                    children=[
                        decs_open_cases_pie(
                            open_cases_df, 
                            values_col="stage",
                            pie_name="Cases outside of service standard by stage",
                            legend_title="Case stage"
                        )
                    ]
                ),
            ]
        ), 
        html.Div(
            className="decs-grid-row",
            children=[

            ]
        )
    ],
)
