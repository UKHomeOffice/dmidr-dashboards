from dash import html, dcc

from app.components import report_header

def report_base(title: str, body: list[object], controls: list[object] = None):
    return html.Div(
        className="report-background-box govuk-body",
        children=[
            html.Hr(
                className="decs-section-break"
            ),
            html.Div(
                style={"paddingLeft": "10px"},
                children=[
                    html.A(
                        className="govuk-back-link govuk-link--no-underline govuk-!-font-size-19",
                        style={
                            "paddingLeft": "20px"
                        },
                        children="Back to home",
                        href="/"
                    ),
                ]
            ),
            report_header(title),
            html.Div(
                className="tab-controls govuk-body-l",
                style={"paddingTop": "0px", "marginBottom": "0px"},
                children=[
                    html.P(
                        style={"marginBottom": "15px"},
                        children=[
                            "Controls"
                        ],
                    ),
                    *controls
                ],
            ) if controls else None,
            *body
        ]
    )
