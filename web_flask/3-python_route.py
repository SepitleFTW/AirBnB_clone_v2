#!/usr/bin/python3
"""Commences a Flask web application.

The application doth hearken on 0.0.0.0, port 5000.
Routes:
    /: Doth present 'Salutations, good HBNB!'.
    /hbnb: Doth present 'HBNB'.
    /c/<text>: Doth present 'C' followed by the value of <text>.
    /python/(<text>): Doth present 'Python' followed by the value of <text>.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):

    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
