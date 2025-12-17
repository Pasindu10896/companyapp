import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('inspection.db')
c = conn.cursor()

c.execute("SELECT * FROM inspections")
rows = c.fetchall()

if rows:
    headers = [description[0] for description in c.description]
    print(tabulate(rows, headers=headers, tablefmt="grid"))
else:
    print("⚠️ No records found in the inspections table.")

conn.close()
