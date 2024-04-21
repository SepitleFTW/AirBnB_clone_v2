#!/usr/bin/python3
"""Initializes a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)


def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)


def display_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)


def c(text):
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
