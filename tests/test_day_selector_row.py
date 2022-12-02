from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

from app.pages.operational_report.day_selector_row import day_clicks


def test_day_selector_selects_tuesday():
        def run_callback():
            context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": "tues-btn.n_clicks"}]}))
            return day_clicks()

        ctx = copy_context()
        output = ctx.run(run_callback)
        assert output[0] == "Tuesday"
        assert output[1:6] == [
                "day-selector govuk-body",
                "day-selector--active govuk-body govuk-!-font-weight-bold",
                "day-selector govuk-body",
                "day-selector govuk-body",
                "day-selector govuk-body"
            ]


def test_day_selector_selects_friday():
    def run_callback():
        context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": "fri-btn.n_clicks"}]}))
        return day_clicks()

    ctx = copy_context()
    output = ctx.run(run_callback)
    assert output[0] == "Friday"
    assert output[1:6] == [
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector govuk-body",
            "day-selector--active govuk-body govuk-!-font-weight-bold",
        ]