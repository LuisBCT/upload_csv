from fastapi import APIRouter
from config.db import get_conn, get_conn_alch
import pandas as pd
from io import BytesIO
import pyodbc

jobs = APIRouter()

@jobs.get("/jobs")
def get_jobs():
    rows= []
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobs")

        for row in cursor.fetchall():
            print(row.id,row.job)
            rows.append(f"{row.id},{row.job}")
        return rows
    
def load_jobs(file):
    csv_data = BytesIO(file)
    cols = ["id","job"]
    df = pd.read_csv(csv_data,header= None, names= cols)

    connection = get_conn_alch()
    df.to_sql("jobs", connection,schema= "dbo", if_exists= "append", index= False)
    return "ok"