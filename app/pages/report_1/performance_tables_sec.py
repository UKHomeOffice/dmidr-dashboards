# Third party imports
from dash import html

from .leader_board import leader_board, personal_leaders

performance_table_sec = html.Div(
    className="govuk-grid-column-one-third",
    children=[
        html.Div(
            className="information_box",
            style={"marginBottom": "30px"},
            children=[
                html.Span(
                    className="govuk-caption-m", children="Team performance quick view"
                ),
                html.H3(className="govuk-heading-m", children="Team performance"),
                html.P(
                    className="govuk-body",
                    children="There is a good opportunity to add some descriptive text here. ",
                ),
                leader_board,
                html.P(
                    className="govuk-body",
                    children="You could have some text here to explain what is being presented.",
                ),
            ],
        ),
        html.Div(
            className="information_box",
            children=[
                html.Span(
                    className="govuk-caption-m",
                    children="Individual performance quick view",
                ),
                html.H3(className="govuk-heading-m", children="Individual performance"),
                html.P(
                    className="govuk-body",
                    children="There is a good opportunity to add some descriptive text here. ",
                ),
                personal_leaders,
                html.P(
                    className="govuk-body",
                    children="You could have some text here to explain what is being presented.",
                ),
            ],
        ),
    ],
)
