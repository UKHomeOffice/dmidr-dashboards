import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(
    className="govuk-grid-row",
    style={
        "marginTop":"50px"
    },
    children=[
        html.Div(
            className="govuk-grid-column-two-thirds",
            style={
                "padding":"0px"
            },
            children=[
                html.H1(
                    className="govuk-heading-l",
                    children="Page not found"
                ),
                html.P(
                    className="govuk-body",
                    children="If you typed the web address, check it is correct."
                ),
                html.P(
                    className="govuk-body",
                    children="If you pasted the web address, check you copied the entire address."
                ),
                html.P(
                    className="govuk-body",
                    children=[
                        "If the web address is correct or you selected a link or button, ",
                        html.A(
                            className="govuk-link",
                            href="/",
                            children="try returning to the home page"
                        ),
                        "."
                    ]
                )
            ]
        )
    ]
)