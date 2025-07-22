import sqlite3

def init_db():
    conn = sqlite3.connect("suggestions.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_suggestion(message):
    conn = sqlite3.connect("suggestions.db")
    c = conn.cursor()
    c.execute("INSERT INTO suggestions (message) VALUES (?)", (message,))
    conn.commit()
    conn.close()
