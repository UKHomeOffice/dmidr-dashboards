from dash import html
import pandas as pd

from components import auto_govuk_table

teams_df = pd.DataFrame(
    data={
        "Team":["Team 1", "Team 2", "Team 3", "Team 4", "Team 5", "Team 6"],
        "Score":[95, 93, 84, 65, 63, 54]
    }
)

users_df = pd.DataFrame(
    data={
        "User":["User 1", "User 2", "User 3", "User 4", "User 5", "User 6"],
        "Score":[94, 91, 88, 64, 60, 59]
    }
)


leader_board = html.Div(
    className="govuk-grid-row",
    children=[
        html.Div(
            className="govuk-grid-column-one-half", 
            children=[
                auto_govuk_table(
                    teams_df[0:3],
                    title="Top 3",
                    bold_lead=True
                )
            ]
        ), 
        html.Div(
            className="govuk-grid-column-one-half", 
            children=[
                auto_govuk_table(
                    teams_df[3:6],
                    title="Bottom 3",
                    bold_lead=True
                )
            ]
        ), 
    ]
)

personal_leaders = html.Div(
    className="govuk-grid-row",
    children=[
        html.Div(
            className="govuk-grid-column-one-half", 
            children=[
                auto_govuk_table(
                    users_df[0:3], 
                    title="Top 3",
                    bold_lead=True
                )
            ]
        ), 
        html.Div(
            className="govuk-grid-column-one-half", 
            children=[
                auto_govuk_table(
                    users_df[3:6], 
                    title="Bottom 3",
                    bold_lead=True
                )
            ]
        ), 
    ]
)