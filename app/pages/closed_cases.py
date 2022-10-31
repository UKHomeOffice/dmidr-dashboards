import dash
from dash import html, dcc

from app.pages.open_cases_components import *
from app.pages.closed_cases_components import *
from app.components import report_header

dash.register_page(
    __name__,
    name="Closed cases",
    path="/closed-cases"
)


layout = html.Div(
    className="report-background-box govuk-body",
    children=[
        html.Div(
            style={"paddingLeft":"10px"},
            children=[
                html.A(
                    className="govuk-back-link",
                    children="Back",
                    href="/"
                ),
            ]
        ),
        dcc.Tabs(
            parent_className="custom-tabs",
            className="custom-tabs-container",
            children=[
                dcc.Tab(
                    label="Report One",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                    children=[
                        html.Div(
                            className="tab-controls",
                            children=[
                                html.P(
                                    className="govuk-body",
                                    style={"marginBottom": "0px"},
                                    children="There is a date here: 10/02/2022",
                                )
                            ],
                        ),
                        report_header("The reports"),
                        html.Div(
                            className="govuk-grid-row",
                            children=[
                                html.Div(
                                    style={"padding": "0px 15px"},
                                    children=[
                                        html.P(
                                            className="govuk-body",
                                            children="Suspendisse potenti. Proin aliquet mi vel viverra faucibus. Quisque a lacus ac diam bibendum placerat. Etiam placerat eros a urna dapibus accumsan. Duis eu ipsum dignissim, sagittis arcu sit amet, tincidunt orci. Donec pulvinar, nibh ac rutrum faucibus, mauris augue malesuada odio, eget luctus turpis justo a nulla. Ut sed ipsum libero. Morbi rutrum, nisi at hendrerit luctus, lacus neque ultrices sem, id pellentesque nibh nunc et turpis. Nam auctor nibh ut orci viverra, vel suscipit neque cursus. Sed cursus nibh eu porttitor interdum. Suspendisse potenti. Aenean eleifend, nisi eget aliquam consequat, odio mauris venenatis purus, id ornare justo tortor a nisl. Proin nec tincidunt nisl. Nullam nec posuere mi. Nulla et erat ultricies, condimentum sapien ut, posuere lacus. Vestibulum ante mauris, pellentesque ac tellus sit amet, fringilla imperdiet nibh.",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="govuk-grid-row",
                                    style={"marginBottom": "30px"},
                                    children=[
                                        html.Div(
                                            className="govuk-grid-column-three-quarters",
                                            children=[
                                                html.Div(
                                                    className="information-box",
                                                    children=[
                                                        html.Span(
                                                            className="govuk-caption-m",
                                                            children="When are tickets completed through the week",
                                                        ),
                                                        html.H3(
                                                            className="govuk-heading-m",
                                                            children="Ticket completion",
                                                        ),
                                                        example_bar,
                                                    ],
                                                )
                                            ],
                                        ),
                                        html.Div(
                                            className="govuk-grid-column-one-quarter",
                                            children=[
                                                html.Div(
                                                    className="information-box",
                                                    children=[
                                                        html.Span(
                                                            className="govuk-caption-m",
                                                            children="All business targets",
                                                        ),
                                                        html.H3(
                                                            className="govuk-heading-m",
                                                            children="Performance",
                                                        ),
                                                        example_gauge,
                                                    ],
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="govuk-grid-row",
                                    children=[
                                        ticket_details_sec,
                                        performance_table_sec,
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                dcc.Tab(
                    label="Report Two",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                    children=[
                        html.Div(
                            className="tab-controls",
                            children=[
                                html.P(
                                    className="govuk-body",
                                    style={"marginBottom": "0px"},
                                    children="There is a date here: 10/02/2022",
                                )
                            ],
                        ),
                        report_header("The reports"),
                        html.Div(
                            className="govuk-grid-row",
                            children=[
                                html.Div(
                                    style={"padding": "0px 15px"},
                                    children=[
                                        html.P(
                                            className="govuk-body",
                                            children="Suspendisse potenti. Proin aliquet mi vel viverra faucibus. Quisque a lacus ac diam bibendum placerat. Etiam placerat eros a urna dapibus accumsan. Duis eu ipsum dignissim, sagittis arcu sit amet, tincidunt orci. Donec pulvinar, nibh ac rutrum faucibus, mauris augue malesuada odio, eget luctus turpis justo a nulla. Ut sed ipsum libero. Morbi rutrum, nisi at hendrerit luctus, lacus neque ultrices sem, id pellentesque nibh nunc et turpis. Nam auctor nibh ut orci viverra, vel suscipit neque cursus. Sed cursus nibh eu porttitor interdum. Suspendisse potenti. Aenean eleifend, nisi eget aliquam consequat, odio mauris venenatis purus, id ornare justo tortor a nisl. Proin nec tincidunt nisl. Nullam nec posuere mi. Nulla et erat ultricies, condimentum sapien ut, posuere lacus. Vestibulum ante mauris, pellentesque ac tellus sit amet, fringilla imperdiet nibh.",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="govuk-grid-row",
                            children=[
                                html.Div(
                                    className="govuk-grid-column-two-thirds",
                                    children=[
                                        example_case_count,
                                        completion_time_table,
                                    ],
                                ),
                                html.Div(
                                    className="govuk-grid-column-one-third",
                                    children=[example_pie],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
    ],
)
