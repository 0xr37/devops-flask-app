from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '<p>Welcome!</p><a href="/about">About</a><a href="/contact">Contact</a>'

@app.route("/about")
def about():
    return '<p>This application is running on the Flask web framework.</p><a href="https://flask.palletsprojects.com/">Learn more about Flask</a>'

@app.route("/contact")
def contact():
    return '<p>Contact: contact@r37.dev</p>'