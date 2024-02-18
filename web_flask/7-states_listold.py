#!/usr/bin/python3
"""Flask Application with Functionality

This code implements a Flask application with
a route that performs a specific task.

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


@app.route('/do_something')
def do_something():
    """Performs a specific task and returns a message.

    Returns:
        str: A message indicating that the task has been performed.

    """
    # Add your code here to perform the desired task

    return 'Task has been performed.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
