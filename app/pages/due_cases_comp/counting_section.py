from dash import html

def counting_section(box_text, bold_section:str="", count:int=None):
    return html.Div(
        className="decs-grid-column-one-quarter", 
        children=[
            html.Div(
                className="counter-tile",
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