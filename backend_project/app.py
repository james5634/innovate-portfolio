##################################
#! FLASK APPLICATION
##################################
#extensions that alllow specific class and functions
from flask import Flask, Blueprint, render_template, url_for, redirect

#a 'bluerint' if the website structure
views = Blueprint(__name__, "views")

#the wesite is defined as a flask app and the url prefix is set to '/'.
app =Flask(__name__)
app.register_blueprint(views, url_prefix = "/")

##################################
#! APPLICATION PAGES
##################################

#this is how the homepage is accessed.
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/two")
def test_page():
    return render_template("index.html")

@app.route("/three")
def three_page():
    return render_template("index.html")

@app.route("/four")
def four_page():
    return render_template("index.html")

@app.route("/five")
def five_page():
    return render_template("index.html")

@app.route("/admin")
def admin_page():
    return render_template("index.html")


##################################

@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))

@app.route("/javascript")
def javascript_redirect():
    return redirect(url_for("home"))

@app.route("/js")
def js_redirect():
    return redirect(url_for("home"))

##################################

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

##################################

#debugging is activated and the prject is set to hosted on port 8000 (debigging should only be used in testing)
if __name__ == "__main__":
    app.run(debug = True, port =8000)

##################################