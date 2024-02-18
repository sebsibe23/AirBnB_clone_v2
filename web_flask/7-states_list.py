#!/usr/bin/python3
"""Flask Application with Functionality

This code implements a Flask application with
a route that performs a specific task.

"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)

    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
