from fastapi import FastAPI

from routes.employees import employees
from routes.departments import departments
from routes.jobs import jobs

app = FastAPI()

app.include_router(employees)
app.include_router(departments)
app.include_router(jobs)