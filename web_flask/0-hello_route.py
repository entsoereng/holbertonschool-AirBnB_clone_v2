from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
@app.route("/")
def hello():
    return "Hello HBNB!"
=======

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> daa88c421bffcbdb0df71b17622649b8499644e9
