# 0-hello_route.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello HBNB!"
