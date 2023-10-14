from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def main():
    """Main page."""
    return "<p>Main page</p>"


@app.route("/hello")
def hello_world():
    """Hello to everyone"""
    return "<p>Coucou</p>"


@app.route("/hello/<string:name>")
def hello_name(name: str):
    """Hellot to someone."""
    return f"<p>Coucou {escape(name)}</p>"


@app.route("/id/<int:uid>")
def hello_id(uid: int):
    """Hello to an id."""
    return f"<p>Coucou n°:{uid}</p>"
