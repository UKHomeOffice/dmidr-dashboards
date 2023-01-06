from dash import html

def counter(text:str= "place holder", count:int=000):
    return html.Div(
        className="decs-grid-row",
        children=[
            html.Div(
                className="counter-tile",
                children=[
                    html.P(
                        className="govuk-body-l",
                        style={"marginBottom":"10px"},
                        children=[f"{text}"]
                    ),
                    html.H1(
                        className="govuk-body counter-number--l",
                        children=f"{count}"
                    )
                ]
            )
        ]
    )