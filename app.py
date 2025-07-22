from flask import Flask, render_template, request
from encryption_util import encrypt_message
from database import insert_suggestion  # 🆕 import DB function

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    message = request.form["suggestion"]
    encrypted = encrypt_message(message)

    insert_suggestion(encrypted.decode())  # Save to DB

    return f"""
    ✅ Your encrypted suggestion has been saved securely!<br><br>
    <b>Encrypted Message:</b><br>
    <code>{encrypted.decode()}</code><br><br>
    🗃️ Stored safely in suggestions.db
    """

if __name__ == "__main__":
    app.run(debug=True)
