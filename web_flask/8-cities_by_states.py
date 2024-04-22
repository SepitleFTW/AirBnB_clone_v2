#!/usr/bin/python3
"""Initiates a Flask web application.

The application is set to listen on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: An HTML page presenting a list of all states and their related cities.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states and related cities.

    States and their cities are arranged alphabetically.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Closes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
