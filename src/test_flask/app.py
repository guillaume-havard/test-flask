from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>Main page</p>"

@app.route("/hello")
def hello_world():
    return "<p>Coucou</p>"

@app.route("/hello/<string:name>")
def hello_name(name: str):
    return f"<p>Coucou {escape(name)}</p>"

@app.route("/id/<int:id>")
def hello_id(id: int):
    return f"<p>Coucou n°:{id}</p>"    