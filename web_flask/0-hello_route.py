#!/usr/bin/python3
"""
This script will start a Flask web application,
whoch will be listening on 0.0.0.0, port 5000
Routes: /:display 'Hello HBNB!
strict_slashes=False must be an option in
route definition'
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """will print Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
