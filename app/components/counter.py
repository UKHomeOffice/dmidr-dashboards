from dash import html


def counter(text: str = "place holder", count: int = 000, bold_section:str = None):
    return html.Div(
        className="counter-tile",
        children=[
            html.P(
                className="govuk-body-l",
                style={"marginBottom": "10px"},
                children=[f"{text}", html.B(f" {bold_section}")],
            ),
            html.H1(className="govuk-body counter-number--l", children=f"{count}"),
        ],
    )
