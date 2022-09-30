from dash import html

def auto_govuk_table(dFrame, title:str=None, title_size:str="s", bold_lead:bool=False, hidden_lead_head:bool=False):
    """
    Function to build a style a table in accordance with GovUK style guide.
    
    dFrame: DataFrame - Prepared data frame to be turned into a table.
    title: String - Title for the table, default None.
    title_size: String - Set the size of the title.
    bold_lead: Bool - Set the leading column to bold text, default False.
    hidden_lead_head: Bool - Hide the leading column heading, default False. 
    """
    return html.Table(
        className="govuk-table",
        children=[
            auto_table_title(title, title_size),
            auto_table_header(dFrame.columns, hidden_lead_head),
            auto_table_body(dFrame, bold_lead=bold_lead)    
        ]
    )

def auto_table_title(title:str, title_size) -> str:
    if title:
        return html.Caption(
            className=f"govuk-table__caption govuk-table__caption--{title_size}",
            children=f"{title}"
        )
    else:
        return None


def auto_table_header(columns, hidden_lead_head):
    is_hidden=""
    if hidden_lead_head:
        is_hidden = "hide-lead-column-head"

    return html.Thead(
        className=f"govuk-table__head pad-head {is_hidden}",
        children=[
            html.Tr(
                className="govuk_table__row",
                children=[
                    html.Th(
                        className="govuk-table__header",
                        scope="col",
                        children=c
                    )
                    for c in columns
                ]
            )
        ]
    )

def auto_table_body(df, bold_lead=False):
    bold = ""
    if bold_lead:
        bold = "auto-table-cells"

    return html.Tbody(
        className=f"govuk-table__body {bold}",
        children=[
            html.Tr(
                className="govuk-table__row", 
                children=[
                    html.Td(
                        className="govuk-table__cell", 
                        children=f"{v}"
                    )
                    for v in row
                ]
            )
            for i, row in df.iterrows()
        ]
    )
