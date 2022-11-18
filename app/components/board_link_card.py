from dash import html

def board_link_card(dash_title:str, dash_link:str="/"):
    return html.Div(
        className="govuk-grid-column-one-third",
        style={"padding":"0px 0px 0px 15px"},
        children=[
            html.Div(
                style={"border":"1.5px solid #c3c3c3"},
                children=[
                    html.Div(
                        style={"backgroundColor":"#e6e6e6"},
                        children=[
                            html.H2(
                                className="govuk-heading-m",
                                style={
                                    "padding":"10px 5px", 
                                    "marginBottom":"0px"
                                },
                                children=dash_title
                            ),
                        ]
                    ),
                    html.Div(
                        style={"padding":"10px 5px"},
                        children=[
                            html.A(
                                className="govuk-link",
                                children="View dashboard",
                                href=dash_link
                            )
                        ]
                    )
                ]
            )
        ]
    )