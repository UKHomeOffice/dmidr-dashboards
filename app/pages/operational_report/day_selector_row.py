from dash import html, dcc, callback, Input, Output, ctx

day_selector_row = html.Div(
    className="decs-grid-row govuk-body",
    style={"marginBottom":"50px"},
    children=[
        dcc.Store(
            id='week-day-store', 
            data=None
        ),
        html.Button(
            id="mon-btn",
            className="day-selector govuk-body",
            children="Monday"
        ),
        html.Button(
            id="tues-btn",
            className="day-selector govuk-body",
            children="Tuesday"
        ),
        html.Button(
            id="wed-btn",
            className="day-selector govuk-body",
            children="Wednesday"
        ),
        html.Button(
            id="thurs-btn",
            className="day-selector govuk-body",
            children="Thursday"
        ),
        html.Button(
            id="fri-btn",
            className="day-selector govuk-body",
            children="Friday"
        ),
        html.Button(
            id="clear-day-selection",
            className="govuk-button clear-selection-position",
            children="Clear selection"
        ),
    ]
)

@callback(
    [
        Output(component_id="week-day-store", component_property="data"),
        Output(component_id=f"mon-btn", component_property="className"),
        Output(component_id=f"tues-btn", component_property="className"),
        Output(component_id=f"wed-btn", component_property="className"),
        Output(component_id=f"thurs-btn", component_property="className"),
        Output(component_id=f"fri-btn", component_property="className"),
    ],
    [
        Input(component_id="mon-btn", component_property="n_clicks"),
        Input(component_id="tues-btn", component_property="n_clicks"),
        Input(component_id="wed-btn", component_property="n_clicks"),
        Input(component_id="thurs-btn", component_property="n_clicks"),
        Input(component_id="fri-btn", component_property="n_clicks"),
        Input(component_id="clear-day-selection", component_property="n_clicks")
    ],
    prevent_initial_call=True,
)
def day_clicks(*args):
    button_id = ctx.triggered_id if ctx.triggered_id else None

    if button_id == "mon-btn":
        return [
            "Monday",
            "day-selector--active govuk-body govuk-!-font-weight-bold",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector govuk-body"
        ]

    if button_id == "tues-btn":
        return [
            "Tuesday",
            "day-selector govuk-body",
            "day-selector--active govuk-body govuk-!-font-weight-bold",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector govuk-body"
        ]
    if button_id == "wed-btn":
        return [
            "Wednesday",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector--active govuk-body govuk-!-font-weight-bold",
            "day-selector govuk-body",
            "day-selector govuk-body"
        ]
    if button_id == "thurs-btn":
        return [
            "Thursday",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector--active govuk-body govuk-!-font-weight-bold",
            "day-selector govuk-body"
        ]
    if button_id == "fri-btn":
        return [
            "Friday",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector--active govuk-body govuk-!-font-weight-bold"
        ]
    if button_id == "clear-day-selection":
        return [
            None, 
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector govuk-body"
        ]
