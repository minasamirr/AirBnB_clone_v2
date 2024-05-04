#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that returns a message when accessed.

    Returns:
        str: Message "Hello HBNB!".
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Route that returns a message when accessed.

    Returns:
        str: Message "HBNB".
    """
    return 'HBNB'


@app.route('/hbnb', strict_slashes=False)
def display_c(text):
    """
    Route that returns a message when accessed.

    Args:
        text (str): Text variable.

    Returns:
        str: Message "C " followed by the value of the text variable.
    """
    return 'c' + text.replace('_', '')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
