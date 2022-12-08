import os

import pandas as pd

from app.data.create_db_connection import create_db_connection

MPAM_OPEN_CASES_QUERY = "SELECT * FROM public.mpam_open_cases"

# Dummy data
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

ages = ["4", "15", "78", "4", "17", "2", "7", "4", "12", "31"]

dummy_open_cases = pd.DataFrame(
    data={
        "Case ID": [
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
        "Business Area": blanks,
        "Age": ages,
        "Deadline": blanks,
        "Stage": blanks,
        "Outside Service Standard": blanks,
    }
)


def get_mpam_open_cases():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return dummy_open_cases

    with create_db_connection() as connection:
        data = pd.read_sql_query(MPAM_OPEN_CASES_QUERY, connection)

        return data
