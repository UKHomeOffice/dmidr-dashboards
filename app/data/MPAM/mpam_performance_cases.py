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

business_areas = [
    "PCT",
    "BF",
    "LSE",
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
    80,
    74,
    82,
]

Unanswered = [
    243,
    431,
    12,
]

due_data = []
n_days = 3
base = pd.Timestamp.today()
timestamp_list = [base + datetime.timedelta(days=x) for x in range(n_days)]
for x in timestamp_list:
    due_data.append(x)

dummy_performance_cases = pd.DataFrame(
    data={
        "business_area": business_areas,
        "Due": Due,
        "Answered": Answered,
        "Answered on time": Answered_on_time,
        "Performance": Performance,
        "Unanswered": Unanswered,
        "date": due_data,
    }
)


def get_mpam_performance_cases():
    if os.environ.get("STAGE") == "local" or os.environ.get("STAGE") is None:
        return dummy_performance_cases

    with create_db_connection() as connection:
        data = pd.read_sql_query(MPAM_OPEN_CASES_QUERY, connection)

        return data
