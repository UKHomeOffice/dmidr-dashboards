import os

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

dummy_performance_cases = pd.DataFrame(
    data={
        "Unit": [
            "Unit 1",
            "Unit 2",
            "Unit 3",
            "Unit 4",
            "Unit 5",
            "Unit 6",
            "Unit 7",
            "Unit 8",
            "Unit 9",
            "Unit 10",
        ],
        "Due": blanks,
        "Answered": blanks,
        "Answered on time": blanks,
        "Performance": blanks,
        "Unanswered": blanks,
    }
)


def get_mpam_performance_cases():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return dummy_performance_cases

    with create_db_connection() as connection:
        data = pd.read_sql_query(MPAM_OPEN_CASES_QUERY, connection)

        return data
