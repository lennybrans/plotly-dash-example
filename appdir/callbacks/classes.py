from dash import html, dcc
from datetime import datetime, timedelta

class View:
    """Contains a customizable view."""
    def __init__(self, index: int):
        self.index = index

    def present_view(self):
        return html.Div(className="views", id=f"view{self.index}", children=[
            dcc.Dropdown(
                id={
                    'type': 'metric-ddown', 
                    'index': self.index
                    },
                options=[
                    {"label": "Visits", "value": "visits"},
                    {"label": "Visitors", "value": "visitors"},
                    {"label": "Pageviews", "value": "pageviews"},
                    {"label": "Views Per Visit", "value": "views_per_visit"},
                    {"label": "Bounce Rate", "value": "bounce_rate"},
                    {"label": "Visit Duration", "value": "visit_duration"},
                ],
                value="visitors"
            ),
            dcc.Dropdown(
                id={
                    'type': 'dimension-ddown',
                    'index': self.index
                },
                placeholder = f"view_{self.index}",
                options=[
                    {"label": "Entry Page", "value": "visit:entry_page"},
                    {"label": "Exit Page", "value": "visit:exit_page"},
                    {"label": "Source", "value": "visit:source"},
                    {"label": "Referrer", "value": "visit:referrer"},
                    {"label": "Channel", "value": "visit:channel"},
                    {"label": "Device", "value": "visit:device"},
                    {"label": "Browser", "value": "visit:browser"},
                    {"label": "OS", "value": "visit:os"},
                    {"label": "Country only", "value": "visit:country"},  
                ],  
            ),
            dcc.DatePickerRange(
                id={
                    'type': 'date-range',
                    'index': self.index
                },
                start_date=(datetime.today() - timedelta(days=7)).date(),
                end_date=datetime.today().date()
            ),
            dcc.Graph(id={'type': 'analytics-graph', 'index': self.index})
        ])
    