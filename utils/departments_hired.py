from fastapi import APIRouter,HTTPException
from fastapi.responses import HTMLResponse
from config.db import get_conn, get_conn_alch
import pandas as pd

departments_hired = APIRouter()
@departments_hired.get("/departments_hired", response_class=HTMLResponse)
def get_departments_hired():
    try:
        connection = get_conn_alch()
        df_employees = pd.read_sql_query("SELECT * FROM hired_employees", connection)
        df_jobs = pd.read_sql_query("SELECT * FROM jobs", connection)
        df_dep = pd.read_sql_query("SELECT * FROM departments", connection)

        df_employees['hired_datetime'] = pd.to_datetime(df_employees['hired_datetime'])

        hired_employees_2021 = df_employees[df_employees['hired_datetime'].dt.year == 2021]


        department_counts = hired_employees_2021.groupby('department_id')['id'].count().reset_index()
        department_counts.columns = ['department_id', 'hired']

        mean_employees = department_counts['hired'].mean()

        selected_departments = department_counts[department_counts['hired'] > mean_employees]

        result_df = pd.merge(selected_departments, df_dep, left_on='department_id', right_on='id', how='inner')
        result_df = result_df[['department_id', 'department', 'hired']]
        result_df = result_df.sort_values(by='hired', ascending=False)
        result_df['department_id'] = result_df['department_id'].astype(int)

        html_table = result_df.to_html(index=False)

        html_template = '''
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>DataFrame Table</title>
                    </head>
                    <body>
                        {{ table|safe }}
                    </body>
                    </html>
                    '''

        rendered_html = html_template.replace("{{ table|safe }}", html_table)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return HTMLResponse(content=rendered_html)
