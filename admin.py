from encryption_util import decrypt_message
import sqlite3

def view_suggestions():
    conn = sqlite3.connect("suggestions.db")
    c = conn.cursor()
    c.execute("SELECT id, message FROM suggestions")
    rows = c.fetchall()
    conn.close()

    print("\n🔓 Decrypted Suggestions:\n")
    for row in rows:
        decrypted = decrypt_message(row[1].encode())
        print(f"{row[0]}. {decrypted}")

if __name__ == "__main__":
    view_suggestions()
