from dash import html, callback, Input, Output

from app.components import auto_govuk_table

from app.pages.due_cases_comp.day_selector_row import day_selector_row_func
from app.pages.due_cases_comp.counting_section import counting_section
from app.data.MPAM.mpam_due_cases import get_mpam_due_cases, get_mpam_due_cases_aggregate

cases_df = get_mpam_due_cases()
cases_df['Due Date'] = cases_df['Due Date'].dt.date
case_counts = get_mpam_due_cases_aggregate()

def mpam_due_cases(filter_func, week_day_select, prefix):
    mpam_due_cases_div = html.Div(
        children=[
            html.Div(
                className="tab-controls",
                children=[
                    html.P(
                        className="govuk-body-l",
                        style={"marginBottom": "0px"},
                        children=[
                            "Controls",
                            day_selector_row_func if week_day_select else None,
                        ],
                    )
                ],
            ),

            html.Div(
                className="decs-grid-row",
                style={
                    "marginBottom":"30px",
                },
                children=[
                    counting_section("Total due cases", bold_section="this week", count=case_counts["Total due this week"]),
                    counting_section("Total due cases", bold_section="next 4 weeks", count=case_counts["Total due next 4 weeks"]),
                    counting_section("Total due cases", bold_section="out of service standard", count=case_counts["Total out of service standard"]),
                    counting_section("Total due cases", bold_section="all time", count=case_counts["Total cases"]),
                ]
            ),
            html.Div(
                className="decs-grid-row",
                style={
                    "padding":"0px 15px"
                },
                children=[
                    html.Div(
                        id=prefix+"table-section-test",
                        style={
                            "backgroundColor":"#fff",
                            "padding":"10px"
                        },
                        children=[
                            auto_govuk_table(filter_func(cases_df), title="Case details", title_size="m")
                        ]
                    )
                ]
            )
        ]
    ) 
    return mpam_due_cases_div

@callback(
    Output(component_id="table-section-test", component_property="children"),
    Input(component_id="week-day-store", component_property="data"),
    prevent_initial_call=True
)
def filter_table_by_day(filter_day):
    if filter_day == None:
        return auto_govuk_table(cases_df, title="Case details", title_size="m")
    else:
        df_filtered = cases_df.loc[cases_df["Day"] == filter_day]
        return auto_govuk_table(df_filtered, title="Case details", title_size="m")