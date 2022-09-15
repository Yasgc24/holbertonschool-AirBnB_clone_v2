#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """Display a HTML page"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/id", strict_slashes=False)
def states_id(id):
    """Display a HTML page"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", states=states)
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
