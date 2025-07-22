import sqlite3

conn = sqlite3.connect("suggestions.db")
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("✅ Table created successfully!")
