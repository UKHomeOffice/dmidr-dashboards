from dash import html, dcc

from app.components import report_header

def report_base(title: str, body: list[object]):
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
            html.Div(
                className="tab-controls",
                children=[
                    html.P(
                        className="govuk-body-l",
                        style={"marginBottom": "0px"},
                        children=[
                            "Controls",
                        ],
                    )
                ],
            ),
            report_header(title),
            *body
        ]
    )
