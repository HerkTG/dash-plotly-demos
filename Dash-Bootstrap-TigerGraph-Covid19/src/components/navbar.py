import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="/page-5")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Patient", href="/page-1"),
                dbc.DropdownMenuItem("Global", href="/page-2"),
                dbc.DropdownMenuItem("Map", href="/page-3"),
                dbc.DropdownMenuItem("Data", href="/page-4"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
            right=True,
        ),
    ],
    brand="TigerGraph",
    brand_href="#",
    color="#ef6c00",
    dark=False,
    fluid=True,
)


def get_navbar():
    return navbar
