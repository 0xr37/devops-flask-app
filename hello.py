from flask import Flask
import redis
import time
import json
import os


app = Flask(__name__)

r = redis.Redis(
        host=os.environ.get("REDIS_HOST", "the-redis-server"),
        port=6379,
        decode_responses=True
)

def cached_page(key, html):
    data = r.get(key)

    if data is not None:
        data = json.loads(data)
        if time.time() - data["time"] <=600:
            return data["html"]

    r.set(key, json.dumps({
        "html": html,
        "time": time.time()
    }))

    return html



@app.route("/")
def home():
    html = '<p>Welcome!</p><a href="/about">About</a><a href="/contact">Contact</a>'
    return cached_page("home", html)


@app.route("/about")
def about():
    html = '<p>This application is running on the Flask web framework.</p><p><a href="https://flask.palletsprojects.com/">Learn more about Flask</a></p><p><a href="https://www.python.org/">Learn more about Python</a></p>'
    return cached_page("about", html)

@app.route("/contact")
def contact():
    html = '<p>Contact: contact@r37.dev</p>'
    return cached_page("contact", html)


