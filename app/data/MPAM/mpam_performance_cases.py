import os
import datetime

import pandas as pd

from app.data.create_db_connection import create_db_connection

MPAM_OPEN_CASES_QUERY = "SELECT * FROM public.mpam_performance"

blanks = [
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
    "blank",
]

Due = [
    39, 
    403,
    49,
]

Answered = [
    53, 
    234,
    59,
]

Answered_on_time = [
    32,
    212,
    34,
]

Performance = [
    "80%",
    "74%",
    "82",
]

Unanswered = [
    243,
    431,
    12,
]

dummy_performance_cases = pd.DataFrame(
    data={
        "Due": Due,
        "Awaiting QA": Unanswered,
        "Answered": Answered,
        "Completed in time": Answered_on_time,
        "Performance": Performance,
        "Unanswered": Unanswered,
        "Required to achieve 95% target": Due,
        "Outstanding required to achieve 95% target": Due,

    }
)


def get_mpam_performance_cases():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return dummy_performance_cases

    with create_db_connection() as connection:
        data = pd.read_sql_query(MPAM_OPEN_CASES_QUERY, connection)

        return data
