import pyTigerGraph as tg

hostname = "https://tigerdashcovid.i.tgcloud.io"
username = "tigergraph"
graphname = "MyGraph"
password = "tigergraph"
conn = None
try:
    conn = tg.TigerGraphConnection(host=hostname,
                                   graphname=graphname,
                                   username=username,
                                   password=password,
                                   useCert=True)
    secret = conn.createSecret()
    token = conn.getToken(secret, setToken=True)
except Exception as e:
    print('There was an error. Make sure to start your box and try again')


def getConnection():
    if conn is not None:
        return conn
