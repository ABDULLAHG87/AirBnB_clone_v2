#!/usr/bin/python3
"""Run a flask web application that listen to host 0.0.0.0 at port 5000"""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def state():
    """Display a render html page with a list of all state"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route("/states/<id>", strict_slashes=False)
def state_by_id():
    """Display a render html page with cities of state"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=states, mode='id')
    return render_template('9-states.html', states=state, mode='none')


@app.teardown_appcontext
def teardown(exc):
    """Close current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
