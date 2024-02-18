#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.

Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.

This script starts a Flask web application that provides two routes:
- The "/states" route displays an HTML page with a list of all
  State objects.
- The "/states/<id>" route displays an HTML page with information
  about a specific state identified by the given <id>.

The application listens on the IP address 0.0.0.0, allowing it
to accept requests from any available network interface. It uses
port 5000 as the default port for incoming connections.

The "/states" route triggers the `states` function, which retrieves
all the states from the storage module using the `storage.all("State")`
method. The retrieved states are then passed to the `render_template`
function along with the name of the HTML template file,
"9-states.html". The states are sorted by name.

The "/states/<id>" route triggers the `states_id` function, which
searches for a state with the given <id> in the storage module. If
the state is found, it is passed to the `render_template` function
along with the template file name. If the state is not found, the
template is rendered without any state information.

In case an exception occurs during the execution of the `states`
or `states_id` functions, the exception is caught, and an error
message is returned, providing details about the exception. This
helps with error handling and provides meaningful error messages
to users.

The `teardown_appcontext` function is used as a decorator with
the @app.teardown_appcontext annotation. This function is called
when the application context is torn down, allowing for any
necessary cleanup operations. In this case, it closes the
SQLAlchemy session.

To run this Flask application, execute the script using Python 3.
For example, if the script is saved as app.py, run it with the
command "python3 app.py". The application will be accessible at
http://0.0.0.0:5000/states and http://0.0.0.0:5000/states/<id>.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Displays an HTML page with a list of all State objects.
    States are sorted by name.

    Exceptions:
        Exception: If an error occurs during the retrieval of
                   states from storage.

    Returns:
        str: HTML page with the list of states, or an error
             message.
    """
    try:
        states = storage.all("State")
        return render_template("9-states.html", states=states)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Displays an HTML page with information about the state with
    the given <id>, if it exists.

    Parameters:
        id (str): The identifier of the state.

    Exceptions:
        Exception: If an error occurs during the retrieval of
                   states from storage.

    Returns:
        str: HTML page with the state information, or an error
             message if the state is not found.
    """
    try:
        for state in storage.all("State").values():
            if state.id == id:
                return render_template("9-states.html", state=state)
        return render_template("9-states.html")
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
