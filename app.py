from fastapi import FastAPI, UploadFile, File

from routes.employees import employees, load_employees
from routes.departments import departments,load_departments
from routes.jobs import jobs,load_jobs

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...), table:str = ""):
    load_tables = {
        "hired_employees":load_employees,
        "jobs": load_jobs,
        "departments": load_departments
    }
    #file_ext = file.filename.split(".").pop()
    #return {"file_ext": file_ext, "load_table":table}
    content = await file.read()
    load_function = load_tables.get(table)
    result = load_function(content)
    return result

app.include_router(employees)
app.include_router(departments)
app.include_router(jobs)