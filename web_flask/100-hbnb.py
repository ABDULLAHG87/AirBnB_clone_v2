#!/usr/bin/python3
"""Run a flask web application that listen to host 0.0.0.0 at port 5000"""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display a render html page of hbnb filter"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Close current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
