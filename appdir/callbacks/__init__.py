import os
from dash import callback, Output, Input, State, Patch, dash_table, ctx,  MATCH
from pandas import DataFrame
import plotly_express as px

from appdir.config import Config
from appdir.api_module import APIClient
from .classes import View
from .functions import store_upload, create_table

upload_path = os.path.join(os.getcwd(), Config.UPLOAD_PATH)

# ------------------- User Settings -------------------------------------------

# ------------------- Upload callbacks ----------------------------------------

@callback(Output('some-table', 'children'),
          Input('upload', 'contents'))
def display_content(content: str) -> dash_table.DataTable:
    """Display uploaded content and store it."""
    default_name = 'upload.xlsx'

    if content is not None:
        decoded = store_upload(
            content, default_name, upload_path, variable=True
            )
        return create_table(decoded)
    
    else:
        source = upload_path + '/' + default_name
        return create_table(source=source)

# ------------------- API callbacks -------------------------------------------
# It is possible to select multiple views in the first tab to allow for user 
# customisation. Therefore these input variables have to be matched according to
# the query response
@callback(Output({'type': 'analytics-graph', 'index': MATCH}, 'figure'), 
          Input({'type': 'metric-ddown', 'index': MATCH}, 'value'),
          Input({'type': 'dimension-ddown', 'index': MATCH}, 'value'),
          Input({'type': 'date-range', 'index': MATCH}, 'start_date'),
          Input({'type': 'date-range', 'index': MATCH}, 'end_date'),
          State({'type': 'metric-ddown', 'index': MATCH}, 'id'),
          State({'type': 'dimension-ddown', 'index': MATCH}, 'id'))
def some(metric_value: str, dim_value: str, start, end, metric_id, dim_id):
    instance = APIClient.for_plausible()
    if not dim_value:
        dim_value = ""
    json = {
        "site_id": Config.TARGET_SITE,
        "metrics": [metric_value],
        "date_range": [start, end],
        "dimensions": [dim_value]
    }
    try:
        response = instance.post(json=json)
        response.raise_for_status()
        results = response.json().get("results", [])

        df = DataFrame([
            {
                'Dimension': ' / '.join(dct['dimensions']),
                metric_value.capitalize(): dct["metrics"][0]
            } for dct in results
        ])
        
        fig = px.bar(df, x="Dimension", y=metric_value.capitalize(),
                    #  title=f"{metric.capitalize()} by {' and '.join([d.split(':')[1].replace('_name', '') for d in dimensions])}"
                    )
        return fig
    except Exception as e:
        return px.scatter(title=f"Error fetching data: {str(e)}")

# ------------------- View callback -------------------------------------------
@callback(Output('view-container', 'children'),
          Input('add-btn', 'n_clicks'),
          Input('delete-btn', 'n_clicks'),
          State('view-container', 'children'))
def present_view(_add, _delete, state: list):
    index = len(state) if state else 0
    
    patched_children = Patch()
    if ctx.triggered_id == 'add-btn':
        patched_children.append(View(index=index).present_view())
        return patched_children
    
    if ctx.triggered_id == 'delete-btn':
        if state is None:
            pass
        else:
            return state[:-1]
