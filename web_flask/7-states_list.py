#!/usr/bin/python3
"""Initiates a Flask web application.

The application is set to listen on 0.0.0.0, port 5000.
Routes:
    /states_list: An HTML page containing a list of all State objects in DBStorage.
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)



@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.

    States are arranged alphabetically.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Closes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
