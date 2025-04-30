###
# Change layout as you see fit

from dash import html, dcc

layout = html.Div(className='main-container', children=[
    html.Div(className='header', children=[
        html.Img(src='logo.png', className='logo'),
        html.H2('This is the Way')
    ]),
    html.Div(className='body', children=[
        dcc.Tabs(className="tabs-container", children=[
            dcc.Tab(label="Tab 1", className="custom-tab", children=[
                html.H1("My Dashboard"),
                html.Button("Add View", id="add-btn"), 
                html.Button("Remove view", id="delete-btn"),
                html.Div(id="view-container")
            ]),
            dcc.Tab(label="Tab 2", className="custom-tab", children=[]),
            dcc.Tab(label="Tab 3", className="custom-tab", children=[
                html.H3("Here lies a hidden Div"),
                html.Div(id='some-table'),
            ]),
            dcc.Tab(label="Tab 4", className="custom-tab", children=[
                html.Div(className='upload-buttons', children=[
                    html.Div([
                        html.H3("This is for Uploads"),
                        dcc.Upload(
                            id='upload',
                            accept='.xls, .xlsx',
                            max_size=5_000_000,
                            children=html.Div(
                                ['Drag and Drop or ', html.A('Select Files')]
                        )),
                    ]),   
                ])
            ]),
        ]),
    ]),
    html.Div(className='footer', children=[]),
])
