import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    filename TEXT,

    transcript TEXT,

    summary TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()
conn.close()

print("Database Created Successfully")