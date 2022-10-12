from dash import html, callback, Input, Output
import pandas as pd

from components import auto_govuk_table

from .day_selector_row import day_selector_row
from .counting_section import counting_section

blanks = ["cell", "cell", "cell", "cell", "cell", "cell", "cell", "cell"]
Days = ["Mon", "Mon", "Tues", "Wed", "Thurs", "Thurs", "Thurs", "Fri"]

df = pd.DataFrame(
    data={
        "Case reference":blanks,
        "Owning CSU":blanks,
        "Business Area":blanks,
        "Location":blanks,
        "NRO":blanks,
        "Case queue name":blanks,
        "UKBA recieved date":blanks,
        "Status":blanks,
        "Current handler name":blanks,
        "Day":Days,
    }
)

operational_report_body = html.Div(
    children=[
        day_selector_row, 
        html.Div(
            className="govuk-grid-row",
            style={"marginBottom":"30px"},
            children=[
                counting_section("Total due cases", bold_section="this week", count=34),
                counting_section("Total due cases", bold_section="next 4 weeks", count=186),
                counting_section("Total due cases", bold_section="out of service standard", count=114),
                counting_section("Total due cases", bold_section="all time", count=300),           
            ]
        ),
        html.Div(
            className="govuk-grid-row",
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
                        auto_govuk_table(df, title="Case details", title_size="m")
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
        return auto_govuk_table(df, title="Case details", title_size="m")
    else:
        df_filtered = df.loc[df["Day"] == filter_day]
        return auto_govuk_table(df_filtered, title="Case details", title_size="m")
