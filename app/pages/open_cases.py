import dash

from dash import html

from app.pages.open_cases_comp import *


dash.register_page(
    __name__, 
    path="/open-cases",
    name="Open Cases"
)
 
layout = html.Div(
    style={"backgroundColor": "#f1f1f1", "padding": "20px 0px"},
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
        html.Div(
            className="decs-grid-row",
            children=[
                html.Div(
                    style={"padding": "0px 15px"},
                    children=[
                        html.H2(
                            className="govuk-heading-l", children="Title for the report"
                        ),
                        html.P(
                            className="govuk-body",
                            children="Suspendisse potenti. Proin aliquet mi vel viverra faucibus. Quisque a lacus ac diam bibendum placerat. Etiam placerat eros a urna dapibus accumsan. Duis eu ipsum dignissim, sagittis arcu sit amet, tincidunt orci. Donec pulvinar, nibh ac rutrum faucibus, mauris augue malesuada odio, eget luctus turpis justo a nulla. Ut sed ipsum libero. Morbi rutrum, nisi at hendrerit luctus, lacus neque ultrices sem, id pellentesque nibh nunc et turpis. Nam auctor nibh ut orci viverra, vel suscipit neque cursus. Sed cursus nibh eu porttitor interdum. Suspendisse potenti. Aenean eleifend, nisi eget aliquam consequat, odio mauris venenatis purus, id ornare justo tortor a nisl. Proin nec tincidunt nisl. Nullam nec posuere mi. Nulla et erat ultricies, condimentum sapien ut, posuere lacus. Vestibulum ante mauris, pellentesque ac tellus sit amet, fringilla imperdiet nibh.",
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="decs-grid-row",
            children=[
                html.Div(
                    className="decs-grid-column-two-thirds",
                    children=[example_case_count, completion_time_table],
                ),
                html.Div(
                    className="decs-grid-column-one-third", children=[example_pie]
                ),
            ],
        ),
    ],
)
