# from flask import Flask, render_template, url_for, redirect

# app = Flask(__name__)


import sqlite3
from flask import Flask, render_template, url_for, redirect, request, flash, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"

###########################################################

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/one")
def one():
    return render_template("one.html")

@app.route("/two")
def two():
    return render_template("two.html")

@app.route("/three")
def three():
    return render_template("three.html")

@app.route("/four")
def four():
    return render_template("four.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("page-not-found.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("internal-server-error.html"), 500

########################################

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()

    conn.close()
    if post is None:
        abort(404)
    return post

@app.route("/blog")
def blog():
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return render_template("blog.html", posts=posts)

@app.route("/create/", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title required.")
        elif not content:
            flash("Content required.")
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for("blog"))

    return render_template("blog-create.html")

@app.route("/<int:id>/edit/", methods=("GET", "POST"))
def edit(id):
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title required.")
        elif not content:
            flash("Content required.")
        else:
            conn = get_db_connection()
            conn.execute("UPDATE posts SET title = ?, content = ?" " WHERE id = ?", (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for("blog"))
    return render_template("blog-edit.html", post=post)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash(f"'{post['title']}' was successfully deleted!")
    return redirect(url_for('blog'))

########################################



if __name__ == "__main__":
    app.run(debug=True, port=8000)