import sqlite3
from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return render_template("index.html", posts=posts)

@app.route("/create/", methods=("GET", "POST"))
def create():
    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)