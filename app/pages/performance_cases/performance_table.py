import pandas as pd

from app.components import auto_govuk_table



def performance_table_func(unit_df):
    performance_df = unit_df[["Due", "Answered", "Answered", "Completed in time", "Performance", "Unanswered"]].copy()
    performance_table = auto_govuk_table(
        performance_df,
        title="Performance details",
        title_size="m",
        bold_lead=True,
        hidden_lead_head=False,
    )
    return performance_table