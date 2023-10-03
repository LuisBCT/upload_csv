from fastapi import APIRouter
from config.db import get_conn, get_conn_alch
import pandas as pd
from io import BytesIO
import pyodbc

departments = APIRouter()

@departments.get("/departments")
def get_departments():
    rows= []
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM departments")

        for row in cursor.fetchall():
            print(row.id,row.department)
            rows.append(f"{row.id},{row.department}")
        return rows
    
# def load_departments(file):
#     csv_data = BytesIO(file)
#     cols = ["id","department"]
#     df = pd.read_csv(csv_data,header= None, names= cols)

#     connection = get_conn_alch()
#     df.to_sql("departments", connection,schema= "dbo", if_exists= "append", index= False)
#     return "ok"