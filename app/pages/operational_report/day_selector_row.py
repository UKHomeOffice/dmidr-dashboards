from dash import html

day_selector_row = html.Div(
    className="govuk-grid-row",
    style={"marginBottom":"30px"},
    children=[
        html.Div(
            id="monday-selector-div",
            className="day-selector",
            children=[
                html.P(
                    className="govuk-body day-selector-text",
                    children="Monday"
                )
            ]
        ),
        html.Div(
            id="tuesday-selector-div",
            className="day-selector",
            children=[
                html.P(
                    className="govuk-body day-selector-text",
                    children="Tuesday"
                )
            ]
        ),
        html.Div(
            id="wednesday-selector-div",
            className="day-selector",
            children=[
                html.P(
                    className="govuk-body day-selector-text",
                    children="Wednesday"
                )
            ]
        ),
        html.Div(
            id="thursday-selector-div",
            className="day-selector",
            children=[
                html.P(
                    className="govuk-body day-selector-text",
                    children="Thursday"
                )
            ]
        ),
        html.Div(
            id="firday-selector-div",
            className="day-selector",
            children=[
                html.P(
                    className="govuk-body day-selector-text",
                    children="Friday"
                )
            ]
        )
    ]
)