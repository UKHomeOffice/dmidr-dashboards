import plotly.express as px
from dash import html, dcc


def decs_open_cases_pie(pie_data, values_col:str, pie_name:str="Placeholder", legend_title:str="Legend"):

    pie_chart = px.pie(
        values=pie_data[values_col].value_counts(), 
        names=pie_data[values_col].value_counts().index,
        hole=0.6,
        color_discrete_sequence=[
            "#832CAD","#E590C6","#5774F6",
            "#D82EF6","#72BFF9"
        ]
    )

    pie_chart.update_layout(
        annotations=[
            dict(
                text=f"{pie_data.shape[0]}", 
                x=0.5, 
                y=0.5, 
                font_size=30, 
                showarrow=False
            )
        ],
        legend={
            "title":f"{legend_title}",
        }
    )

    pie_chart.update_traces(
        textinfo="value"
    )

    return html.Div(
        className="decs-grid-row",
        style={"margin":"0px"},
        children=[
            html.Div(
                className="information-box",
                children=[
                    html.H3(className="govuk-heading-m", children=pie_name),
                    dcc.Graph(figure=pie_chart),
                ],
            )
        ],
    )
