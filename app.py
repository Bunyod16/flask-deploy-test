from flask import Flask

app = Flask(__name__)
visited = 0


@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"
