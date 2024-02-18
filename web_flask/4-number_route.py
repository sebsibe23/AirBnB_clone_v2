#!/usr/bin/python3
"""Flask Application with Multiple View Functions

This code implements a Flask application with multiple
view functions that handle different routes.
Each view function returns a specific response based on the requested route.

"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Returns a greeting message.

    Returns:
        str: A greeting message.

    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """Returns a specific text.

    Returns:
        str: A specific text.

    """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Replaces underscores with spaces in the text and
    returns the modified text.

    Args:
        text (str): The input text.

    Returns:
        str: The modified text.

    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """Replaces underscores with spaces in the text and
    returns the modified text.
    If no text is provided, a default text is used.

    Args:
        text (str, optional): The input text. Defaults to 'is cool'.

    Returns:
        str: The modified text.

    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """Returns a message indicating whether the provided number is an integer.
    If the number is an integer, it is converted to a string.

    Args:
        n (int): The input number.

    Returns:
        str: A message indicating whether the number is an integer.

    """
    try:
        n = str(n)
        return '{} is a number'.format(n)
    except Exception as e:
        return 'An error occurred: {}'.format(str(e))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
