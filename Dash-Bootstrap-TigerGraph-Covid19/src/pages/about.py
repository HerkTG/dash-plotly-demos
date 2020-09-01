import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import urllib.request
from pandas.tseries.offsets import *

page = html.Div(
    [
        html.H2("Graphistry Visualization")
    ]
)


def get_page():
    return page
