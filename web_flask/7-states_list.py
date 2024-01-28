#!/usr/bin/python3
"""Run a flask web application that listen to host 0.0.0.0 at port 5000"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a render html page with a lis of all state"""
    states = storage.all('State')
    return render_template('7-states_list.html',states=states)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    app.run(host ="0.0.0.0", port=5000)
