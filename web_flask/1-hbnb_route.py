#!/usr/bin/python3
"""
1. Script to start a Flask web application with 2 commands

Description:
    This script starts a Flask web application that
    serves two routes - '/' and '/hbnb'.
    - When the route '/' is accessed, it returns the string 'Hello HBNB!'.
    - When the route '/hbnb' is accessed, it returns the string 'HBNB'.
    The web application runs on the local host (0.0.0.0)
    and listens on port 5000.

Dependencies:
    - flask

Usage:
    - Execute the script to start the Flask web application.
    - Access the route 'http://localhost:5000/' on a web browser
    to see the output 'Hello HBNB!'.
    - Access the route 'http://localhost:5000/hbnb'
    on a web browser to see the output 'HBNB'.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
    Returns some text.

    Returns:
        A string containing the text 'Hello HBNB!'.
    """

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """
    Return other text.

    Returns:
        A string containing the text 'HBNB'.
    """

    return 'HBNB'


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
