# Third party
from dash import html

decs_footer = html.Footer(
    style={
        "padding":"0px 30px"
    },
    children=[
        html.P(
            className="govuk-body",
            style={
                "float":"left",
                "marginTop":"16px"
            },
            children="A Home Office Digital, Data and Technology service"
        ), 
        html.A(
            className="govuk-link govuk-!-font-size-19",
            style={
                "float":"right",
                "margin":"16px 0px 16px 16px"
            },
            href="https://www.gov.uk",
            children="GOV.UK"
        ),
        html.A(
            className="govuk-link govuk-!-font-size-19",
            style={
                "float":"right",
                "margin":"16px 0px 16px 16px"
            },
            href="mailto:test@testing.gov.uk",
            children="Feedback"
        )
    ]
)
