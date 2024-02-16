#!/usr/bin/python3
"""
0. Script to start a Flask web application

Description:
    This script starts a Flask web application that serves a single route '/'.
    When the route is accessed, it returns the string 'Hello HBNB!'. The web
    application runs on the local host (0.0.0.0) and listens on port 5000.

Dependencies:
    - flask

Usage:
    - Execute the script to start the Flask web application. Access the route
      'http://localhost:5000/' on a web browser to see the output.

"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
    Returns some text.

    Description:
        This function is the handler for the route '/'. When the route is
        accessed, it returns the string 'Hello HBNB!'. The 'strict_slashes'
        parameter is set to False to allow accessing the route with or without
        a trailing slash.

    Returns:
        A string containing the text 'Hello HBNB!'.
    """

    return 'Hello HBNB!'


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
