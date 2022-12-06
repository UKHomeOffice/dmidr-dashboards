from dash import html
import pandas as pd

from app.components import auto_govuk_table
from app.data.MPAM.mpam_open_cases import get_mpam_open_cases

open_cases_df = get_mpam_open_cases()

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
            open_cases_df.drop("Outside Service Standard", axis=1),
            title="Open Cases",
            title_size="m",
            bold_lead=True,
            hidden_lead_head=True,
        ),
    ],
)
