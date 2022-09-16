#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state():
    """Display a HTML page"""
    return render_template('7-states_list.html',
                           states=storage.all(State))

@app.route('/states/<string:id>', strict_slashes=False)
def state_id(id=None):
    """Display a HTML page inside the tag BODY"""
    return render_template('9-states.html',
                           states=storage.all(State)
                           .get('State.{}'.format(id)))


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
