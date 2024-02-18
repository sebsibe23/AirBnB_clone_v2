#!/usr/bin/python3
"""
<<<<<<< HEAD
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


=======
starts a Flask web application
"""

from flask import Flask
>>>>>>> 724cfe6dd2d21fedeae11b441bd8b63e8ab80681
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
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
=======
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 724cfe6dd2d21fedeae11b441bd8b63e8ab80681
