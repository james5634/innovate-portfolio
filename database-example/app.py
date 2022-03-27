import sqlite3
from flask import Flask, render_template, url_for, redirect, request, flash, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id): #for deleting post
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id)).fetchone
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route("/")
def home():
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return render_template("index.html", posts=posts)

@app.route("/create/", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required.")
        elif not content:
            flash("Content is required.")
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for("home"))

    return render_template("create.html")

@app.route("/<int:id>/edit/", methods=("GET","POST"))
def edit(id):
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if not title:
            flash("Title is required.")
        elif not content:
            flash("Content is required.")
        else:
            conn = get_db_connection()
            conn.execute("UPDATE posts SET title =?, content = ?" "WHERE id = ?", (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for("home"))
        return redirect(url_for("edit.html", post=post))



if __name__ == "__main__":
    app.run(debug=True, port=8000)