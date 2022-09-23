# Third party imports
from dash import html

from .details_table import details_table

ticket_details_sec = html.Div(
    className="govuk-grid-column-two-thirds",
    children=[
        html.Div(
            className="information_box",
            children=[
                html.Span(
                    className="govuk-caption-m",
                    children="Breakdown of ticket responses"
                ),
                html.H3(
                    className="govuk-heading-m",
                    children="Ticket details"
                ), 
                html.P(
                    className="govuk-body",
                    children="This would be a good place to describe the table and the purpose. If you were so inclined."
                ),
                details_table, 
                html.P(
                    className="govuk-body",
                    children="Usually I guess there would be some more text here. Suspendisse potenti. Proin aliquet mi vel viverra faucibus. Quisque a lacus ac diam bibendum placerat. Etiam placerat eros a urna dapibus accumsan."
                )
            ]
        )
    ]
)