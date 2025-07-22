from flask import Flask, request, render_template_string
from cryptography.fernet import Fernet
import sqlite3
import uuid

app = Flask(__name__)

# Load your encryption key
with open('secret.key', 'rb') as file:
    key = file.read()

fernet = Fernet(key)

# Simple HTML form
form_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>WhisperBox ✨</title>
</head>
<body style="background-color:#fdf6f0;font-family:sans-serif;text-align:center;">
    <h1>💌 Whisper Something...</h1>
    <form method="post">
        <textarea name="message" rows="6" cols="40" placeholder="Your anonymous message..." required></textarea><br><br>
        <button type="submit">Send</button>
    </form>

    {% if code %}
    <h3>✅ Your message was sent!</h3>
    <p>🔐 Save this code to check reply later: <strong>{{ code }}</strong></p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def suggestion():
    code = None
    if request.method == 'POST':
        message = request.form['message']
        encrypted = fernet.encrypt(message.encode())
        code = str(uuid.uuid4())[:8]  # Generate a short unique code

        # Save to DB
        conn = sqlite3.connect('suggestions.db')
        c = conn.cursor()
        c.execute("INSERT INTO suggestions (message, code) VALUES (?, ?)", (encrypted, code))
        conn.commit()
        conn.close()

    return render_template_string(form_html, code=code)

if __name__ == '__main__':
    app.run(debug=True)
