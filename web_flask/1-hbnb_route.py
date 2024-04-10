#!/usr/bin/python3
""" Start a Flask Web Application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message """
    return 'Hello HBNB!'
  
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints a Message """
    return 'HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
