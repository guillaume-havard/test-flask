from faker import Faker
from faker.providers import date_time, person, python
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


@app.route("/users")
def users_administration():
    """Users administration page."""
    fake = Faker()
    fake.add_provider(person)
    fake.add_provider(python)
    fake.add_provider(date_time)
    users = []
    for _ in range(10):
        users.append(
            {
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "age": fake.pyint(18, 80),
                "member_since": fake.date("%d/%m/%Y"),
            }
        )

    return render_template("users.html", users=users)
