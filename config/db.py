import pyodbc
import urllib
from sqlalchemy import create_engine

def get_conn():
    conn = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};Server=tcp:testserverlct.database.windows.net,1433;Database=sampledb;Uid=luis;Pwd=LCT#10180;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    return conn

def get_conn_alch():
    params = urllib.parse.quote_plus(r'Driver={ODBC Driver 18 for SQL Server};Server=tcp:testserverlct.database.windows.net,1433;Database=sampledb;Uid=luis;Pwd=LCT#10180;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

    conn_str = f"mssql+pyodbc:///?odbc_connect={params}"
    engine_azure = create_engine(conn_str,echo=True)
    return engine_azure