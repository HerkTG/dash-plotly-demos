import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

page = html.Div(
    [
        html.H2("About the Authors"),
        html.H3('Akash Kaul'),
        dbc.Row(
            [
                dbc.Col(
                    html.H5(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('Website', href='https://akashkaul.com', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
                dbc.Col(
                    html.H5(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('LinkedIn', href='https://www.linkedin.com/in/akash-kaul-6a8063194/', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
                dbc.Col(
                    html.H5(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('GitHub', href='https://github.com/akash-kaul', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
                dbc.Col(
                    html.H5(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('Medium', href='https://medium.com/@akash_kaul', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
            ],
        ),
        html.H3('Jon Herke')
    ]
)


def get_page():
    return page
