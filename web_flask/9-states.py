#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states7<states_id>", strict_slashes=False)
def states(state_id=None):
    """Display a HTML page"""
    states = storage.all(State)
    if state_id is not None:
        state_id = State + "." + state_id
    return render_template("9-states.html", states=states, state_id=state_id)


@app.route("/states/id", strict_slashes=False)
def states_id(id):
    """Display a HTML page"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", states=states)
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
