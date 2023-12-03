from flask import Flask

app = Flask(__name__)
visited = 0


def visited_inc():
    visited += 1
    return visited


@app.route("/")
def hello_world():
    return f"<p>Hello, World! Visited {visited_inc(visited)} times</p>"
