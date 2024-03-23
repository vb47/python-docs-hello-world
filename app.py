from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h2>Navigate to /about to know about me. :-)</h2>"

@app.route("/about")
def about():
    return "<h1>Hi, I am Vaibhav.</h1><br/><br/><h3>Naam hi kaafi he.</h3>"
