# Third party
from dash import html

decs_footer = html.Footer(
    style={
        "padding":"0px 20px"
    },
    children=[
        html.P(
            style={
                "font":"roboto",
                "float":"left"
            },
            children="A Home Office Digital, Data and Technology service"
        ), 
        html.A(
            style={
                "float":"right",
                "margin":"16px 0px 16px 16px"
            },
            href="https://www.gov.uk",
            children="GOV.UK"
        ),
        html.A(
            style={
                "float":"right",
                "margin":"16px 0px 16px 16px"
            },
            href="mailto:test@testing.gov.uk",
            children="Feedback"
        )
    ]
)
