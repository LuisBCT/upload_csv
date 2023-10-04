# Upload CSV to Azure SQL

This REST API will take csv files to upload them to 3 different tables in Azure SQL 
## Tables in Azure SQL
- hired_employees
- jobs
- departments
## Requirements EndPoints
### POST
- /Uploads: Take a csv file and the name of the table
### GET
- /quarters: Number of employees hired for each job and department in 2021 divided by quarter
- /departments_hired: List of ids, name and number of employees hired of each department that hired more
employees than the mean of employees hired in 2021 for all the departments
