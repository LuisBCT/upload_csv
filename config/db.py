import pyodbc

def get_conn():
    conn = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};Server=tcp:testserverlct.database.windows.net,1433;Database=sampledb;Uid=luis;Pwd=LCT#10180;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    return conn
#cursor = conn.cursor()

#print("connected")