from fastapi import APIRouter
from config.db import get_conn

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