from fastapi import FastAPI, UploadFile, File

from routes.employees import employees
from routes.departments import departments
from routes.jobs import jobs

app = FastAPI()

@app.post("/upload")
def upload(file: UploadFile = File(...), table:str = ""):
    file_ext = file.filename.split(".").pop()
    return {"file_ext": file_ext, "load_table":table}

app.include_router(employees)
app.include_router(departments)
app.include_router(jobs)