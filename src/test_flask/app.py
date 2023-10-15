from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route("/")
def main():
    """Main page."""
    return render_template("index.html")


@app.route("/index")
def index():
    """Main page."""
    return redirect(url_for("main"))
