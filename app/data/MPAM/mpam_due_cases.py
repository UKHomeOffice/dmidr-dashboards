import os

import pandas as pd

from app.data.get_data import create_db_connection

MPAM_DUE_CASES_QUERY = "SELECT * FROM public.mpam_due_cases"
MPAM_DUE_CASES_AGGREGATE_QUERY = "SELECT * FROM public.mpam_due_cases_aggregate"

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

dummy_due_cases = pd.DataFrame(
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
        "Awaiting QA": blanks,
        "Answered": blanks,
        "Answered on time": blanks,
        "Performance": blanks,
        "Unanswered": blanks,
    }
)

dummy_due_cases_aggregate = pd.Series(data={
        "Total due this week": 10,
        "Total due next 4 weeks": 18,
        "Total out of service standard": 3,
        "Total cases": 18
    })


def get_mpam_due_cases():

    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return dummy_due_cases

    with create_db_connection() as connection:
        data = pd.read_sql_query(MPAM_DUE_CASES_QUERY, connection)

        return data


def get_mpam_due_cases_aggregate():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return dummy_due_cases_aggregate

    with create_db_connection() as connection:
            data = pd.read_sql_query(MPAM_DUE_CASES_AGGREGATE_QUERY, connection)

            return data.squeeze()
