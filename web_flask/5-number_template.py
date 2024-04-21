#!/usr/bin/python3
"""Initiates a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Showcases 'Greetings, Esteemed HBNB!'.
    /hbnb: Exemplifies 'HBNB'.
    /c/<text>: Portrays 'C' followed by the value of <text>.
    /python/(<text>): Exhibits 'Python' followed by the value of <text>.
    /number/<n>: Illustrates 'n is a number' solely if <n> is an integer.
    /number_template/<n>: Depicts an HTML page solely if <n> is an integer.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnbb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C " + text.replace("_", " ")


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def nooby_number(n):
    return f"<html><body><h1><Number: {n}</h1></body></html"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
