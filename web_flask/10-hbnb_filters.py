#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.

Routes:
    /hbnb_filters: HBnB HTML filters page.

This script starts a Flask web application that provides one route:
- The "/hbnb_filters" route displays the HBnB HTML filters page.

The application listens on the IP address 0.0.0.0, allowing it
to accept requests from any available network interface. It uses
port 5000 as the default port for incoming connections.

The "/hbnb_filters" route triggers the `hbnb_filters` function,
which retrieves all the states and amenities from the storage
module using the `storage.all()` method. The retrieved states and
amenities are then passed to the `render_template` function along
with the name of the HTML template file, "10-hbnb_filters.html".

In case an exception occurs during the execution of the
`hbnb_filters` function, the exception is caught, and an error
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
http://0.0.0.0:5000/hbnb_filters.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Displays the main HBnB filters HTML page.

    Exceptions:
        Exception: If an error occurs during the retrieval of
                   states or amenities from storage.

    Returns:
        str: HTML page with the HBnB filters, or an error
             message.
    """
    try:
        states = storage.all("State")
        amenities = storage.all("Amenity")
        return render_template("10-hbnb_filters.html",
                               states=states, amenities=amenities)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
