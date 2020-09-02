import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_cytoscape as cyto

myGraph = cyto.Cytoscape(
    id='cytoscape-compound',
    layout={'name': 'preset'},
    style={'width': '100%', 'height': '100%'},
    stylesheet=[
        {
            'selector': 'node',
            'style': {'content': 'data(label)'}
        },
        {
            'selector': '.countries',
            'style': {'width': 5}
        },
        {
            'selector': '.cities',
            'style': {'line-style': 'dashed'}
        }
    ],
    elements=[
        # Parent Nodes
        {
            'data': {'id': 'us', 'label': 'United States'}
        },
        {
            'data': {'id': 'can', 'label': 'Canada'}
        },

        # Children Nodes
        {
            'data': {'id': 'nyc', 'label': 'New York', 'parent': 'us'},
            'position': {'x': 100, 'y': 100}
        },
        {
            'data': {'id': 'sf', 'label': 'San Francisco', 'parent': 'us'},
            'position': {'x': 100, 'y': 200}
        },
        {
            'data': {'id': 'mtl', 'label': 'Montreal', 'parent': 'can'},
            'position': {'x': 400, 'y': 100}
        },

        # Edges
        {
            'data': {'source': 'can', 'target': 'us'},
            'classes': 'countries'
        },
        {
            'data': {'source': 'nyc', 'target': 'sf'},
            'classes': 'cities'
        },
        {
            'data': {'source': 'sf', 'target': 'mtl'},
            'classes': 'cities'
        }
    ]
),

page = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            dbc.Row(
                                dbc.InputGroup(
                                    [
                                        dbc.Input(
                                            id='input-group-button-input', placeholder='Enter Info', value=""),
                                        dbc.InputGroupAddon(
                                            dbc.Button(
                                                'Submit', id='input-group-button', n_clicks=0),
                                            addon_type='append'
                                        ),
                                    ],
                                ),
                                style={'width': '100%', 'height': '50px',
                                       'margin-bottom': '5px'}
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        # html.Img(
                                        #     src='https://banner2.cleanpng.com/20180329/zue/kisspng-computer-icons-user-profile-person-5abd85306ff7f7.0592226715223698404586.jpg', height='150px'),
                                        width=4,
                                        style={"border-style": "solid"},
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            id='output-panel',
                                        ),
                                        width=8,
                                        style={"border-style": "solid"},
                                    ),
                                ],
                                style={'width': '100%', 'height': '150px',
                                       'margin-bottom': '10px', "border-style": "solid"}
                            ),
                            dbc.Row(
                                html.Div(
                                    "Test",
                                    style={"height": "100%"},
                                ),
                                style={'width': '100%', 'height': '150px',
                                       'margin-bottom': '10px', "border-style": "solid"}
                            ),
                            dbc.Row(
                                html.Div(
                                    myGraph,
                                    style={"height": "100%", 'width': '100%'},
                                ),
                                style={'width': '100%', 'height': '375px',
                                       "border-style": "solid"}
                            ),
                        ],
                    ),
                    width=8,
                ),
                dbc.Col(
                    html.Div(
                        id='timeline-div',
                    ),
                    width=4,
                    style={'width': '100%', 'height': '750px',
                           "border-style": "solid"}
                ),
            ],
        ),
    ]
)


def get_page():
    return page
