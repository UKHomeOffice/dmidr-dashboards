import plotly.express as px
from dash import html, dcc

the_pie_chart = px.pie(values=[90, 20, 20, 20, 50, 100, 60], hole=0.6,)

the_pie_chart.update_layout(
    annotations=[dict(text="66", x=0.5, y=0.5, font_size=30, showarrow=False)]
)


example_pie = html.Div(
    className="govuk-grid-row",
    children=[
        html.Div(
            className="information_box",
            children=[
                html.Span(className="govuk-caption-m", children="The title caption"),
                html.H3(className="govuk-heading-m", children="This title"),
                html.P(
                    className="govuk-body", children="This is some place holder text."
                ),
                dcc.Graph(figure=the_pie_chart),
            ],
        )
    ],
)
