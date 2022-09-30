from dash import html
import pandas as pd

teams = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5", "Team 6"]
scores = [95, 93, 84, 65, 63, 54]

users = ["User 1", "User 2", "User 3", "User 4", "User 5", "User 6"]
users_scores = [94, 91, 88, 64, 60, 59]

leader_board = html.Div(
    className="govuk-grid-row",
    children=[
        html.Div(
            className="govuk-grid-column-one-half",
            children=[
                html.Table(
                    className="govuk-table",
                    children=[
                        html.Caption(
                            className="govuk-table__caption govuk-table__caption--s",
                            children="Top 3",
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
                                            children="Team",
                                        ),
                                        html.Th(
                                            className="govuk-table__header",
                                            scope="col",
                                            children="Score",
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
                                            children=teams[i],
                                        ),
                                        html.Td(
                                            className="govuk-table__cell",
                                            children=f"{scores[i]} %",
                                        ),
                                    ],
                                )
                                for i in [0, 1, 2]
                            ],
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="govuk-grid-column-one-half",
            children=[
                html.Table(
                    className="govuk-table",
                    children=[
                        html.Caption(
                            className="govuk-table__caption govuk-table__caption--s",
                            children="Bottom 3",
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
                                            children="Team",
                                        ),
                                        html.Th(
                                            className="govuk-table__header",
                                            scope="col",
                                            children="Score",
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
                                            children=teams[i],
                                        ),
                                        html.Td(
                                            className="govuk-table__cell",
                                            children=f"{scores[i]} %",
                                        ),
                                    ],
                                )
                                for i in [3, 4, 5]
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)

#################################

personal_leaders = html.Div(
    className="govuk-grid-row",
    children=[
        html.Div(
            className="govuk-grid-column-one-half",
            children=[
                html.Table(
                    className="govuk-table",
                    children=[
                        html.Caption(
                            className="govuk-table__caption govuk-table__caption--s",
                            children="Top 3",
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
                                            children="Team",
                                        ),
                                        html.Th(
                                            className="govuk-table__header",
                                            scope="col",
                                            children="Score",
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
                                            children=users[i],
                                        ),
                                        html.Td(
                                            className="govuk-table__cell",
                                            children=f"{users_scores[i]} %",
                                        ),
                                    ],
                                )
                                for i in [0, 1, 2]
                            ],
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="govuk-grid-column-one-half",
            children=[
                html.Table(
                    className="govuk-table",
                    children=[
                        html.Caption(
                            className="govuk-table__caption govuk-table__caption--s",
                            children="Bottom 3",
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
                                            children="Team",
                                        ),
                                        html.Th(
                                            className="govuk-table__header",
                                            scope="col",
                                            children="Score",
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
                                            children=users[i],
                                        ),
                                        html.Td(
                                            className="govuk-table__cell",
                                            children=f"{users_scores[i]} %",
                                        ),
                                    ],
                                )
                                for i in [3, 4, 5]
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)
