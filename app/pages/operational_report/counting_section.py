from dash import html

def counting_section(box_text, bold_section:str="", count=None):
    return html.Div(
        className="govuk-grid-column-one-quarter", 
        children=[
            html.Div(
                style={
                    "backgroundColor":"#fff",
                    "padding":"5px"
                },
                children=[
                    html.P(
                        className="govuk-body-l",
                        style={"marginBottom":"10px"},
                        children=[
                            f"{box_text} ",
                            html.B(f"{bold_section}")
                        ]
                    ),
                    html.H1(
                        className="govuk-body counter-number--l ",
                        children=f"{count}"
                    )
                ]
            )
        ]
    )