from cryptography.fernet import Fernet
import sqlite3

# Load the secret key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Get suggestion input from user
suggestion = input("Enter your suggestion: ")

# Encrypt the suggestion
encrypted = cipher.encrypt(suggestion.encode())

# Store it in SQLite
conn = sqlite3.connect('suggestions.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT
)
''')

c.execute("INSERT INTO suggestions (message) VALUES (?)", (encrypted,))
conn.commit()
conn.close()

print("✅ Your encrypted suggestion has been saved successfully!")
