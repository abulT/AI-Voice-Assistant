import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM history")

rows = cursor.fetchall()

if len(rows) == 0:
    print("No records found.")
else:
    for row in rows:
        print(row)

conn.close()