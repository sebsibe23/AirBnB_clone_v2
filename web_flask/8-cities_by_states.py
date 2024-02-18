#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.

Routes:
    /cities_by_states: HTML page with a list of
    all states and cities.

This script starts a Flask web application that provides
a route, /cities_by_states,
which returns an HTML page displaying a list of all states
and their related cities.
The states and cities are sorted by name.

The application listens on the IP address 0.0.0.0,
allowing it to accept requests from
any available network interface. It uses port 5000 as the default
port for incoming
connections.

The route "/cities_by_states" triggers the cities_by_states function.
This function
retrieves all the states from the storage module using the storage.
all("State") method.
It then passes the states to the render_template function
along with the name of the
HTML template file, "8-cities_by_states.html".

In case an exception occurs during the execution of the
cities_by_states function, the
exception is caught and an error message is returned,
providing details about the
exception. This helps with error handling and provides
meaningful error messages to
users.

The teardown_appcontext function is used as a decorator with the @app.
teardown_appcontext
annotation. This function is called when the application context is torn down,
allowing
for any necessary cleanup operations. In this case,
it closes the SQLAlchemy session.

To run this Flask application, execute the script using Python 3.
For example, if the
script is saved as app.py, run it with the command "python3 app.py".
The application
will be accessible at http://0.0.0.0:5000/cities_by_states.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Displays an HTML page with a list of all states and related cities.
    States and cities are sorted by name.

    Exceptions:
        Exception: If an error occurs during the retrieval
        of states from storage.

    Returns:
        str: HTML page with the list of states and cities, or an error message.
    """
    try:
        states = storage.all("State")
        return render_template("8-cities_by_states.html", states=states)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
