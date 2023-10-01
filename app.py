from fastapi import FastAPI

from routes.employees import employees

app = FastAPI()

app.include_router(employees)