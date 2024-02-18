#!/usr/bin/python3
# Importing Flask module from the flask package. Flask is a web framework.
from flask import Flask

# Creating a new web application instance.
app = Flask(__name__)

# Defining a route for the URL '/'.
# The 'strict_slashes=False' argument allows the route
#to match URLs with or without a trailing slash.
@app.route('/', strict_slashes=False)
def hello_hbnb():
    # This function will run when the '/' URL is accessed.
    # It returns the string 'Hello HBNB!' as a response.
    return 'Hello HBNB!'

# This conditional is used to ensure
# the server only runs if the script is executed directly.
if __name__ == '__main__':
    # Running the server.
    # The 'host' argument is set to '0.0.0.0'
    # to make the server publicly available.
    # The 'port' argument is set to '5000',
    # which is a common port for web services.
    app.run(host='0.0.0.0', port=5000)
