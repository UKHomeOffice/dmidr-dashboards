from dash import html

units = [
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
]

completion_time_table = html.Div(
    className="information_box",
    children=[
        html.Span(className="govuk-caption-m", children="Case response time details"),
        html.H3(className="govuk-heading-m", children="Time to completion details"),
        html.P(
            className="govuk-body",
            children="This would be a good place to describe the table and the purpose. If you were so inclined.",
        ),
        html.Table(
            className="govuk-table",
            children=[
                html.Caption(
                    className="govuk-table__caption govuk-table__caption--s",
                    children="Table title",
                ),
                html.Thead(
                    className="govuk-table__head",
                    children=[
                        html.Tr(
                            className="govuk_table__row",
                            children=[
                                html.Th(
                                    className="govuk-table__header",
                                    scope="col",
                                    children="",
                                ),
                                html.Th(
                                    className="govuk-table__header",
                                    scope="col",
                                    children="Due",
                                ),
                                html.Th(
                                    className="govuk-table__header",
                                    scope="col",
                                    children="Awaiting QA",
                                ),
                                html.Th(
                                    className="govuk-table__header",
                                    scope="col",
                                    children="Answered",
                                ),
                                html.Th(
                                    className="govuk-table__header",
                                    scope="col",
                                    children="Answered on time",
                                ),
                                html.Th(
                                    className="govuk-table__header",
                                    scope="col",
                                    children="Performance",
                                ),
                                html.Th(
                                    className="govuk-table__header",
                                    scope="col",
                                    children="Unanswered",
                                ),
                            ],
                        )
                    ],
                ),
                html.Tbody(
                    className="govuk-table__body",
                    children=[
                        html.Tr(
                            className="govuk-table__row",
                            children=[
                                html.Th(
                                    className="govuk-table__header",
                                    style={"paddingLeft": "5px"},
                                    scope="row",
                                    children=f"{u}",
                                ),
                                html.Td(
                                    className="govuk-table__cell", children="blank"
                                ),
                                html.Td(
                                    className="govuk-table__cell", children="blank"
                                ),
                                html.Td(
                                    className="govuk-table__cell", children="blank"
                                ),
                                html.Td(
                                    className="govuk-table__cell", children="blank"
                                ),
                                html.Td(
                                    className="govuk-table__cell", children="blank"
                                ),
                                html.Td(
                                    className="govuk-table__cell", children="blank"
                                ),
                            ],
                        )
                        for u in units
                    ],
                ),
            ],
        ),
    ],
)
