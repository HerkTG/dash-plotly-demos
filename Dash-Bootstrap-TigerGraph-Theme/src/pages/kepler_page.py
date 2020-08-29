import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import pandas as pd
import keplergl
import geopandas as gpd
import urllib.request
# from dateutil.relativedelta import relativedelta
from pandas.tseries.offsets import *


url = "https://docs.mapbox.com/help/data/stations.geojson"
download_file = urllib.request.urlretrieve(url, "stations.geojson")

def make_kepler_plot():
    map_data = gpd.read_file("stations.geojson")
    map_1 = keplergl.KeplerGl()
    map_1.add_data(data=map_data)
    map_1.save_to_html(file_name="map_test.html")

# make plot
make_kepler_plot()

kep_viz = html.Iframe(srcDoc = open('map_test.html').read(), height='800', width='100%')


# df = pd.read_csv('kepler.gl-data/nyctrips/data.csv')
# map1 = KeplerGl(height=500)


# def unix_time_millis(dt):
#     return (dt - epoch).total_seconds()
maxmarks = 13
tday = pd.Timestamp.today()  # gets timestamp of today
m1date = tday + DateOffset(months=-maxmarks + 1)  # first month on slider
datelist = pd.date_range(m1date, periods=maxmarks,
                         freq='M')  # list of months as dates
dlist = pd.DatetimeIndex(datelist).normalize()
tags = {}  # dictionary relating marks on slider to tags. tags are shown as "Apr', "May', etc
datevalues = {}  # dictionary relating mark to date value
x = 1
for i in dlist:
    # gets the string representation of next month ex:'Apr'
    tags[x] = (i + DateOffset(months=1)).strftime('%b')
    datevalues[x] = i
    x = x + 1

kepler_page = html.Div(
    [
        html.H2("Kepler Visualization"),
        kep_viz
        # dcc.RangeSlider(
        #     id='datetime_RangeSlider',
        #     updatemode='mouseup',  # don't let it update till mouse released
        #     min=1,
        #     max=15,
        #     value=[maxmarks - 5, maxmarks],
        #     marks=tags,
        #     pushable=1,
        # )
    ]
)


def get_page():
    return kepler_page
