# Third party imports
from dash import html

govuk_header = html.Header(
    className="govuk-header ",
    role="banner",
    **{"data-module": "govuk-header"},
    children=[
        html.Div(
            className="govuk-header__container ",
            style={"marginRight": "2%", "marginLeft": "2%",},
            children=[
                html.Div(
                    className="govuk-header__logo",
                    children=[
                        html.A(
                            className="govuk-header__link govuk-header__link--homepage",
                            href="/",
                            children=[
                                html.Span(
                                    className="govuk-header__logotype",
                                    style={
                                        "marginRight":"15px"
                                    },
                                    children=[
                                        html.Img(
                                            className="govuk-header__logotype-crown",
                                            style={
                                                "marginRight": "10px",
                                                "marginBottom":"3px"
                                            },
                                            src="/assets/images/govuk-logotype-crown.png",
                                        ),
                                        html.Span(
                                            className="govuk-header__logotype-text",
                                            children="GOV.UK",
                                        ),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="govuk-header__content", 
                    children=[
                        html.A(
                            className="govuk-header__link govuk-header__service-name",
                            href="/",
                            children="DECS - Operational Reporting"
                        )
                    ]
                )
            ],
        ),
    ]
)
