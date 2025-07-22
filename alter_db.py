import sqlite3

# Connect to your existing database
conn = sqlite3.connect('suggestions.db')
c = conn.cursor()

# Add new columns
try:
    c.execute("ALTER TABLE suggestions ADD COLUMN code TEXT")
    print("✅ 'code' column added.")
except sqlite3.OperationalError:
    print("⚠️ 'code' column already exists.")

try:
    c.execute("ALTER TABLE suggestions ADD COLUMN reply TEXT")
    print("✅ 'reply' column added.")
except sqlite3.OperationalError:
    print("⚠️ 'reply' column already exists.")

# Commit changes and close
conn.commit()
conn.close()
