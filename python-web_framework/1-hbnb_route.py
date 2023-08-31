"""
Starting a Flask web application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index(strict_slashes=False):
    return "Hello HBNB!"

@app.route("/hbnb")
def index(strict_slashes=False):
    return "HBNB"

if __name__ == "__main__":
 app.run(host='0.0.0.0', port=5000)
