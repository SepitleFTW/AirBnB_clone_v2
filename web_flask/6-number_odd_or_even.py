#!/usr/bin/python3
"""Commence a Flask web application.

The application attends on 0.0.0.0, port 5000.
Routes:
    /: Shows 'Salutations, Esteemed HBNB!'.
    /hbnb: Demonstrates 'HBNB'.
    /c/<text>: Illustrates 'C' pursued by the value of <text>.
    /python/(<text>): Exhibits 'Python' pursued by the value of <text>.
    /number/<n>: Presents 'n is a number' solely if <n> is an integer.
    /number_template/<n>: Showcases an HTML page solely if <n> is an integer.
        - Exemplifies the value of <n> in the body.
    /number_odd_or_even/<n>: Displays an HTML page solely if <n> is an integer.
        - Mentions whether <n> is even or odd in the body.
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
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
    return  "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
