from dash import html, callback, Input, Output

from app.components import auto_govuk_table

from app.pages.due_cases_comp.day_selector_row import day_selector_row
from app.pages.due_cases_comp.counting_section import counting_section
from app.data.MPAM.mpam_due_cases import get_mpam_due_cases, get_mpam_due_cases_aggregate

import datetime

cases_df = get_mpam_due_cases()
case_counts = get_mpam_due_cases_aggregate()

four_week_due_case_body = html.Div(
    children=[
        day_selector_row, 
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
                    id="table-section-test",
                    style={
                        "backgroundColor":"#fff",
                        "padding":"10px"
                    },
                    children=[
                        auto_govuk_table(cases_df.set_index("Due Date").loc[datetime.now():datetime.deltatime(weeks=4)], title="Case details", title_size="m")
                    ]
                )
            ]
        )
    ]
)

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
