import sqlite3
conn = sqlite3.connect('employees.db')
cur = conn.cursor()
for row in cur.execute("select * from employees"):
    print(row)
conn.close()
#ethan collins 4/29/2025