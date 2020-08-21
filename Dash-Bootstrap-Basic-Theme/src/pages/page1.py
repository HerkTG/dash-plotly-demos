import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import datetime
import numpy as np

#START-HEATMAP-COMPONENT
# np.random.seed(1)

# programmers = ['Alex','Nicole','Sara','Etienne','Chelsea','Jody','Marianne']

# base = datetime.datetime.today()
# dates = base - np.arange(180) * datetime.timedelta(days=1)
# z = np.random.poisson(size=(len(programmers), len(dates)))

# fig = go.Figure(data=go.Heatmap(
#         z=z,
#         x=dates,
#         y=programmers,
#         colorscale='Viridis'))

# fig.update_layout(
#     title='GitHub commits per day',
#     xaxis_nticks=36)
#END-HEATMAP-COMPONENT

page1 = html.Div(
    [
        html.H2("Plotly Widgets 1"),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        "This is column 1",
                        style={"height": "400px", "border-style": "solid"},
                    ),
                    md=4,
                ),
                dbc.Col(
                    html.Div(
                        "This is column 1",
                        style={"height": "400px", "border-style": "solid"},
                    ),
                    md=8,
                ),
            ],
            no_gutters=True,
        ),
        html.Br(),
        html.H4("Plotly Widgets 2"),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        "This is column 1",
                        style={"height": "300px", "border-style": "solid"},
                    ),
                    md=6,
                ),
                dbc.Col(
                    html.Div(
                        "This is column 2",
                        style={"height": "300px", "border-style": "solid"},
                    ),
                    md=6,
                ),
            ],
            no_gutters=True,
        ),
    ]
)

def get_page1():
    return page1