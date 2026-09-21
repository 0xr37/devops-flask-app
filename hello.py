from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '<p>Hello, World, I am a Flask app!</p><a href="/about">About</a>'

@app.route("/about")
def about():
    return '<p>This application is running on the Flask web framework.</p><a href="https://flask.palletsprojects.com/">Learn more about Flask</a>'
