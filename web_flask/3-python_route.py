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
def hello_hbnb():
    """Doth display 'Salutations, good HBNB!'."""
    return "Salutations, good HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Doth display 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Doth display 'C' followed by the value of <text>.

    Doth replace any underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Doth display 'Python' followed by the value of <text>.

    Doth replace any underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
