#!/usr/bin/python3
"""
2. Script to start a Flask web application with 3 view functions

Description:
    This script starts a Flask web application that serves three routes - '/',
    '/hbnb', and '/c/<text>'.
    - When the route '/' is accessed, it returns the string 'Hello HBNB!'.
    - When the route '/hbnb' is accessed, it returns the string 'HBNB'.
    - When the route '/c/<text>' is accessed, it takes a variable 'text' and
      returns a string that starts with 'C ' followed by the value of 'text'
      after replacing underscores with spaces.
    The web application runs on the local host (0.0.0.0)
    and listens on port 5000.

Dependencies:
    - flask

Usage:
    - Execute the script to start the Flask web application.
    - Access the route 'http://localhost:5000/' on a web browser to see the
      output 'Hello HBNB!'.
    - Access the route 'http://localhost:5000/hbnb' on a web browser to see the
      output 'HBNB'.
    - Access the route 'http://localhost:5000/c/<text>' on a web browser,
      replacing '<text>' with any desired text, to see the output 'C <text>'.
      Underscores in the provided text will be replaced with spaces.
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
    Returns some text.

    Returns:
        A string containing the text 'Hello HBNB!'.
    """

    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """
    Returns other text.

    Returns:
        A string containing the text 'HBNB'.
    """

    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """
    Returns modified text.

    Parameters:
        text (str): The text provided in the route.

    Returns:
        A string containing the text 'C ' followed by the value of 'text' after
        replacing underscores with spaces.
    """

    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
