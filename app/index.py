import dash
from dash import Dash, html, callback, Output, Input
from flask import Flask

from app.components import *

server = Flask(__name__)

app = Dash(__name__, use_pages=True, server=server)

app.layout = html.Div(
    id="main",
    children=[
        decs_header,
        dash.page_container,
        html.Span(id="login-status-text", children=[]),
        decs_footer
    ]
)


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True, port=8050)
