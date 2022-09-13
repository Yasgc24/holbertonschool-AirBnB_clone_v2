#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """Display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False, defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """Display “Python ”, followed by the value of the
    text variable (replace underscore _ symbols with a space)"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
