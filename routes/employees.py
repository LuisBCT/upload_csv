from fastapi import APIRouter
from config.db import get_conn, get_conn_alch
import pandas as pd
from io import BytesIO
import pyodbc

employees = APIRouter()

@employees.get("/employees")
def get_employees():
    rows= []
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hired_employees")

        for row in cursor.fetchall():
            print(row.id,row.name, row.hired_datetime, row.department_id, row.job_id)
            rows.append(f"{row.id},{row.name},{row.hired_datetime},{row.department_id},{row.job_id}")
        return rows
    
def load_employees(file):
    csv_data = BytesIO(file)
    cols = ["id","name","hired_datetime","department_id","job_id"]
    df = pd.read_csv(csv_data,header= None, names= cols)

    connection = get_conn_alch()
    #df2 = pd.read_sql_query("SELECT * FROM hired_employees", connection)
    df.to_sql("hired_employees", connection,schema= "dbo", if_exists= "append", index= False)
    return "ok"