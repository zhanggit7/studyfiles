import json
import pyodbc

# -----------------------------
# 1. JSON file
# -----------------------------
json_file = r"C:\Study\python\employees.json"

# -----------------------------
# 2. Read JSON
# -----------------------------
with open(json_file, "r", encoding="utf-8") as file:
    employees = json.load(file)

print(f"Read {len(employees)} records from JSON")

# -----------------------------
# 3. SQL Server connection
# -----------------------------
server = r"XFZHP\SQLEXPRESS"
database = "TestDB"

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# -----------------------------
# 4. Insert data
# -----------------------------
sql = """
INSERT INTO dbo.Employee
(
    EmployeeID,
    FirstName,
    LastName,
    Department,
    Salary
)
VALUES (?, ?, ?, ?, ?)
"""

for employee in employees:

    cursor.execute(
        sql,
        employee["EmployeeID"],
        employee["FirstName"],
        employee["LastName"],
        employee["Department"],
        employee["Salary"]
    )

# -----------------------------
# 5. Commit
# -----------------------------
conn.commit()

print(f"Successfully inserted {len(employees)} records")

# -----------------------------
# 6. Close connection
# -----------------------------
cursor.close()
conn.close()