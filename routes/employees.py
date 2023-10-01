from fastapi import APIRouter
from config.db import get_conn

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