#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Route that returns a message when accessed.

    Returns:
        str: A greeting message "Hello HBNB!".
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that returns a message when accessed.

    Returns:
        str: A message "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisamazing(text):
    """ Route that returns a message when accessed.

    Args:
        text (str): The text variable appended to "C".

    Returns:
        str: The message "C " followed by the value of the text variable
             (with underscores replaced by spaces).
    """
    return 'C' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonstyle(text=' is cool'):
    """
    Route that returns a message when accessed.

    Args:
        text (str): Text variable.

    Returns:
        str: Message "Python " followed by the value of the text variable.
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
