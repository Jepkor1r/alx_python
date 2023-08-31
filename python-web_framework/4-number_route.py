"""
Starting a Flask web application
"""
from flask import Flask
from markupsafe import escape

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index(strict_slashes=False):
    """"
    This function handles requests to the root URL ("/") of the web application.
    
    Returns:
        str: A simple greeting message "Hello HBNB!"
    """
    return "Hello HBNB!"

# Define a route for the "/hbnb" URL
@app.route("/hbnb")
def hbnb(strict_slashes=False):
    """"
      This function handles requests to the "/hbnb" URL of the web application.
    
    Returns:
        str: A message "HBNB" 
    """
    return "HBNB"

# Define a route for the "c/<text>" URL
@app.route("/c/<text>")
def c(text, strict_slashes=False):
    """"
      This function handles requests to the "c/<text>" URL of the web application.
    
    Returns:
        str: A message "C 'followed by the value of the text variable'" 
    """
    text = text.replace("_", " ")
    return f"C {escape(text)}"

# Define a route for the "python/<text>" URL
@app.route("/python/", defaults={"text":"is cool"})
@app.route("/python/<text>")
def python(text, strict_slashes=False):
    """"
      This function handles requests to the "python/<text>" URL of the web application.
    
    Returns:
        str: A message "Python followed by the value of the text variable" 
    """
    text = text.replace("_", " ")
    return f"Python {escape(text)}"

# Define a route for the "number/<n>" URL
@app.route("/number/<int:n>/")
def number(n, strict_slashes=False):
    """"
      This function handles requests to the "number/<n>" URL of the web application.
    
    Returns:
        str: A message "n is a number” and only if n is an integer" 
    """
    if n==int:
        return f"{escape(n)} is a number"
    else:
        return(404)

# Entry point of the application
if __name__ == "__main__":
    # Run the Flask application on all available network interfaces (host='0.0.0.0')
    # and use port 5000 for communication
    app.run(host='0.0.0.0', port=5000)
