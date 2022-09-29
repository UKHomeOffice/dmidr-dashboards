from dash import html

def auto_govuk_table(dFrame, title:str=None, titleSize:str="s", boldLead:bool=False, hiddenLeadHead:bool=False):
    """
    Function to build a style a table in accordance with GovUK style guide.
    
    dFrame: DataFrame - Prepared data frame to be turned into a table.
    title: String - Title for the table, default None.
    titleSize: String - Set the size of the title.
    boldLead: Bool - Set the leading column to bold text, default False.
    hiddenLeadHead: Bool - Hide the leading column heading, default False. 
    """
    return html.Table(
        className="govuk-table",
        children=[
            auto_table_title(title, titleSize),
            auto_table_header(dFrame.columns, hiddenLeadHead),
            auto_table_body(dFrame, boldLead=boldLead)    
        ]
    )

def auto_table_title(title:str, titleSize) -> str:
    if title:
        return html.Caption(
            className=f"govuk-table__caption govuk-table__caption--{titleSize}",
            children=f"{title}"
        )
    else:
        return None


def auto_table_header(columns, hiddenLeadHead):
    is_hidden=""
    if hiddenLeadHead:
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

def auto_table_body(df, boldLead=False):
    bold = ""
    if boldLead:
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
