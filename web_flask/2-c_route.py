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
        str: A greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Route that returns a message when accessed.

    Returns:
        str: A message "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Route that returns a message when accessed.

    Args:
        text (str): The text variable appended to "C".

    Returns:
        str: The message "C " followed by the value of the text variable
             (with underscores replaced by spaces).
    """
    return "C {}".format(escape(text).replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
