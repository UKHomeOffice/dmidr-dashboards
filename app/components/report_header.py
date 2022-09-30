from dash import html

def report_header(report_title:str, todays_date):
    return  html.Div(
        className="govuk-grid-row",
        style={"marginTop":"20px"},
        children=[
            html.Div(
                className="govuk-grid-column-one-third",
                children=[
                    html.Img(
                        className="ho-logo-image",
                        src="/assets/images/uk-home-office-logo.png", 
                    ),
                    html.P(
                        className="ho-logo-text govuk-body-l",
                        children="Home Office"
                    ), 
                ]
            ),
            html.Div(
                className="govuk-grid-column-one-third",
                children=[
                    html.H3(
                        className="govuk-heading-l",
                        style={"textAlign":"center"},
                        children=f"{report_title}"
                    ), 
                ]
            ),
            html.Div(
                className="govuk-grid-column-one-third",
                children=[
                    html.Span(
                        className="govuk-caption-s tab-date-caption",
                        children="Todays date"
                    ),
                    html.H3(
                        className="govuk-heading-s",
                        style={"textAlign":"right"},
                        children=f"{todays_date.strftime('%A %d %B %Y')}"
                    ), 
                ]
            )
        ]
    )