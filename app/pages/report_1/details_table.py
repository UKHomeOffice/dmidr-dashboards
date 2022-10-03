import pandas as pd

from components import auto_govuk_table

blanks = ["blank", "blank", "blank", "blank", "blank", "blank", "blank", "blank", "blank", "blank"]

unit_df = pd.DataFrame(
    data={
        "Unit":["Unit 1","Unit 2","Unit 3","Unit 4","Unit 5","Unit 6","Unit 7","Unit 8","Unit 9","Unit 10"],
        "Due":blanks,
        "Awaiting QA":blanks,
        "Answered":blanks,
        "Answered on time":blanks,
        "Performance":blanks,
        "Unanswered":blanks
    }
)


details_table = auto_govuk_table(
    unit_df,
    title="Performance details",
    title_size="m",
    bold_lead=True,
    hidden_lead_head=True
)
