#!/usr/bin/python3
""" 7-states_list.py
Module that starts a Flask web application
and lists all State instances from a database
"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """states_list
    Function that displays a HTML page with a list of all
    State objects from a database
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """teardown_db
    Function that removes the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
