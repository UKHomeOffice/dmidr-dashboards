from dash import html
import pandas as pd

from components import auto_govuk_table

from .day_selector_row import day_selector_row
from .counting_section import counting_section

blanks = ["cell", "cell", "cell", "cell", "cell", "cell", "cell", "cell"]

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
        "Case SLA Date":blanks,
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