import dash
from dash import html, dcc

from .report_1 import *
from .report_2 import *

dash.register_page(__name__, path="/report-3")


layout = html.Div(
    className="report_background_box govuk-body",
    children=[
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
                            style={
                                "padding": "10px 5px",
                                "borderBottom": "1px solid #000",
                                "backgroundColor": "#fff",
                            },
                            children=[
                                html.P(
                                    className="govuk-body",
                                    style={"marginBottom": "0px"},
                                    children="There is a date here: 10/02/2022",
                                )
                            ],
                        ),
                        html.Div(
                            className="govuk-grid-row",
                            style={"marginTop": "20px"},
                            children=[
                                html.Div(
                                    className="govuk-grid-column-one-third",
                                    children=[
                                        html.Img(
                                            style={
                                                "verticalAlign": "middle",
                                                "height": "45px",
                                                "paddingLeft": "10px",
                                                "marginRight": "15px",
                                                "borderLeft": "3px solid #8f23b3",
                                            },
                                            src="/assets/images/uk-home-office-logo.png",
                                        ),
                                        html.P(
                                            className="govuk-body-l",
                                            style={
                                                "verticalAlign": "middle",
                                                "display": "inline",
                                            },
                                            children="Home Office",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="govuk-grid-column-one-third",
                                    children=[
                                        html.H3(
                                            className="govuk-heading-l",
                                            style={"textAlign": "center"},
                                            children="Performance Overview",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="govuk-grid-column-one-third",
                                    children=[
                                        html.Span(
                                            className="govuk-caption-s",
                                            style={
                                                "display": "block",
                                                "textAlign": "right",
                                            },
                                            children="Todays date",
                                        ),
                                        html.H3(
                                            className="govuk-heading-s",
                                            style={"textAlign": "right"},
                                            children="Monday 9 September 2022",
                                        ),
                                    ],
                                ),
                            ],
                        ),
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
                                                    className="information_box",
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
                                                    className="information_box",
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
                            style={
                                "padding": "10px 5px",
                                "borderBottom": "1px solid #000",
                                "backgroundColor": "#fff",
                            },
                            children=[
                                html.P(
                                    className="govuk-body",
                                    style={"marginBottom": "0px"},
                                    children="There is a date here: 10/02/2022",
                                )
                            ],
                        ),
                        html.Div(
                            className="govuk-grid-row",
                            style={"marginTop": "20px"},
                            children=[
                                html.Div(
                                    className="govuk-grid-column-one-third",
                                    children=[
                                        html.Img(
                                            style={
                                                "verticalAlign": "middle",
                                                "height": "45px",
                                                "paddingLeft": "10px",
                                                "marginRight": "15px",
                                                "borderLeft": "3px solid #8f23b3",
                                            },
                                            src="/assets/images/uk-home-office-logo.png",
                                        ),
                                        html.P(
                                            className="govuk-body-l",
                                            style={
                                                "verticalAlign": "middle",
                                                "display": "inline",
                                            },
                                            children="Home Office",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="govuk-grid-column-one-third",
                                    children=[
                                        html.H3(
                                            className="govuk-heading-l",
                                            style={"textAlign": "center"},
                                            children="Performance Overview",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="govuk-grid-column-one-third",
                                    children=[
                                        html.Span(
                                            className="govuk-caption-s",
                                            style={
                                                "display": "block",
                                                "textAlign": "right",
                                            },
                                            children="Todays date",
                                        ),
                                        html.H3(
                                            className="govuk-heading-s",
                                            style={"textAlign": "right"},
                                            children="Monday 9 September 2022",
                                        ),
                                    ],
                                ),
                            ],
                        ),
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
