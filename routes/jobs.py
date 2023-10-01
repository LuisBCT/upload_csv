from fastapi import APIRouter
from config.db import get_conn

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