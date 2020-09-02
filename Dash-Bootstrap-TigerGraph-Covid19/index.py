"""
This is a basic multi-page Dash app using Bootstrap.
"""
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import src.components.navbar as nb
import src.components.sidebar as sb
import pyTigerGraph as tg
import plotly.express as px
import json
import pandas as pd
import src.pages.patientView as p1
import src.pages.mapExplore as p3
import src.pages.dataStatistics as p4
import src.pages.globalView as p2
import src.pages.about as p5
from dash.dependencies import Input, Output, State
from datetime import datetime

# link fontawesome to get the chevron icons
FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"

# setup stylesheets
app = dash.Dash(external_stylesheets=[dbc.themes.LUX, FA])

# setup parameters
navbar = nb.get_navbar()
sidebar = sb.get_sidebar()
patientView = p1.get_page()
globalView = p2.get_page()
mapView = p3.get_page()
dataView = p4.get_page()
aboutView = p5.get_page()


'''
TigerGraph Connection Parameters:
'''

hostname = "https://tigerdashcovid.i.tgcloud.io"
username = "tigergraph"
graphname = "MyGraph"
password = "tigergraph"
# conn = None
try:
    conn = tg.TigerGraphConnection(host=hostname,
                                   graphname=graphname,
                                   username=username,
                                   password=password,
                                   useCert=True)
    secret = conn.createSecret()
    token = conn.getToken(secret, setToken=True)

    # print(conn.gsql('ls'))
except Exception as e:
    print('There was an error. Make sure to start your box and try again')


# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), navbar, sidebar, content])


def getPatientData(userID):
    q = conn.runInstalledQuery("getPatientInfo", {'p': userID})
    patientID = q[0]['Patient'][0]['v_id']
    patientSex = q[0]['Patient'][0]['attributes']['sex']
    patientBirthYear = q[0]['Patient'][0]['attributes']['birth_year']
    patientAge = datetime.now().year - patientBirthYear
    patientDeceased = False if q[0]['Patient'][0]['attributes']['deceased_date'].startswith(
        '1970') else True
    patientCountry = q[0]['Patient_Locations'][2]['v_id']
    patientProvince = q[0]['Patient_Locations'][0]['v_id']
    patientCity = q[0]['Patient_Locations'][1]['v_id']
    return patientID, patientSex, patientAge, patientDeceased, patientBirthYear, patientCountry, patientProvince, patientCity


def getPatientDates(userID):
    q = conn.runInstalledQuery("getPatientTimeline", {'p': userID})
    # print(str(q))
    # patientDates = []
    # patientDateLabels = []
    divs = []

    for x, y in q[0]['Seed'][0]['attributes'].items():
        # patientDateLabels.append(x)
        # patientDates.append(y)
        divs.append(
            html.H5(f"Date: {y.split(' ')[0]} ---- {x}")
        )

    for event in q[0]['results']:
        # patientDates.append(event['attributes']['visited_date'])
        # patientDateLabels.append(event['attributes']['travel_type'])
        divs.append(
            html.H5(f"Date: {event['attributes']['visited_date'].split(' ')[0]} ---- Travel Event : {event['attributes']['travel_type']}")
        )

    return divs


@app.callback(Output('timeline-div', 'children'), [Input(component_id="input-group-button", component_property="n_clicks")], [State("input-group-button-input", "value")])
def getPatientTimeline(n_clicks, userID):
    if n_clicks != 0:
        try:
            divs = getPatientDates(userID)
            patientTimeline = html.Div(
                children=divs
            )
            return patientTimeline
        except Exception as e:
            return [html.Br(), html.P("Please enter Valid Patient ID", style={'color': 'red'})]


@app.callback(Output("output-panel", "children"), [Input(component_id="input-group-button", component_property="n_clicks")], [State("input-group-button-input", "value")])
def getPatientInfo(n_clicks, userID):
    if n_clicks != 0:
        try:
            id, sex, age, deceased, birthYear, country, province, city = getPatientData(
                userID)
            dec = 'T' if deceased else 'F'
            patientData = html.Div(
                [
                    html.H5(f'Patient ID: {id}'),
                    html.H5(
                        f'Sex: {sex} Age: {age} DOB: {birthYear} Deceased: {dec}'),
                    html.H5(
                        f'Country: {country} Province: {province} City: {city}'),

                ],
                style={'height': '100%', 'width': '100%',
                       'padding': '5px 0 0 0'},
            )
            return patientData
        except Exception as e:
            return [html.Br(), html.P("Please enter Valid Patient ID", style={'color': 'red'})]


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 6)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False, False, False
    return [pathname == f"/page-{i}" for i in range(1, 6)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return html.P(patientView)
    elif pathname == "/page-2":
        return html.P(globalView)
    elif pathname == "/page-3":
        return html.P(mapView)
    elif pathname == "/page-4":
        return dataView
    elif pathname == "/page-5":
        return aboutView

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=8881)
