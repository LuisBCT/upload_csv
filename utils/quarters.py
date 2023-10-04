from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from config.db import get_conn, get_conn_alch
import pandas as pd


quarters = APIRouter()

@quarters.get("/quarters", response_class=HTMLResponse)
def get_quarters():
    connection = get_conn_alch()
    df_employees = pd.read_sql_query("SELECT * FROM hired_employees", connection)
    df_jobs = pd.read_sql_query("SELECT * FROM jobs", connection)
    df_dep = pd.read_sql_query("SELECT * FROM departments", connection)

    df_employees['hired_datetime'] = pd.to_datetime(df_employees['hired_datetime'])
    df_employees_2021 = df_employees[df_employees['hired_datetime'].dt.year == 2021]
    df_employees_2021['quarter'] = df_employees_2021['hired_datetime'].dt.to_period("Q").astype(str)
    df_employees_2021['quarter'] = 'Q' + df_employees_2021['quarter'].str.split('Q').str[1]

    result_df = pd.merge(df_employees_2021, df_dep, left_on='department_id', right_on='id', how='inner')
    result_df = pd.merge(result_df, df_jobs, left_on='job_id', right_on='id', how='inner')
    result_df = result_df.pivot_table(index=['department', 'job'], columns='quarter', values='id', aggfunc='count', fill_value=0).reset_index()
    result_df = result_df.sort_values(by=['department', 'job'], ascending=[True, True])

    #data = result_df.to_dict(orient='records')
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
    return HTMLResponse(content=rendered_html)