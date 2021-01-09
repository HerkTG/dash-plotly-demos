import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import graphistry as graphistry
from config import graphistry_un, graphistry_pw
import connect
import pandas as pd
import plotly.figure_factory as ff

graphistry.register(api=3, protocol="https", server="hub.graphistry.com", username=graphistry_un, password=graphistry_pw)
g = None
conn = connect.getConnection()
source_col = []
dest_col = []
source_type = []
dest_type = []


def type_to_color(t):
    mapper = {'Patient': 0xFF000000}
    if t in mapper:
        return mapper[t]
    else:
        return 0xFFFFFF00


def generateGraph():
    try:
        q = conn.runInstalledQuery("getGraph")
        edges = q[0]['@@AllE']
        # nodes = q[0]['AllV']
        for edge in edges:
            source_col.append(edge['from_id'])
            source_type.append(edge['from_type'])
            dest_col.append(edge['to_id'])
            dest_type.append(edge['to_type'])

        df = pd.DataFrame(list(zip(source_col, source_type, dest_col, dest_type)), columns=['Source', 'Source_Type', 'Destination', 'Destination_Type'])
        df2 = df.assign(my_color=df['Source_Type'].apply(lambda v: type_to_color(v)))
        g = graphistry.edges(df2).bind(edge_color='my_color', source='Source', destination='Destination')
        g = g.settings(url_params={'bg': '%23FFFFFF'})
        graph = g.plot(render=False)
        graph_viz = html.Iframe(src=graph, height='600', width='100%')
        return graph_viz
    except Exception as e:
        return html.P('There was an error. Double check your username and password in your config file')


graph = generateGraph()
# fig = ff.create_table(table)

page = html.Div(
    [
        html.H2("Graphistry Visualization"),
        graph
    ],
    # style={'height': '100vh'}
)


def get_page():
    return page
