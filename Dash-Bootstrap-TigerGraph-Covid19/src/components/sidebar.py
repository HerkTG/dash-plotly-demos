import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "89px",
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "white",
}

sidebar = html.Div(
    [
        # html.H2("Sidebar", className="display-4"),
        html.H5("Dashboard"),
        html.Hr(),
        # html.P(
        #     "A simple sidebar layout with navigation links", className="lead"
        # ),
        dbc.Nav(
            [
                dbc.NavLink("Patient", href="/page-1", id="page-1-link"),
                dbc.NavLink("Global", href="/page-2", id="page-2-link"),
                dbc.NavLink("Map", href="/page-3", id="page-3-link"),
                dbc.NavLink("Data", href="/page-4", id="page-4-link"),
                dbc.NavLink("About", href="/page-5", id="page-5-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


def get_sidebar():
    return sidebar
