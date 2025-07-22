from flask import Flask, render_template_string, request, redirect
import sqlite3
from cryptography.fernet import Fernet

app = Flask(__name__)

# Load key
with open("secret.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

# Admin page template
admin_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Admin WhisperBox 💼</title>
</head>
<body style="background-color:#fef6f8;font-family:sans-serif;">
    <h2>🔐 All Whispered Messages</h2>
    {% for msg in suggestions %}
        <div style="border:1px solid #ccc; margin:10px; padding:10px;">
            <p><strong>Code:</strong> {{ msg[0] }}</p>
            <p><strong>Message:</strong> {{ msg[1] }}</p>
            <form method="post">
                <input type="hidden" name="code" value="{{ msg[0] }}">
                <textarea name="reply" rows="2" cols="40" placeholder="Reply here..." required></textarea>
                <br><button type="submit">Send Reply</button>
            </form>
            {% if msg[2] %}
                <p style="color:green;"><strong>Replied:</strong> {{ msg[2] }}</p>
            {% endif %}
        </div>
    {% endfor %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def admin():
    conn = sqlite3.connect('suggestions.db')
    c = conn.cursor()

    if request.method == 'POST':
        code = request.form['code']
        reply = request.form['reply']
        c.execute("UPDATE suggestions SET reply=? WHERE code=?", (reply, code))
        conn.commit()

    c.execute("SELECT code, message, reply FROM suggestions")
    rows = c.fetchall()

    # Decrypt messages
    suggestions = []
    for code, enc_msg, reply in rows:
        try:
            decrypted_msg = fernet.decrypt(enc_msg).decode()
        except:
            decrypted_msg = "[Unable to decrypt]"
        suggestions.append((code, decrypted_msg, reply))

    conn.close()
    return render_template_string(admin_template, suggestions=suggestions)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
