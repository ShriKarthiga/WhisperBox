from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# HTML Template
reply_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Check Your Reply 🌸</title>
</head>
<body style="background-color:#fffafc; font-family:Arial, sans-serif;">
    <h2>🔎 Whisperbox Reply Checker</h2>
    <form method="post">
        <label>Enter your Code:</label><br>
        <input type="text" name="code" required>
        <br><br>
        <button type="submit">Check Reply</button>
    </form>

    {% if reply is not none %}
        <hr>
        <h3>💌 Your Reply:</h3>
        {% if reply %}
            <p style="color:green;"><strong>{{ reply }}</strong></p>
        {% else %}
            <p style="color:red;">No reply yet. Please check again later 🙏</p>
        {% endif %}
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def check_reply():
    reply = None
    if request.method == 'POST':
        code = request.form['code']
        conn = sqlite3.connect('suggestions.db')
        c = conn.cursor()
        c.execute("SELECT reply FROM suggestions WHERE code=?", (code,))
        result = c.fetchone()
        reply = result[0] if result else None
        conn.close()

    return render_template_string(reply_template, reply=reply)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
