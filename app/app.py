import dash
from dash import Dash, html

from components import *


app = Dash(
    __name__, 
    use_pages=True
)

app.layout = html.Div(
    children = [
        govuk_header,
        html.Div(
            className="govuk-grid-row",
            style={
                "padding":"10px 2% 0% 2%"
            },
            children=[
                html.A(
                    className="govuk-link govuk-!-font-size-27",
                    style={
                        "float":"left", 
                        "marginRight":"30px", 
                    },
                    children=f"{page['name']}", 
                    href=page["relative_path"]
                )
                for page in dash.page_registry.values()
            ]
        ),
        dash.page_container, 
        govuk_footer
    ]
)

if __name__ == '__main__':
	app.run_server(debug=True)