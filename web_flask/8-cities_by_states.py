#!/usr/bin/python3
"""Run a flask web application that listen to host 0.0.0.0 at port 5000"""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route("/cities-by_states", strict_slashes=False)
def cities_by_states():
    """Display a render html page with a lis of all state"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Close current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
