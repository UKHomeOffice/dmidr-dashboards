# Third party
from dash import html

govuk_footer = html.Footer(
    className="govuk-footer",
    role="contentinfo",
    children=[
        html.Div(
            className="govuk-footer__container",
            style={
                "marginRight": "2%",
                "marginLeft": "2%",
                "marginTop": "30px",
            },
            children=[
                html.Div(
                    className="govuk-footer__meta",
                    children=[
                        html.Div(
                            className="govuk-footer__meta-item govuk-footer__meta-item--grow",
                            children=[
                                # Logo,
                                html.Span(
                                    className="govuk-footer__licence-description",
                                    children=[
                                        "All content is available under the ",
                                        html.A(
                                            "Open Government Licence v3.0",
                                            className="govuk-footer__link", 
                                            href="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/", 
                                            rel="license",
                                        ),
                                        ", except where otherwise stated"
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className="govuk-footer__meta-item",
                            children=[
                                html.A("© Crown copyright", 
                                    href="https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/",
                                    className="govuk-footer__link govuk-footer__copyright-logo"
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)