from dash import html
import pandas as pd

from app.components import auto_govuk_table

blanks = [
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
]

unit_df = pd.DataFrame(
    data={
        "Unit": [
            "Unit 1",
            "Unit 2",
            "Unit 3",
            "Unit 4",
            "Unit 5",
            "Unit 6",
            "Unit 7",
            "Unit 8",
            "Unit 9",
            "Unit 10",
        ],
        "Due": blanks,
        "Awaiting QA": blanks,
        "Answered": blanks,
        "Answered on time": blanks,
        "Performance": blanks,
        "Unanswered": blanks,
    }
)

completion_time_table = html.Div(
    className="information-box",
    children=[
        html.Span(className="govuk-caption-m", children="Case response time details"),
        html.H3(className="govuk-heading-m", children="Time to completion details"),
        html.P(
            className="govuk-body",
            children="This would be a good place to describe the table and the purpose. If you were so inclined.",
        ),
        auto_govuk_table(
            unit_df,
            title="Open Cases",
            title_size="m",
            bold_lead=True,
            hidden_lead_head=True,
        ),
    ],
)
