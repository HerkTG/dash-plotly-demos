"""
This is a basic multi-page Dash app using Bootstrap.
"""
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import src.components.navbar as nb
import src.components.sidebar as sb
import pyTigerGraph as tg
import json
import src.pages.page1 as p1
from dash.dependencies import Input, Output, State

# link fontawesome to get the chevron icons
FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"

# setup stylesheets
app = dash.Dash(external_stylesheets=[dbc.themes.LUX, FA])

# setup parameters
navbar = nb.get_navbar()
sidebar = sb.get_sidebar()
page1 = p1.get_page1()


'''
TigerGraph Connection Parameters:
'''

hostname = "https://payment-fraud.i.tgcloud.io"
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


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("userIdOutput", "children"), [Input(component_id="userIdSubmit", component_property="n_clicks")], [State("userId", "value")])
def output_text(n_clicks, userID):
    if n_clicks != 0:
        try:
            q = conn.runInstalledQuery("getUserInfo", {'userID': userID})
            q = json.load(q)
            return [html.Br(), html.P(q)]
        except Exception as e:
            return [html.Br(), html.P("Please enter Valid Patient ID", style={'color': 'red'})]
    else:
        return


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return html.P(page1)
    elif pathname == "/page-2":
        return html.P("This is the content of page 2. Yay!")
    elif pathname == "/page-3":
        return html.P(conn.gsql('ls'))
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=8888)
