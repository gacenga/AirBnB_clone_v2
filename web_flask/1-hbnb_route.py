#!/usr/bin/python3
"""
   simple flask app

"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnh():
    """ intro """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ name """
    return "HBNB"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
