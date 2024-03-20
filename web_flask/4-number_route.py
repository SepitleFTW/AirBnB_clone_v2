#!/usr/bin/python3
"""Initiates a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Showcases 'Greetings, Esteemed HBNB!'.
    /hbnb: Exemplifies 'HBNB'.
    /c/<text>: Portrays 'C' followed by the value of <text>.
    /python/(<text>): Exhibits 'Python' followed by the value of <text>.
    /number/<n>: Illustrates 'n is a number' solely if n be an integer.
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Showcases 'Greetings, Esteemed HBNB!'."""
    return "Greetings, Esteemed HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Exemplifies 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Portrays 'C' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Exhibits 'Python' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Illustrates 'n is a number' solely if n be an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
