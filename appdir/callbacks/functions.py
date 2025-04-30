import base64
import io
import os

from dash import html, dash_table
import pandas as pd


def store_upload(
        content: str, 
        name: str, 
        destination: str, 
        variable=False
    ) -> str:
    """Store upload in destination folder."""

    content_type, content_string = content.split(',')
    decoded = base64.b64decode(content_string)

    try:
        with open(f"{destination}/{name}", 'wb') as f:
            f.write(decoded)
    except Exception as e:
        print(e)

    if variable:
        return decoded
    
def create_table(
        decoded: str = None, 
        source: str = None
    ) -> dash_table.DataTable:
    """Create a DataTable from the uploaded file OR the latest saved file."""
    
    try:
        if decoded is not None:
            df = pd.read_excel(io.BytesIO(decoded))
            column_list = df.columns.to_list()
            df.columns = ['' if "Unnamed" in x else x for x in column_list]

        elif os.path.exists(source):
            df = pd.read_excel(source)
            column_list = df.columns.to_list()
            df.columns = ['' if "Unnamed" in x else x for x in column_list]

        else:
            return html.Div(["No file available. Please upload one."])

    except Exception as e:
        print(f"From create_table: {e}")
        return html.Div(["There was an error processing this file."])
    
    return html.Div([dash_table.DataTable(
        columns=[{"name": col, "id": col} for col in df.columns],
        data=df.to_dict("records"),
        style_table={"overflowX": "auto"},
        style_cell={"textAlign": "left"},
    )])
