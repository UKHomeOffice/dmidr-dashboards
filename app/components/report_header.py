from dash import html
from datetime import date

today = date.today()

def report_header(report_title: str, todays_date=today):
    return html.Div(
        className="decs-grid-row",
        children=[
            html.Div(
                className="decs-grid-column-three-quarters",
                children=[
                    html.H3(
                        className="govuk-heading-l",
                        children=f"{report_title}",
                    ),
                ],
            ),
            html.Div(
                className="decs-grid-column-one-quarter",
                style={
                    "textAlign":"right"
                },
                children=[
                    html.Span(
                        className="govuk-caption-s tab-date-caption",
                        children="Todays date",
                    ),
                    html.H3(
                        className="govuk-heading-s",
                        children=f"{todays_date.strftime('%A %d %B %Y')}",
                    ),
                ],
            ),
        ],
    )
