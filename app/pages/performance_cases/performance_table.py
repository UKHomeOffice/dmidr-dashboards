import pandas as pd

from app.components import auto_govuk_table



def performance_table_func(unit_df):
    performance_table = auto_govuk_table(
        unit_df,
        title="Performance details",
        title_size="m",
        bold_lead=True,
        hidden_lead_head=True,
    )
    return performance_table